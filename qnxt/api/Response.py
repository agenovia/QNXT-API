import json
import logging


class Response:
    def __init__(self, http_response):
        self.http_response = http_response
        self._json = json.loads(self.http_response.text)

    def __str__(self):
        pretty = json.dumps(self._json, indent=4, sort_keys=True)
        return pretty

    def __repr__(self):
        return self.__str__()

    @property
    def metadata(self) -> dict:
        try:
            return self._json['processMetadata']
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract metadata from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def results(self) -> dict:
        try:
            return self._json['results']
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract results from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def overview(self) -> dict:
        try:
            d = {k: v for k, v in self._json.items() if k not in ['results', 'processMetadata']}
            return d
        except KeyError as e:
            print(self.__str__(), 'Exception encountered in attempting to extract results from HTTP response')
            logging.exception(e, exc_info=True)

    @property
    def json(self) -> dict:
        return self._json
