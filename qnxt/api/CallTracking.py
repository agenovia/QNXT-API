import requests
from qnxt.authentication import RequestHeader
from typing import Union
from datetime import date, datetime
from qnxt.utils import *
from qnxt.api.Response import Response


# TODO need to add extensive docstrings for each API class


class CallStatistics:
    BASE_PATH = r'QNXTApi/CallTracking/stats/calls/dates/count'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 memid: str = None,
                 provid: str = None,
                 eligible_orgid: str = None,
                 date_type: str = None,
                 date_from: Union[date, datetime, str] = None,
                 date_to: Union[date, datetime, str] = None,
                 entity_state: str = None
                 ):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

        self.memid = memid
        self.provid = provid
        self.eligible_orgid = eligible_orgid
        self.date_type = date_type
        self.date_from = date_from
        self.date_to = date_to
        self.entity_state = entity_state

    def from_date(self, date_object):
        self.date_from = dateutil.dateformat(date_object)

    def to_date(self, date_object):
        self.date_to = dateutil.dateformat(date_object)

    def get_statistics(self, **kwargs) -> Response:
        uri = self.base_uri
        params = {'memid': self.memid,
                  'provId': self.provid,
                  'eligibleOrgId': self.eligible_orgid,
                  'dateType': self.date_type,
                  'dateFrom': self.date_from,
                  'dateTo': self.date_to,
                  'entityState': self.entity_state
                  }
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class CallResource:
    BASE_PATH = r'QNXTApi/CallTracking'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 memid: str = None,
                 userid: str = None,
                 callerid: str = None,
                 managerid: str = None,
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
                 access_group_control: str = None,
                 skip: int = None,
                 take: int = None,
                 orderby: str = None,
                 expand: str = None
                 ):
        self.base_uri = clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

        self.memid = memid
        self.userid = userid
        self.callerid = callerid
        self.managerid = managerid
        self.provid = provid
        self.eligible_orgid = eligible_orgid
        self.claimid = claimid
        self.referralid = referralid
        self.assigned_to_userid = assigned_to_userid
        self.status = status
        self.callsourceid = callsourceid
        self.submitmethod = submitmethod
        self.calldate_from = calldate_from
        self.calldate_to = calldate_to
        self.access_group_control = access_group_control
        self.skip = skip
        self.take = take
        self.orderby = orderby
        self.expand = expand

    def search_call_issues(self, **kwargs) -> Response:
        endpoint = "callIssues/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'memId': self.memid,
                  'provId': self.provid,
                  'eligibleOrgId': self.eligible_orgid,
                  'claimId': self.claimid,
                  'referralId': self.referralid,
                  'assignedToUserId': self.assigned_to_userid,
                  'status': self.status,
                  'callSourceId': self.callsourceid,
                  'submitMethod': self.submitmethod,
                  'callDateFrom': self.calldate_from,
                  'callDateTo': self.calldate_to,
                  'skip': self.skip,
                  'take': self.take,
                  'orderBy': self.orderby,
                  'expand': self.expand,
                  }
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def search_call_details(self, **kwargs) -> Response:
        endpoint = 'calls/search'
        uri = f"{self.base_uri}/{endpoint}"
        params = {'callerId': self.callerid,
                  'memId': self.memid,
                  'provId': self.provid,
                  'eligibleOrgId': self.eligible_orgid,
                  'managerId': self.managerid,
                  'callDateFrom': self.calldate_from,
                  'callDateTo': self.calldate_to,
                  'status': self.status,
                  'userId': self.userid,
                  'accessGroupControl': self.access_group_control,
                  'skip': self.skip,
                  'take': self.take,
                  'orderBy': self.orderby,
                  'expand': self.expand
                  }
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_call_details(self):
        # TODO
        pass

    def get_calls_by_callerid(self):
        # TODO
        pass
