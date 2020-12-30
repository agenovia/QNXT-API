from datetime import datetime, date
from typing import Union

import requests

from qnxt.authentication import RequestHeader
# from qnxt.utils.dateutil import dateformat
# from qnxt.utils.clean_url import clean_url
from qnxt.api.Response import Response
from qnxt.utils import *


class BenefitResource:
    """
    Benefits are services that are included in a benefit plan. Each benefit is defined by cost share, copayments,
    covered services, procedures, diagnostic codes, restrictions, limits, and service categories. The Benefit resource
    provides access to stored values for benefits.
    """
    BASE_PATH = r'QNXTApi/Benefit'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 ):
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}"
        self.header_factory = header_factory

    def get_accumulators(self,
                         plan_id,
                         benefit_id
                         ) -> Response:
        """
        This operation returns accumulators data such as AccumId, AccumType, and Description, based on the plan ID
        and benefit ID passed in the endpoint.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"benefits/{plan_id}/{benefit_id}/accumulators"
        uri = f"{self.base_uri}/{endpoint}"
        response = requests.get(uri, headers=self.header_factory())
        return Response(response)

    def get_benefit(self,
                    plan_id: str,
                    benefit_id: str,
                    ) -> Response:
        """
        This operation returns benefit data, based on the plan ID and benefit ID passed in the endpoint.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"benefits/{plan_id}/{benefit_id}"
        uri = f"{self.base_uri}/{endpoint}"
        response = requests.get(uri, headers=self.header_factory())
        return Response(response)

    def get_coverage_details(self,
                             plan_id: str,
                             benefit_id: str,
                             enroll_id: str = None,
                             as_of: Union[date, datetime, str] = None,
                             expand: str = None,
                             ) -> Response:
        """
        This operation returns benefit data including limits and restrictions, based on the plan ID and benefit ID
        passed in the endpoint.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"benefits/{plan_id}/{benefit_id}/details"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'enrollId': enroll_id,
                  'asOfDate': as_of,
                  'expand': expand
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class BenefitPlan:
    BASE_PATH = r'QNXTApi/Benefit/plans'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 plan_id: str,
                 expand: str = None,
                 enroll_type: str = None,
                 as_of: Union[date, datetime, str] = None
                 ):
        self.base_uri = f"{clean_url(app_server, self.BASE_PATH)}/{plan_id}"
        self.header_factory = header_factory

        self.expand = expand
        self.enroll_type = enroll_type
        self.as_of = as_of

    def get_benefit_plan(self, **kwargs) -> Response:
        """Takes in the optional parameter expand"""
        uri = self.base_uri
        params = {'expand': self.expand}
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_benefit_plan_details(self, **kwargs) -> Response:
        """Takes in the optional parameters enrollType and asOfDate"""
        endpoint = "details"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'enrollType': self.enroll_type, 'asOfDate': self.as_of}
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory())
        return Response(response)

    def since(self, as_of: Union[date, datetime, str]):
        """Pass either a datetime/date object or a string in ISO format to set the class' asOfDate parameter.
        This parameter only affects the get_details method"""
        self.as_of = dateutil.dateformat(as_of)
