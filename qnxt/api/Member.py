"""The Member API provides access to member data including eligibility and enrollments, relationships, conditions,
restrictions, assigned providers, benefits and accumulations, and memos and alerts"""

from datetime import date, datetime
from typing import Union

import requests

from qnxt.api.Response import Response
from qnxt.authentication import RequestHeader
from qnxt.utils import *


class COPCProviders:
    """The Continuity of Physician Care (COPC) feature provides you with the ability to configure QNXT to continue
    paying claims based on a provider contract that has terminated from the network for reasons other than fraud. You
    can associate members with COPC providers and the conditions they can treat. The COPC Providers resource includes
    stored values for COPC providers, including address information and identifiers."""
    BASE_PATH = r"QNXTApi/Member"

    def __init__(self, app_server: str, header_factory: RequestHeader):
        """
        Parameters
        ----------
        app_server: str, optional
            This is the FQDN of the target QNXT app server
        header_factory: qnxt.authentication.RequestHeader, required
            This is a callable that generates the appropriate authentication headers for QNXT API requests
        """
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}"
        self.header_factory = header_factory

    def get_copc_enrollment_providers(self,
                                      enroll_id: str,
                                      as_of_date: Union[date, datetime, str] = None,
                                      skip: int = None,
                                      take: int = None,
                                      order_by: str = None,
                                      expand: str = None,
                                      ) -> Response:
        """This operation returns COPC providers for a member enrollment, based on the enrollment ID passed in the
        endpoint.

        Parameters
        ----------
        enroll_id: str, required
            Primary key of the enrollment table
        as_of_date: [date, datetime, str], optional
            AsOfDate property - - To get active copc providers, compare with copc.effdate and copc.termdate
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
        endpoint = f"enrollments/{enroll_id}/copcProviders"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'asOfDate': dateutil.dateformat(as_of_date),
                  'skip': skip,
                  'take': take,
                  'order_by': order_by,
                  'expand': expand,
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def validate_copc_provider(self,
                               enroll_id: str,
                               prov_id: str,
                               as_of_date: Union[date, datetime, str] = None,
                               diag_codes=None,
                               code_id=None,
                               icd_version=None
                               ) -> Response:
        """This operation returns determines if a COPC provider is valid for a member enrollment, based on the
        enrollment ID and provider ID passed in the endpoint. A value of True indicates that the provider is valid for
        the member enrollment. A value of False indicates that the provider is not valid for the member enrollment.

        Parameters
        ----------
        enroll_id: str, required
            Primary key of the enrollment table
        prov_id: str, required
            Primary key of the provider table
        as_of_date: [date, datetime, str], optional
            QNXT DOCUMENTATION UNAVAILABLE
        diag_codes: optional
            QNXT DOCUMENTATION UNAVAILABLE
        code_id: str, optional
            QNXT DOCUMENTATION UNAVAILABLE
        icd_version: str, optional
            QNXT DOCUMENTATION UNAVAILABLE

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"enrollments/{enroll_id}/copcProviders/{prov_id}/validate"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'asOfDate': dateutil.dateformat(as_of_date),
                  'diagCodes': diag_codes,
                  'codeId': code_id,
                  'icdVersion': icd_version
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class EnrollmentAccumulators:
    """Enrollment accumulations track the total, used, and remaining balances for individual and family benefits,
    deductibles, and maximum out-of-pocket amounts for a member. The Enrollment Accumulations resource includes stored
    values for accumulations, including amounts and effective dates."""

    BASE_PATH = r"QNXTApi/Member"

    def __init__(self, app_server: str, header_factory: RequestHeader):
        """
        Parameters
        ----------
        app_server: str, optional
            This is the FQDN of the target QNXT app server
        header_factory: qnxt.authentication.RequestHeader, required
            This is a callable that generates the appropriate authentication headers for QNXT API requests
        """
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}"
        self.header_factory = header_factory

    def get_static_plan_accruals(self, enroll_id: str, expand: str = None) -> Response:
        endpoint = f"accumulations/{enroll_id}/staticPlanAccruals"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def get_static_benefit_accruals(self,
                                    enroll_id: str,
                                    accum_id: str,
                                    accum_type: str,
                                    entity_state: str = None
                                    ) -> Response:
        """This operation retrieves individual and family benefit accruals, based on the enrollment ID, accummulator
        ID, and accummulator type passed in the endpoint.

        Parameters
        ----------
        enroll_id: str, required
            StaticBeneIndAccrual.EnrollId
            The unique system generated identifier for the member’s enrollment. This is the primary key for the table
            StaticBeneIndAccrual table.
        accum_id: str, required
            StaticBeneIndAccrual.AccumId
            The unique system generated identifier for an accumulator. This is part of primary key for
            StaticBeneIndAccrual table.
        accum_type: str, required
            StaticBeneIndAccrual.AccumType
            Type of the accumulatorleftparenANNUAL, DEDUCTIBLE, LIFETIME, LIFEUNITS, MAXOUT, VISITSrightparen. This is
            part of primary key for StaticBeneIndAccrual table.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"accumulations/{enroll_id}/staticBenefitAccruals/{accum_id}/{accum_type}"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'entityState': entity_state}
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class EnrollmentPlanAccumulations:
    def __init__(self):
        pass
        # TODO
