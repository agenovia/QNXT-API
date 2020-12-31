import requests

from qnxt.authentication import RequestHeader
from qnxt.api.Response import Response

forcing a linting error

class Search:
    BASE_PATH = r'QNXTApi/AppealAndGrievance/agIncidents/search'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 skip: int = None,
                 take: int = None,
                 order_by: str = None,
                 expand: str = None,
                 ):
        if app_server.endswith('/'):
            self.base_uri = f"{app_server[:-1]}{self.BASE_PATH}"
        else:
            self.base_uri = f"{app_server}/{self.BASE_PATH}"
        self.header_factory = header_factory

        self.skip = skip
        self.take = take
        self.order_by = order_by
        self.expand = expand

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def get_details_by_id(self, detail_id, **kwargs) -> Response:
        uri = self.base_uri
        params = {'skip': self.skip, 'take': self.take, 'orderBy': self.order_by, 'expand': self.expand}
        params.update(kwargs)
        params.update({'detailId': detail_id})
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_details_by_type(self, detail_type, **kwargs) -> Response:
        uri = self.base_uri
        params = {'skip': self.skip, 'take': self.take, 'orderBy': self.order_by, 'expand': self.expand}
        params.update(kwargs)
        params.update({'detailType': detail_type})
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_details_by_status(self, statuses, **kwargs) -> Response:
        uri = self.base_uri
        params = {'skip': self.skip, 'take': self.take, 'orderBy': self.order_by, 'expand': self.expand}
        params.update(kwargs)
        params.update({'statuses': statuses})
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def ascending(self):
        """Update the class' orderBy parameter to ascending"""
        self.order_by = 'ascending'

    def descending(self):
        """Update the class' orderBy parameter to descending"""
        self.order_by = 'descending'
