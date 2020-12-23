import requests
from qnxt.authentication import RequestHeader
from typing import Union
from datetime import date, datetime
from qnxt.utils import *
from qnxt.api.Response import Response


class ApplicationLogs:
    """This operation returns application logs, based on the data passed in the request."""
    BASE_PATH = r"QNXTApi/PlanIntegration"

    def __init__(self,
                 app_server,
                 header_factory,
                 expand: str = None,
                 level: str = None,
                 loginid: str = None,
                 machine_name: str = None,
                 order_by: str = None,
                 referenceid: str = None,
                 skip: int = 0,
                 source: str = None,
                 source_category: str = None,
                 take: int = None,
                 utc_date_from: Union[date, datetime, str] = None,
                 utc_date_to: Union[date, datetime, str] = None,
                 ):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.app_server = app_server
        self.header_factory = header_factory

        self.expand = expand,
        self.level = level,
        self.loginid = loginid,
        self.machine_name = machine_name,
        self.order_by = order_by,
        self.referenceid = referenceid,
        self.skip = skip,
        self.source = source,
        self.source_category = source_category,
        self.take = take,
        self.utc_date_from = dateutil.dateformat(utc_date_from),
        self.utc_date_to = dateutil.dateformat(utc_date_to),

    def from_date(self, date_object):
        self.utc_date_from = dateutil.dateformat(date_object)

    def to_date(self, date_object):
        self.utc_date_to = dateutil.dateformat(date_object)

    def search(self, **kwargs):
        endpoint = r"applicationLogs/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': self.expand,
                  'level': self.level,
                  'loginId': self.loginid,
                  'machineName': self.machine_name,
                  'orderBy': self.order_by,
                  'referenceId': self.referenceid,
                  'skip': self.skip,
                  'source': self.source,
                  'sourceCategory': self.source_category,
                  'take': self.take,
                  'utcDateFrom': self.utc_date_from,
                  'utcDateTo': self.utc_date_to
                  }
        params = params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogs:
    """Provide a processLogDetailID and retrieve full details"""
    BASE_PATH = r'QNXTApi/PlanIntegration'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 process_log_detailid
                 ):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

        self.process_log_detailid = process_log_detailid

    def get_details(self, **kwargs):
        endpoint = f"ProcessLogDetails/{self.process_log_detailid}/xmls"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processLogDetailId': self.process_log_detailid
                  }
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogDetails:
    def __init__(self):
        pass


class ProcessLogHeaders:
    def __init__(self):
        pass
