import requests
from qnxt.authentication import RequestHeader
from typing import Union
from datetime import date, datetime
from qnxt.utils import *
from qnxt.api.Response import Response


# TODO need to add extensive docstrings for each API class


class CallStatistics:
    BASE_PATH = r'QNXTApi/CallTracking/stats/calls/dates/count'

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

    def get_statistics(self,
                       memid: str = None,
                       provid: str = None,
                       eligible_orgid: str = None,
                       date_type: str = None,
                       date_from: Union[date, datetime, str] = None,
                       date_to: Union[date, datetime, str] = None,
                       entity_state: str = None
                       ) -> Response:
        uri = self.base_uri
        params = {'memid': memid,
                  'provId': provid,
                  'eligibleOrgId': eligible_orgid,
                  'dateType': date_type,
                  'dateFrom': date_from,
                  'dateTo': date_to,
                  'entityState': entity_state
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class CallResource:
    BASE_PATH = r'QNXTApi/CallTracking'

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

    def search_call_issues(self,
                           memid: str = None,
                           provid: str = None,
                           eligible_orgid: str = None,
                           claimid: str = None,
                           referralid: str = None,
                           assigned_to_userid: str = None,
                           status: str = None,
                           callsourceid: str = None,
                           submitmethod: str = None,
                           calldate_from: Union[date, datetime, str] = None,
                           calldate_to: Union[date, datetime, str] = None,
                           skip: int = None,
                           take: int = None,
                           orderby: str = None,
                           expand: str = None
                           ) -> Response:
        endpoint = "callIssues/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'memId': memid,
                  'provId': provid,
                  'eligibleOrgId': eligible_orgid,
                  'claimId': claimid,
                  'referralId': referralid,
                  'assignedToUserId': assigned_to_userid,
                  'status': status,
                  'callSourceId': callsourceid,
                  'submitMethod': submitmethod,
                  'callDateFrom': calldate_from,
                  'callDateTo': calldate_to,
                  'skip': skip,
                  'take': take,
                  'orderBy': orderby,
                  'expand': expand,
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def search_call_details(self,
                            memid: str = None,
                            userid: str = None,
                            callerid: str = None,
                            managerid: str = None,
                            provid: str = None,
                            eligible_orgid: str = None,
                            status: str = None,
                            calldate_from: Union[date, datetime, str] = None,
                            calldate_to: Union[date, datetime, str] = None,
                            access_group_control: str = None,
                            skip: int = None,
                            take: int = None,
                            orderby: str = None,
                            expand: str = None
                            ) -> Response:
        endpoint = 'calls/search'
        uri = f"{self.base_uri}/{endpoint}"
        params = {'callerId': callerid,
                  'memId': memid,
                  'provId': provid,
                  'eligibleOrgId': eligible_orgid,
                  'managerId': managerid,
                  'callDateFrom': calldate_from,
                  'callDateTo': calldate_to,
                  'status': status,
                  'userId': userid,
                  'accessGroupControl': access_group_control,
                  'skip': skip,
                  'take': take,
                  'orderBy': orderby,
                  'expand': expand
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_call_details(self, callerid: str, expand: str = None) -> Response:
        endpoint = f"calls/{callerid}/issues"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_calls_by_callerid(self, callerid: str, expand: str = None) -> Response:
        endpoint = f"calls/{callerid}"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)
