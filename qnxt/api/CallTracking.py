from datetime import date, datetime
from typing import Union

import requests

from qnxt.api.Response import Response
from qnxt.authentication import RequestHeader
from qnxt.utils import *


# TODO need to add extensive docstrings for each API class


class CallStatistics:
    """The Call Statistics resource stores statistics related to call records. The Call Statistics resource includes
    stored values for calls, including the year, month, and day they occurred."""

    BASE_PATH = r'QNXTApi/CallTracking/stats/calls/dates/count'

    def __init__(self, app_server: str, header_factory: RequestHeader):
        """
        Parameters
        ----------
        app_server: str, optional
            This is the FQDN of the target QNXT app server
        header_factory: qnxt.authentication.RequestHeader, required
            This is a callable that generates the appropriate authentication headers for QNXT API requests
        """
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

    def get_call_count(self,
                       memid: str = None,
                       provid: str = None,
                       eligible_orgid: str = None,
                       date_type: str = None,
                       date_from: Union[date, datetime, str] = None,
                       date_to: Union[date, datetime, str] = None,
                       entity_state: str = None
                       ) -> Response:
        """This operation returns the number (total count) of calls in the last month, quarter, and year, based on the
        data passed in the request.

        Parameters
        ----------
        memid: str, optional
            calltrack.memid
            The unique system identifier for the member.
        provid: str, optional
            callreasonclaim.callerid
            Primary key of calltrack table.
        eligible_orgid: str, optional
            callreasonclaim.callerid
            Primary key of calltrack table.
        date_type: str, optional
            The type of the date.
        date_from: [date, datetime, str], optional
            calltrack.calldate
            The call date of the call tracking entry.
        date_to: [date, datetime, str], optional
            calltrack.calldate
            The call date of the call tracking entry.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """

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
    """The Calls resource stores call records that include general, descriptive information about the call, and
    detailed information about the specific healthcare-related issue. The Calls resource includes stored values for
    dates, sources, assignments, submit methods, status, and identifiers such as call, claim, referral, member, and
    provider IDs."""

    BASE_PATH = r'QNXTApi/CallTracking'

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

    def search_call_issues(self,
                           memid: str = None,
                           provid: str = None,
                           eligible_orgid: str = None,
                           claimid: str = None,
                           referral_id: str = None,
                           assigned_to_userid: str = None,
                           status: str = None,
                           callsource_id: str = None,
                           submit_method: str = None,
                           calldate_from: Union[date, datetime, str] = None,
                           calldate_to: Union[date, datetime, str] = None,
                           skip: int = None,
                           take: int = None,
                           order_by: str = None,
                           expand: str = None
                           ) -> Response:
        """This operation returns all issues associated with the calls based on the data passed in the request.

        Parameters
        ----------
        memid: str, optional
            calltrack.memid
            The member ID in the calltrack record. This is the primary key of the member table.
        provid: str, optional
            calltrack.provId
            The provider ID in the calltrack record. This is the primary key of the provider table.
        eligible_orgid: str, optional
            calltrack.eligibleorgid
            The identifier for the eligibility organization. This is the primary key of the eligibilityorg table.
        claimid: str, optional
            callreasonclaim.claimid
            The claim ID on the callreasonclaim record. This is the primary key of the claim table.
        referral_id: str, optional
            callreasonreferral.ReferralId
            Primary key of the referal table.
        assigned_to_userid: str, optional
            callreason.userid
            The identifier for the user who logged the call.
        status: str, optional
            callreason.status
            The status of the callreason record.
        callsource_id: str, optional
            calltrack.callsourceid
            The call source ID in the calltrack record. This is the primary key of the callsource table.
        submit_method: str, optional
            calltrack.SubmittalMethod
            Indicates how the request was submitted (e.g., Email, Fax, Call, Walk-In, Letter, etc.).
        calldate_from: [date, datetime, str], optional
            calltrack.calldate
            The date in the calltrack record. This is the primary key of the callsource table.
        calldate_to: [date, datetime, str], optional
            calltrack.calldate
            The date in the calltrack record. This is the primary key of the callsource table.
        skip: int, optional
            The Skip value identifies the subset of query results by defining the number of records to bypass in the
            query result set before paging begins.
        take: int, optional
            The Take value (also known as page size) identifies the subset of query results by defining the number of
            records to return in the query result set.
        order_by: str, optional
            The OrderBy value specifies how to sort the query result set. Sort options (ascending, descending) can be
            applied to one or more sortable columns, in any order.
        expand: str, optional
            The Expand value specifies which properties to include in the query result set for complex objects.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """

        endpoint = "callIssues/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'memId': memid,
                  'provId': provid,
                  'eligibleOrgId': eligible_orgid,
                  'claimId': claimid,
                  'referralId': referral_id,
                  'assignedToUserId': assigned_to_userid,
                  'status': status,
                  'callSourceId': callsource_id,
                  'submitMethod': submit_method,
                  'callDateFrom': calldate_from,
                  'callDateTo': calldate_to,
                  'skip': skip,
                  'take': take,
                  'orderBy': order_by,
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
        """This operation returns all calls, based on the data passed in the request."""

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
        """This operation returns call issues, based on the caller ID passed in the endpoint."""

        endpoint = f"calls/{callerid}/issues"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_calls_by_callerid(self, callerid: str, expand: str = None) -> Response:
        """This operation returns call details, based on the caller ID passed in the endpoint."""

        endpoint = f"calls/{callerid}"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


if __name__ == '__main__':
    help(CallResource.search_call_issues)
