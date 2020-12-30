import json
import logging


class Response:
    def __init__(self, http_response):
        """
        Pass an `http_response` to get methods for quickly inspecting its contents and provide support for pretty
        printing.

        Parameters
        ----------
        http_response: requests.models.Response
            An HTTP response object returned by the requests module

        Examples
        --------
        >>> import requests
        >>> from qnxt.api import Response
        >>> response = requests.get('https://app_server.com/endpoint')
        >>> response = Response(response)
        >>> response.head(5)
        ...
        """
        self.http_response = http_response
        self._json = json.loads(self.http_response.text)

    def __str__(self):
        pretty = json.dumps(self._json, indent=4, sort_keys=True)
        return pretty

    def __repr__(self):
        return self.__str__()

    @property
    def metadata(self) -> dict:
        """Returns a dictionary of the metadata section of the `http_response`"""
        try:
            return self._json['processMetadata']
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract metadata from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def results(self) -> dict:
        """Returns a dictionary of the results section of the `http_response`"""
        try:
            return self._json['results']
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract results from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def overview(self) -> dict:
        """Returns a dictionary of the top-level overview of the `http_response`"""
        try:
            d = {k: v for k, v in self._json.items() if k not in ['results', 'processMetadata']}
            return d
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract results from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def json(self) -> dict:
        """Returns a dictionary of the entire `http_response`"""
        return self._json

    def _get_n_results(self, n: int, head: bool = True) -> list:
        """Returns the first `n` items from the 'results' list if `head` is True, else return the last `n`

        Parameters
        ----------
        n: int
            The number of results to return
        head: bool, optional
            If True, then return the first `n` items of the 'results' list, else return the last `n`

        Raises
        ------
        AssertionError
            `n` has to be greater than 0
        """
        assert (n > 0), "`n` must be greater than 0"
        if head is True:
            return self._json['results'][:n]
        else:
            return self._json['results'][-n:]

    def head(self, n: int = 5) -> list:
        """
        Pretty prints the top `n` 'results' in the Response object and returns its list form

        Parameters
        ----------
        n: int
            The top `n` results to pretty print and return
        """
        __results = self._get_n_results(n)
        pretty = json.dumps(__results, indent=4, sort_keys=True)
        print(pretty)
        return __results

    def tail(self, n: int = 5) -> list:
        """
        Pretty prints the bottom `n` 'results' in the Response object and returns its list form

        Parameters
        ----------
        n: int
            The bottom `n` results to pretty print and return
        """
        __results = self._get_n_results(n, head=False)
        pretty = json.dumps(__results, indent=4, sort_keys=True)
        print(pretty)
        return __results
