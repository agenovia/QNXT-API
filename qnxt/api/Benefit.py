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
    Get Accumulators
    Get Benefit
    Get Benefit Coverage Detail
    """
    BASE_PATH = r'QNXTApi/Benefit/benefits'

    def __init__(self,
                 app_server: str,
                 header_factory: RequestHeader,
                 plan_id: str,
                 benefit_id: str,
                 expand: str = None,
                 enrollid: str = None,
                 as_of: Union[date, datetime, str] = None
                 ):
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}/{plan_id}/{benefit_id}"
        self.header_factory = header_factory

        # be mindful that only the get_details method uses takes in any parameters
        self.expand = expand
        self.enrollid = enrollid
        self.as_of = as_of

    def get_benefit(self) -> Response:
        """According to the docs, this does not take any parameters"""
        uri = self.base_uri
        response = requests.get(uri, headers=self.header_factory())
        return Response(response)

    def get_accumulator(self) -> Response:
        """According to the docs, this does not take any parameters"""
        endpoint = "accumulators"
        uri = f"{self.base_uri}/{endpoint}"
        response = requests.get(uri, headers=self.header_factory())
        return Response(response)

    def get_details(self, **kwargs) -> Response:
        """This is the only method for this class that takes in any parameters and is the only one affected by the
        'since' method and the enrollid and expand class parameters. The kwargs argument allows for setting parameters
        during call time"""
        endpoint = "details"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'enrollid': self.enrollid, 'expand': self.expand}
        params.update(kwargs)
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def since(self, as_of: Union[date, datetime, str]):
        """Pass either a datetime/date object or a string in ISO format to set the class' asOfDate parameter.
        This parameter only affects the get_details method"""
        self.as_of = dateutil.dateformat(as_of)


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
