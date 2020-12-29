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
        """
        Parameters
        ----------
        app_server: str, optional
            This is the FQDN of the target QNXT app server
        header_factory: qnxt.authentication.RequestHeader, required
            This is a callable that generates the appropriate authentication headers for QNXT API requests
        """
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
        """
        This operation returns application logs, based on the data passed in the request.

        Parameters
        ----------
        referenceid: str, optional
            The unique identifier for the error generated in QNXT. The reference ID is available from the common error
            page.
        utc_date_from: [date, datetime, str], optional
            applicationLog.TimeStamp,
            Identifies the date and time of the QNXT error, based on the server time/location where the error occurred.
            The timestamp uses the Coordinated Universal Time (UTC) offset format.
        utc_date_to: [date, datetime, str], optional
            applicationLog.TimeStamp,
            Identifies the date and time of the QNXT error, based on the server time/location where the error occurred.
            The timestamp uses the Coordinated Universal Time (UTC) offset format.
        source: str, optional
            applicationLog.Source,
            The specific area of the application that generated the log entry. This is often the namespace qualified
            class name.
        loginid: str, optional
            applicationLog.UserName,
            The name of the user associated with the log entry.
        machine_name: str, optional
            applicationLog.MachineName,
            The machine name of the client application computer where the web request originated.
        level: str, optional
            applicationLog.Level,
            Indicates the level of the event (for example, Verbose, Debug, Information, Warning, Error, Fatal, etc.).
        source_category: str, optional
            applicationLog.SourceCategory
            The Log source category of message. The valid values for the Source Category are WebUiApplication,
            ApplicationBase, MyQnxt
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

    def get_details(self, process_log_detailid: str):
        """
        This operation returns process log XML data, based on the process log detail ID passed in the endpoint.

        Parameters
        ----------
        process_log_detailid: str, required
            Identifier of the ProcessLogDetailId.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
        endpoint = f"ProcessLogDetails/{process_log_detailid}/xmls"
        uri = f"{self.base_uri}/{endpoint}"
        params = {'processLogDetailId': process_log_detailid
                  }
        response = requests.get(uri, headers=self.header_factory(), params=params)
        return Response(response)


class ProcessLogDetails:
    """QNXT process log detail records provide detailed information about QNXT and QNXT Connect processes. The Process
    Log Details resource stores process details including status, dates, counts, messages, error descriptions, states,
    and stages."""
    BASE_PATH = r"QNXTApi/PlanIntegration"

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

    def search(self,
               referenceid: str = None,
               processlogtype_id: str = None,
               skip: int = None,
               take: int = None,
               order_by: str = None,
               expand: str = None,
               ):
        """
        This operation returns process log data, based on the data passed in the request.

        Parameters
        ----------
        referenceid: str, optional
            processlogdetail.referenceid
            The identifier for the object created, if successful. The object created will vary according to the
            transaction type (e.g., claims identifier, enrollment identifier, etc.).
        processlogtype_id: str, optional
            processlogdetail.processlogtypeid
            The identifier for the process log type record linked to this detail record. This is a foreign key to the
            processlogtype table.
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
        """
        This operation creates a process log detail record, based on the data passed in the request.

        Parameters
        ----------
        processlog_id: str, optional
            processlogdetail.processlogid
            The identifier for the header record linked to this detail record. This is a foreign key to the
            processlogheader table.
        xml_data: str, optional
            processlogdetail.xmldata
            The transaction data stored in an xml format.
        processlogtype_id: str, optional
            processlogdetail.processlogtypeid
            The identifier for the process log type record linked to this header record. This is a foreign key to the
            processlogtype table.
        referenceid: str, optional
            processlogdetail.referenceid
            The identifier for the object created, if successful. The object created will vary according to the
            transaction type (e.g., claims identifier, enrollment identifier, etc.).
        externalid: str, optional
            processlogdetail.externalid
            The process log detail ID used by external applications (e.g., BizTalk Server).
        message: str, optional
            processlogdetail.customerrmsg
            The message that provides the status of the transaction (e.g., claim stored successfully). The message can
            also provide the assigned identifier for objects created during processing (e.g., member ID, enrollment ID,
            etc.).
        amount: float, optional
            processlogdetail.amount
            The value for the user-defined amount field.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
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
        """
        This operation updates a process log detail record, based on the process log detail ID passed in the endpoint.

        Parameters
        ----------
        processlogdetail_id: str, required
            processlogDetail.processlogdetailid
            The identifier for the detail record.
        process_stage_id: str, optional
            processlogdetail.processstageid
            The identifier for the process stage record linked to this detail record. This indicates the final outcome
            of the transaction. Typically, this is COMPLETED or ERROR. This is a foreign key to the processstage table.
        xml_schema_id: str, optional
            processlogdetail.xmlschemaid
            The transaction data stored in an xml format.
        stop_date: [date, datetime, str], optional
            processlogdetail.stopdate
            The date/time that transaction processing ended.
        errorid: str, optional
            processlogdetail.errorid
            The identifier for the error code linked to this detail record. This is a foreign key to the errorcode
            table.
        total_count: int, optional
            processlogdetail.totalcount
            The total number of transactions that were processed.
        failure_count: int, optional
            processlogdetail.failurecount
            The number of detail records that produced warning or error messages. This value is set to zero (0) if
            there are no warning or error messages. This value is set to 1 if a warning or error was generated.
        processlog_id: str, optional
            processlogdetail.processlogid
            The identifier for the header record linked to this detail record. This is a foreign key to the
            processlogheader table.
        xml_data: str, optional
            processlogdetail.xmldata
            The transaction data stored in an xml format.
        processlogtype_id: str, optional
            processlogdetail.processlogtypeid
            The identifier for the process log type record linked to this header record. This is a foreign key to the
            processlogtype table.
        referenceid: str, optional
            processlogdetail.referenceid
            The identifier for the object created, if successful. The object created will vary according to the
            transaction type (e.g., claims identifier, enrollment identifier, etc.).
        externalid: str, optional
            processlogdetail.externalid
            The process log detail ID used by external applications (e.g., BizTalk Server).
        message: str, optional
            processlogdetail.customerrmsg
            The message that provides the status of the transaction (e.g., claim stored successfully). The message can
            also provide the assigned identifier for objects created during processing (e.g., member ID, enrollment ID,
            etc.).
        amount: float, optional
            processlogdetail.amount
            The value for the user-defined amount field.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
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
        """
        This operation creates a process state record, based on the process log detail ID passed in the endpoint.

        Parameters
        ----------
        processlogdetail_id: str, required
            processlogDetail.processlogdetailid
            The identifier for the detail record.
        process_stage_id: str, optional
            processlogdetail.processstageid
            The identifier for the process stage record linked to this detail record. This indicates the final outcome
            of the transaction. Typically, this is COMPLETED or ERROR. This is a foreign key to the processstage table.
        errorid: str, optional
            processlogdetail.errorid
            The identifier for the error code linked to this detail record. This is a foreign key to the errorcode
            table.
        start_date: [date, datetime, str], optional
            processstate.startdate
            The date and time that the transaction began in this state.
        stop_date: [date, datetime, str], optional
            processlogdetail.stopdate
            The date/time that transaction processing ended.
        total_count: int, optional
            processlogdetail.totalcount
            The total number of transactions that were processed.
        failure_count: int, optional
            processstate.failurecount
            The number of detail state records that produced warning or error messages. This value is set to zero (0)
            if there are no warning or error messages. This value is set to 1 if a warning or error was generated.
        amount: float, optional
            processlogdetail.amount
            The value for the user-defined amount field.
        message: str, optional
            processstate.customerrmsg
            The custom message that displays additional information about the processing state (e.g., member found,
            lookup provider, etc.).
        app_server_name: str, optional
            processstate.appserver
            The name of the server where the error occurred. This value is not captured for every process.
        primary_id: str, optional
            processstate.primaryid
            The primary identifier for the process. For example, if the process is Mass Adjudication, then the claim
            ID would be stored in this field. This value is not captured for every process.
        status: str, optional
            processstate.status
            The status of the process. For example, if the process is Mass Adjudication, then the status of the claim
            would be stored in this field. This value is not captured for every process.
        execution_time: int, optional
            processstate.executiontime
            The amount of time (in milliseconds) that the process took to execute.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
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
    """QNXT process log header records provide high level information about QNXT and QNXT Connect processes. The
    Process Log Headers resource stores high level process data including process IDs, process types, dates, warnings,
    and errors, for multiple processes."""
    BASE_PATH = r"QNXTApi/PlanIntegration"

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
        """
        This operation creates a process log header record, based on the data passed in the request.

        Parameters
        ----------
        processlogtype_id: str, required
            processlogheader.processlogtypeid
            The identifier for the process log type record linked to this header record. This is a foreign key to the
            processlogtype table.
        envid: int, optional, default is the same envid provided to the request header
            processlogheader.environmentid
            The identifier for the QNXT environment that the transactions were processed against. This data is provided
            by the qenvironment table.
        batchid: str, optional
            processlogheader.batchid
            The identifier for the batch that was processed.
        batch_count: int, optional
            processlogheader.batchcount
            The number of transactions that are contained in the process log header record. Because BizTalk can be
            configured to separate multi-transaction files into individual transactions, this number will frequently
            be something other than one.
        tradingpartner_id: str, optional
            processlogheader.tradingpartnerid
            The identifier for the trading partner configured in EDI Manager.
        external_id: str, optional
            processlogheader.externalid
            The process log header ID for external applications (e.g., BizTalk Server).
        message: str, optional
            processstate.customerrmsg
            The custom message that displays additional information about the processing state (e.g., member found,
            lookup provider, etc.).
        amount: float, optional
            processlogdetail.amount
            The value for the user-defined amount field.
        xml_schema_id: str, optional
            processlogheader.xmlschemaid
            The user-defined identifier for the xmldata field.
        xml_data: str, optional
            processlogheader.xmldata
            The transaction data stored in an xml format.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
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
                                  envid: int = None,
                                  failure_count: int = None,
                                  error_id: str = None,
                                  process_stage_id: str = None,
                                  stop_date: Union[date, datetime, str] = None,
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
        """
        This operation updates a process log header record, based on the process log ID passed in the endpoint.

        Parameters
        ----------
        processlog_id: str, required
            processlogheader.processlogid The identifier that represents the transaction at the file level.
            There will be one process log header ID for each fileforwardslashtransaction processed.
        processlogtype_id: str, required
            processlogheader.processlogtypeid
            The identifier for the process log type record linked to this header record. This is a foreign key to the
            processlogtype table.
        envid: int, optional, default is the same envid provided to the request header
            processlogheader.environmentid
            The identifier for the QNXT environment that the transactions were processed against. This data is
            provided by the qenvironment table.
        failure_count: int, optional
            processlogheader.failurecount
            The number of header records that produced warning or error messages. This value is set to zero (0) if
            there are no warning or error messages. This value is set to 1 if a warning or error was generated.
        error_id: str, optional
            processlogheader.errorid
            The identifier for the error code linked to this detail record. This is a foreign key to the errorcode
            table.
        process_stage_id: str, optional
            processlogheader.processstageid
            The identifier for the process stage record linked to this header record. Note: In some instances the
            header status is not updated (and will remain in STARTED state) despite the fact that transaction
            processing completed.
        stop_date: [date, datetime, str], optional
            processlogheader.stopdate
            The date/time that transaction processing ended.
        batchid: str, optional
            processlogheader.batchid
            The identifier for the batch that was processed.
        batch_count: int, optional
            processlogheader.batchcount
            The number of transactions that are contained in the process log header record. Because BizTalk can be
            configured to separate multi-transaction files into individual transactions, this number will frequently
            be something other than one.
        tradingpartner_id: str, optional
            processlogheader.tradingpartnerid
            The identifier for the trading partner configured in EDI Manager.
        external_id: str, optional
            processlogheader.externalid
            The process log header ID for external applications (e.g., BizTalk Server).
        message: str, optional
            processstate.customerrmsg
            The custom message that displays additional information about the processing state (e.g., member found,
            lookup provider, etc.).
        amount: float, optional
            processlogdetail.amount
            The value for the user-defined amount field.
        xml_schema_id: str, optional
            processlogheader.xmlschemaid
            The user-defined identifier for the xmldata field.
        xml_data: str, optional
            processlogheader.xmldata
            The transaction data stored in an xml format.
        entity_state: str, optional
            The state of the model object. Valid values include ByDefault, NewlyAdded, Modified, and Deleted.

        Returns
        -------
        response: qnxt.api.Response.Response
            HTTP Response object with convenience methods for getting the response's overview, metadata and results in
            the form of class properties
        """
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
                  'tradingPartnerId': tradingpartner_id,
                  'externalId': external_id,
                  'message': message,
                  'amount': amount,
                  'xmlSchemaId': xml_schema_id,
                  'xmlData': xml_data,
                  'entityState': entity_state,
                  }
        response = requests.put(uri, headers=self.header_factory(), params=params)
        return Response(response)
