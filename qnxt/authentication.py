import json
import time
import logging
import datetime
import requests
from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth
from typing import Union


class RequestHeader:
    ENDPOINT = r'/QnxtSTS'

    def __init__(self, fqdn: str, envid: Union[str, int], auth: Union[HTTPBasicAuth, HttpNtlmAuth], thresh: int = 300):
        """
        A 'header factory' that can be passed to the API classes to allow for the retrieval of tokens that are always
        valid and not expired. RequestHeader requests an access token from the STS endpoint, calculates the expiry
        minus the `thresh` and ensures that a valid token is always ready when it is called.

        Parameters
        ----------
        fqdn: str
            The fully qualified domain name of the STS (token signing) server.
        envid: str or int
            The environment ID. Must match the environment IDs of the app servers you will be making API calls to.
        auth: requests.auth.HTTPBasicAuth or requests_ntlm.HttpNtlmAuth
            The authentication object to use. Can either be a basic HTTP Auth object or a Windows auth object.
        thresh: int, optional, default 300
            `thresh` seconds will be subtracted from the expiry time of the token (3600 seconds). This is used to
            calculate when the RequestHeader class will attempt to retrieve a new token.

        Examples
        --------
        >>> from qnxt.api import PlanIntegration
        >>> auth_obj = basic_authentication('Service_User', 'Service_Password')
        >>> header_factory = RequestHeader(r"http://qnxt_sts_server.com", '1', auth_obj, 500)
        >>> app_server = r"http://qnxt_app_server.com"
        >>> plan_integration = PlanIntegration(app_server, header_factory)
        >>> plan_integration.search(level='Error')
        ...
        """
        self.thresh = thresh
        self.auth = auth
        self.envid = str(envid)

        if fqdn.endswith('/'):
            self.fqdn = fqdn[:-1]
        else:
            self.fqdn = fqdn
        self.uri = f"{self.fqdn}/{self.ENDPOINT}"

        self.headers = {"Accept": "application/json",
                        "x-TZ-EnvId": envid
                        }

        # these will be updated by get_token and update_token respectively
        self.expiry = 0
        self.token = None

    def __call__(self):
        """Call the class to return valid request headers"""
        self.update_token()
        auth_header = {"Authorization": f"{self.token['token_type']} {self.token['access_token']}"}
        return {**self.headers, **auth_header}

    def __str__(self):
        self.__call__()
        msg = f"""
        STS Server: {self.fqdn}
        Authentication Type: {type(self.auth).__name__}
        Authentication User: {self.auth.username}
        Refresh Threshold: {self.thresh} seconds ({round(self.thresh/60.00, 2)} minutes)
        Refreshes On: {self.token['refreshes_on']} ({round((self.expiry - time.time())/60.00, 2)} minutes)
        Token Type: {self.token['token_type']}
        Access Token: {self.token['access_token']}
        """
        return msg

    def __repr__(self):
        return f"RequestHeader(fqdn={self.fqdn}, envid={self.envid}, auth={type(self.auth)}, thresh={self.thresh})"

    def update_token(self):
        """Check for expiry based on the thresh value given to the constructor; if expired, then update the token with
        a new one"""
        if time.time() >= self.expiry:
            self.token = self.get_token()
            self.token['refreshes_on'] = str(datetime.datetime.fromtimestamp(self.expiry))

    def get_token(self):
        """Make a request to the URI and return the access token"""
        response = requests.get(self.uri, headers=self.headers, auth=self.auth)
        logging.debug(f"{response.status_code}: {response.reason}")
        _json = json.loads(response.text)
        if response.ok:
            self.expiry = (time.time() + _json['expires_in']) - self.thresh
            return _json
        raise requests.HTTPError(_json['error_description'])


def basic_authentication(username, password):
    """Returns an HTTPBasicAuth object that can be used to pass to RequestHeader"""
    return HTTPBasicAuth(username, password)


def windows_authentication(username, password, *args, **kwargs):
    """Returns an HttpNtlmAuth object that can be used to pass to RequestHeader"""
    return HttpNtlmAuth(username, password, *args, **kwargs)


if __name__ == '__main__':
    pass