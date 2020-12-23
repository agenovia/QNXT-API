import requests
from qnxt.authentication import RequestHeader
from typing import Union
from datetime import date, datetime
from qnxt.utils import *
from qnxt.api.Response import Response


class ApplicationLogs:
    """This operation returns application logs, based on the data passed in the request."""
    BASE_PATH = r"QNXTApi/PlanIntegration"

    def __init__(self, app_server, header_factory):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.app_server = app_server
        self.header_factory = header_factory

    def search(self,
               referenceid: str = None,
               utc_date_from: Union[date, datetime, str] = None,
               utc_date_to: Union[date, datetime, str] = None,
               source: str = None,
               loginid: str = None,
               machine_name: str = None,
               level: str = None,
               source_category: str = None,
               skip: int = 0,
               take: int = None,
               order_by: str = None,
               expand: str = None,
               ):
        """This operation returns application logs, based on the data passed in the request."""
        endpoint = r"applicationLogs/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'expand': expand,
                  'level': level,
                  'loginId': loginid,
                  'machineName': machine_name,
                  'orderBy': order_by,
                  'referenceId': referenceid,
                  'skip': skip,
                  'source': source,
                  'sourceCategory': source_category,
                  'take': take,
                  'utcDateFrom': dateutil.dateformat(utc_date_from),
                  'utcDateTo': dateutil.dateformat(utc_date_to)
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogs:
    """Provide a processLogDetailID and retrieve full details"""
    BASE_PATH = r'QNXTApi/PlanIntegration'

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = clean_url.clean_url(app_server, self.BASE_PATH)
        self.header_factory = header_factory

    def get_details(self, process_log_detailid: str):
        """This operation returns process log XML data, based on the process log detail ID passed in the endpoint."""
        endpoint = f"ProcessLogDetails/{process_log_detailid}/xmls"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processLogDetailId': process_log_detailid
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogDetails:
    BASE_PATH = r"QNXTApi/PlanIntegration"

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}"
        self.header_factory = header_factory

    def search(self,
               referenceid: str = None,
               processlogtype_id: str = None,
               skip: int = None,
               take: int = None,
               order_by: str = None,
               expand: str = None,
               ):
        """This operation returns process log data, based on the data passed in the request."""
        endpoint = r"ProcessLogDetails/search"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'referenceId': referenceid,
                  'processLogTypeId': processlogtype_id,
                  'skip': skip,
                  'take': take,
                  'orderBy': order_by,
                  'expand': expand
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def create_process_logdetail(self,
                                 processlog_id: str = None,
                                 xml_data: str = None,
                                 processlogtype_id: str = None,
                                 referenceid: str = None,
                                 externalid: str = None,
                                 message: str = None,
                                 amount: float = None,
                                 entity_state: str = None,
                                 ):
        """This operation creates a process log detail record, based on the data passed in the request."""
        endpoint = r"processLogDetails"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processLogId': processlog_id,
                  'xmlData': xml_data,
                  'processLogTypeId': processlogtype_id,
                  'referenceId': referenceid,
                  'externalId': externalid,
                  'message': message,
                  'amount': amount,
                  'entityState': entity_state
                  }
        response = requests.post(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def update_process_logdetail(self,
                                 processlogdetail_id: str,
                                 process_stage_id: str = None,
                                 xml_schema_id: str = None,
                                 stop_date: Union[date, datetime, str] = None,
                                 errorid: str = None,
                                 total_count: int = None,
                                 failure_count: int = None,
                                 processlog_id: str = None,
                                 xml_data: str = None,
                                 processlogtype_id: str = None,
                                 referenceid: str = None,
                                 externalid: str = None,
                                 message: str = None,
                                 amount: float = None,
                                 entity_state: str = None,
                                 ):
        """This operation updates a process log detail record, based on the process log detail ID passed in the
        endpoint."""
        endpoint = f"processLogDetails/{processlogdetail_id}"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processStageId': process_stage_id,
                  'xmlSchemaId': xml_schema_id,
                  'stopDate': dateutil.dateformat(stop_date),
                  'errorId': errorid,
                  'totalCount': total_count,
                  'failureCount': failure_count,
                  'processLogId': processlog_id,
                  'xmlData': xml_data,
                  'processLogTypeId': processlogtype_id,
                  'referenceId': referenceid,
                  'externalId': externalid,
                  'message': message,
                  'amount': amount,
                  'entityState': entity_state
                  }
        response = requests.put(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def create_process_state(self,
                             processlogdetail_id: str,
                             process_stage_id: str = None,
                             errorid: str = None,
                             start_date: Union[date, datetime, str] = None,
                             stop_date: Union[date, datetime, str] = None,
                             total_count: int = None,
                             failure_count: int = None,
                             amount: float = None,
                             message: str = None,
                             app_server_name: str = None,
                             primary_id: str = None,
                             status: str = None,
                             execution_time: int = None,
                             entity_state: str = None,
                             ):
        """This operation creates a process state record, based on the process log detail ID passed in the endpoint."""
        endpoint = f"processLogDetails/{processlogdetail_id}/states"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processStageId': process_stage_id,
                  'errorId': errorid,
                  'startDate': start_date,
                  'stopDate': stop_date,
                  'totalCount': total_count,
                  'failureCount': failure_count,
                  'amount': amount,
                  'message': message,
                  'appServer': app_server_name,
                  'primaryId': primary_id,
                  'status': status,
                  'executionTime': execution_time,
                  'entityState': entity_state,
                  }
        response = requests.post(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogHeaders:
    BASE_PATH = r"QNXTApi/PlanIntegration"

    def __init__(self, app_server: str, header_factory: RequestHeader):
        self.base_uri = f"{clean_url.clean_url(app_server, self.BASE_PATH)}"
        self.header_factory = header_factory

    def create_process_log_header(self,
                                  processlogtype_id: str,
                                  envid: int = None,
                                  batchid: str = None,
                                  batch_count: int = None,
                                  tradingpartner_id: str = None,
                                  external_id: str = None,
                                  message: str = None,
                                  amount: float = None,
                                  xml_schema_id: str = None,
                                  xml_data: str = None,
                                  entity_state: str = None,
                                  ):
        """This operation creates a process log header record, based on the data passed in the request."""
        endpoint = r"processLogs"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processLogTypeId': processlogtype_id,
                  'envId': envid if envid is not None else self.header_factory.envid,
                  'batchId': batchid,
                  'batchCount': batch_count,
                  'tradingPartnerId': tradingpartner_id,
                  'externalId': external_id,
                  'message': message,
                  'amount': amount,
                  'xmlSchemaId': xml_schema_id,
                  'xmlData': xml_data,
                  'entityState': entity_state,
                  }
        response = requests.post(uri, headers=self.header_factory(), params=params)
        return Response(response)

    def update_process_log_header(self,
                                  processlog_id: str,
                                  processlogtype_id: str,
                                  envid: int,
                                  failure_count: int = None,
                                  error_id: str = None,
                                  process_stage_id: str = None,
                                  stop_date: Union[date, datetime, str] = None,
                                  batchid: str = None,
                                  batch_count: int = None,
                                  trading_partner_id: str = None,
                                  external_id: str = None,
                                  message: str = None,
                                  amount: float = None,
                                  xml_schema_id: str = None,
                                  xml_data: str = None,
                                  entity_state: str = None,
                                  ):
        """This operation updates a process log header record, based on the process log ID passed in the endpoint."""
        endpoint = f"processLogs/{processlog_id}"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'failureCount': failure_count,
                  'errorId': error_id,
                  'processStageId': process_stage_id,
                  'stopDate': dateutil.dateformat(stop_date),
                  'processLogTypeId': processlogtype_id,
                  'envId': envid if envid is not None else self.header_factory.envid,
                  'batchId': batchid,
                  'batchCount': batch_count,
                  'tradingPartnerId': trading_partner_id,
                  'externalId': external_id,
                  'message': message,
                  'amount': amount,
                  'xmlSchemaId': xml_schema_id,
                  'xmlData': xml_data,
                  'entityState': entity_state,
                  }
        response = requests.put(uri, headers=self.header_factory(), params=params)
        return Response(response)
