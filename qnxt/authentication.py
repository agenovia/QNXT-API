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

    def __init__(self, fqdn: str, envid: str, auth: Union[HTTPBasicAuth, HttpNtlmAuth], thresh: int = 300):
        """
        Requests an access token from the STS endpoint. Determine whether or not it is `thresh` seconds away from
        expiry before requesting a new one.
        """
        self.thresh = thresh
        self.auth = auth
        self.envid = envid

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
        """Call the class to return non-expired headers"""
        self.update_token()
        auth_header = {"Authorization": f"{self.token['token_type']} {self.token['access_token']}"}
        return {**self.headers, **auth_header}

    def __str__(self):
        self.__call__()
        msg = f"""
        STS Server: {self.fqdn}
        Authentication Type: {type(self.auth).__name__}
        Authentication User: {self.auth.username}
        Expiry Threshold: {self.thresh} seconds ({self.thresh/60.00} minutes)
        Refreshes On: {self.token['refreshes_on']} ({round((self.expiry - time.time())/60, 0)} minutes)
        Token: {self.token['access_token']}
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
        if response.ok:
            _json = json.loads(response.text)
            self.expiry = (time.time() + _json['expires_in']) - self.thresh
            return _json
        return None


def basic_authentication(username, password):
    return HTTPBasicAuth(username, password)


def windows_authentication(username, password, *args, **kwargs):
    return HttpNtlmAuth(username, password, *args, **kwargs)
