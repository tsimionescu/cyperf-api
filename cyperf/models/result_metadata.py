# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.api_link import APILink
from cyperf.models.marked_as_deleted import MarkedAsDeleted
from cyperf.models.result_file_metadata import ResultFileMetadata
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "ResultMetadata" != "APILink":
    from cyperf.models.api_link import APILink

class ResultMetadata(BaseModel):
    """
    ResultMetadata
    """ # noqa: E501
    active_session: Optional[StrictStr] = Field(default=None, description="The id of the session where the result is currently loaded", alias="activeSession")
    config_url: Optional[StrictStr] = Field(default=None, description="The URL of the result's configuration", alias="configUrl")
    csv_url: Optional[StrictStr] = Field(default=None, description="The URL of the cached csv archive", alias="csvURL")
    display_name: Optional[StrictStr] = Field(default=None, description="The user-visible name of the result", alias="displayName")
    download_all: Optional[Any] = Field(default=None, description="Download all available test result types", alias="download-all")
    download_diagnostic: Optional[Any] = Field(default=None, description="The available test diagnostic result", alias="download-diagnostic")
    end_time: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the test ended", alias="endTime")
    files: Optional[List[ResultFileMetadata]] = Field(default=None, description="The list of result files")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the result")
    last_modified: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the result was last modified", alias="lastModified")
    marked_as_deleted: Optional[MarkedAsDeleted] = Field(default=None, alias="markedAsDeleted")
    owner: Optional[StrictStr] = Field(default=None, description="The user-visible name of the user who owns the result")
    owner_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the user who owns the result", alias="ownerId")
    pdf_url: Optional[StrictStr] = Field(default=None, description="The URL of the cached pdf report", alias="pdfURL")
    pinned: Optional[StrictBool] = Field(default=None, description="A flag that indicates if the result's configuration is pinned")
    reporting_links: Optional[List[APILink]] = Field(default=None, description="A list of links to result reporting resources", alias="reportingLinks")
    result_url: Optional[StrictStr] = Field(default=None, description="The URL of the result", alias="resultUrl")
    start_time: Optional[StrictInt] = Field(default=None, description="A Unix timestamp that indicates when the test was started", alias="startTime")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="A series of tags that describe the result")
    test_name: Optional[StrictStr] = Field(default=None, description="The name of the test associated with the result", alias="testName")
    type: Optional[StrictStr] = Field(default=None, description="The application type of the result")
    user_tags: Optional[List[StrictStr]] = Field(default=None, description="The list of user defined tags", alias="userTags")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["activeSession", "configUrl", "csvURL", "displayName", "download-all", "download-diagnostic", "endTime", "files", "id", "lastModified", "markedAsDeleted", "owner", "ownerId", "pdfURL", "pinned", "reportingLinks", "resultUrl", "startTime", "tags", "testName", "type", "userTags"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_active_session(self):
#        if self.active_session is not None:
#            return self.active_session
#        field_info = self.__class__.__fields__["active_session"]
#        try:
#            self.active_session =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.active_session =  self.link_based_request("active_session", "GET", return_type="str")
#        return self.active_session
#
#    @rest_active_session.setter
#    def rest_active_session(self, value):
#        self.active_session = value

#    @property
#    def rest_config_url(self):
#        if self.config_url is not None:
#            return self.config_url
#        field_info = self.__class__.__fields__["config_url"]
#        try:
#            self.config_url =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.config_url =  self.link_based_request("config_url", "GET", return_type="str")
#        return self.config_url
#
#    @rest_config_url.setter
#    def rest_config_url(self, value):
#        self.config_url = value

#    @property
#    def rest_csv_url(self):
#        if self.csv_url is not None:
#            return self.csv_url
#        field_info = self.__class__.__fields__["csv_url"]
#        try:
#            self.csv_url =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.csv_url =  self.link_based_request("csv_url", "GET", return_type="str")
#        return self.csv_url
#
#    @rest_csv_url.setter
#    def rest_csv_url(self, value):
#        self.csv_url = value

#    @property
#    def rest_display_name(self):
#        if self.display_name is not None:
#            return self.display_name
#        field_info = self.__class__.__fields__["display_name"]
#        try:
#            self.display_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.display_name =  self.link_based_request("display_name", "GET", return_type="str")
#        return self.display_name
#
#    @rest_display_name.setter
#    def rest_display_name(self, value):
#        self.display_name = value

#    @property
#    def rest_download_all(self):
#        if self.download_all is not None:
#            return self.download_all
#        field_info = self.__class__.__fields__["download_all"]
#        try:
#            self.download_all =  self.link_based_request(field_info.alias, "GET", return_type="object")
#        except LinkNameException as e:
#            self.download_all =  self.link_based_request("download_all", "GET", return_type="object")
#        return self.download_all
#
#    @rest_download_all.setter
#    def rest_download_all(self, value):
#        self.download_all = value

#    @property
#    def rest_download_diagnostic(self):
#        if self.download_diagnostic is not None:
#            return self.download_diagnostic
#        field_info = self.__class__.__fields__["download_diagnostic"]
#        try:
#            self.download_diagnostic =  self.link_based_request(field_info.alias, "GET", return_type="object")
#        except LinkNameException as e:
#            self.download_diagnostic =  self.link_based_request("download_diagnostic", "GET", return_type="object")
#        return self.download_diagnostic
#
#    @rest_download_diagnostic.setter
#    def rest_download_diagnostic(self, value):
#        self.download_diagnostic = value

#    @property
#    def rest_end_time(self):
#        if self.end_time is not None:
#            return self.end_time
#        field_info = self.__class__.__fields__["end_time"]
#        try:
#            self.end_time =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.end_time =  self.link_based_request("end_time", "GET", return_type="int")
#        return self.end_time
#
#    @rest_end_time.setter
#    def rest_end_time(self, value):
#        self.end_time = value

#    @property
#    def rest_files(self):
#        if self.files is not None:
#            return self.files
#        field_info = self.__class__.__fields__["files"]
#        try:
#            self.files =  self.link_based_request(field_info.alias, "GET", return_type="List[ResultFileMetadata]")
#        except LinkNameException as e:
#            self.files =  self.link_based_request("files", "GET", return_type="List[ResultFileMetadata]")
#        return self.files
#
#    @rest_files.setter
#    def rest_files(self, value):
#        self.files = value

#    @property
#    def rest_id(self):
#        if self.id is not None:
#            return self.id
#        field_info = self.__class__.__fields__["id"]
#        try:
#            self.id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.id =  self.link_based_request("id", "GET", return_type="str")
#        return self.id
#
#    @rest_id.setter
#    def rest_id(self, value):
#        self.id = value

#    @property
#    def rest_last_modified(self):
#        if self.last_modified is not None:
#            return self.last_modified
#        field_info = self.__class__.__fields__["last_modified"]
#        try:
#            self.last_modified =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.last_modified =  self.link_based_request("last_modified", "GET", return_type="int")
#        return self.last_modified
#
#    @rest_last_modified.setter
#    def rest_last_modified(self, value):
#        self.last_modified = value

#    @property
#    def rest_marked_as_deleted(self):
#        if self.marked_as_deleted is not None:
#            return self.marked_as_deleted
#        field_info = self.__class__.__fields__["marked_as_deleted"]
#        try:
#            self.marked_as_deleted =  self.link_based_request(field_info.alias, "GET", return_type="MarkedAsDeleted")
#        except LinkNameException as e:
#            self.marked_as_deleted =  self.link_based_request("marked_as_deleted", "GET", return_type="MarkedAsDeleted")
#        return self.marked_as_deleted
#
#    @rest_marked_as_deleted.setter
#    def rest_marked_as_deleted(self, value):
#        self.marked_as_deleted = value

#    @property
#    def rest_owner(self):
#        if self.owner is not None:
#            return self.owner
#        field_info = self.__class__.__fields__["owner"]
#        try:
#            self.owner =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.owner =  self.link_based_request("owner", "GET", return_type="str")
#        return self.owner
#
#    @rest_owner.setter
#    def rest_owner(self, value):
#        self.owner = value

#    @property
#    def rest_owner_id(self):
#        if self.owner_id is not None:
#            return self.owner_id
#        field_info = self.__class__.__fields__["owner_id"]
#        try:
#            self.owner_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.owner_id =  self.link_based_request("owner_id", "GET", return_type="str")
#        return self.owner_id
#
#    @rest_owner_id.setter
#    def rest_owner_id(self, value):
#        self.owner_id = value

#    @property
#    def rest_pdf_url(self):
#        if self.pdf_url is not None:
#            return self.pdf_url
#        field_info = self.__class__.__fields__["pdf_url"]
#        try:
#            self.pdf_url =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.pdf_url =  self.link_based_request("pdf_url", "GET", return_type="str")
#        return self.pdf_url
#
#    @rest_pdf_url.setter
#    def rest_pdf_url(self, value):
#        self.pdf_url = value

#    @property
#    def rest_pinned(self):
#        if self.pinned is not None:
#            return self.pinned
#        field_info = self.__class__.__fields__["pinned"]
#        try:
#            self.pinned =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.pinned =  self.link_based_request("pinned", "GET", return_type="bool")
#        return self.pinned
#
#    @rest_pinned.setter
#    def rest_pinned(self, value):
#        self.pinned = value

#    @property
#    def rest_reporting_links(self):
#        if self.reporting_links is not None:
#            return self.reporting_links
#        field_info = self.__class__.__fields__["reporting_links"]
#        try:
#            self.reporting_links =  self.link_based_request(field_info.alias, "GET", return_type="List[APILink]")
#        except LinkNameException as e:
#            self.reporting_links =  self.link_based_request("reporting_links", "GET", return_type="List[APILink]")
#        return self.reporting_links
#
#    @rest_reporting_links.setter
#    def rest_reporting_links(self, value):
#        self.reporting_links = value

#    @property
#    def rest_result_url(self):
#        if self.result_url is not None:
#            return self.result_url
#        field_info = self.__class__.__fields__["result_url"]
#        try:
#            self.result_url =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.result_url =  self.link_based_request("result_url", "GET", return_type="str")
#        return self.result_url
#
#    @rest_result_url.setter
#    def rest_result_url(self, value):
#        self.result_url = value

#    @property
#    def rest_start_time(self):
#        if self.start_time is not None:
#            return self.start_time
#        field_info = self.__class__.__fields__["start_time"]
#        try:
#            self.start_time =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.start_time =  self.link_based_request("start_time", "GET", return_type="int")
#        return self.start_time
#
#    @rest_start_time.setter
#    def rest_start_time(self, value):
#        self.start_time = value

#    @property
#    def rest_tags(self):
#        if self.tags is not None:
#            return self.tags
#        field_info = self.__class__.__fields__["tags"]
#        try:
#            self.tags =  self.link_based_request(field_info.alias, "GET", return_type="Dict[str, str]")
#        except LinkNameException as e:
#            self.tags =  self.link_based_request("tags", "GET", return_type="Dict[str, str]")
#        return self.tags
#
#    @rest_tags.setter
#    def rest_tags(self, value):
#        self.tags = value

#    @property
#    def rest_test_name(self):
#        if self.test_name is not None:
#            return self.test_name
#        field_info = self.__class__.__fields__["test_name"]
#        try:
#            self.test_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.test_name =  self.link_based_request("test_name", "GET", return_type="str")
#        return self.test_name
#
#    @rest_test_name.setter
#    def rest_test_name(self, value):
#        self.test_name = value

#    @property
#    def rest_type(self):
#        if self.type is not None:
#            return self.type
#        field_info = self.__class__.__fields__["type"]
#        try:
#            self.type =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.type =  self.link_based_request("type", "GET", return_type="str")
#        return self.type
#
#    @rest_type.setter
#    def rest_type(self, value):
#        self.type = value

#    @property
#    def rest_user_tags(self):
#        if self.user_tags is not None:
#            return self.user_tags
#        field_info = self.__class__.__fields__["user_tags"]
#        try:
#            self.user_tags =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.user_tags =  self.link_based_request("user_tags", "GET", return_type="List[str]")
#        return self.user_tags
#
#    @rest_user_tags.setter
#    def rest_user_tags(self, value):
#        self.user_tags = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResultMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "config_url",
            "id",
            "last_modified",
            "owner",
            "owner_id",
            "result_url",
            "start_time",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of marked_as_deleted
        if self.marked_as_deleted:
            _dict['markedAsDeleted'] = self.marked_as_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reporting_links (list)
        _items = []
        if self.reporting_links:
            for _item in self.reporting_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reportingLinks'] = _items
        # set to None if download_all (nullable) is None
        # and model_fields_set contains the field
        if self.download_all is None and "download_all" in self.model_fields_set:
            _dict['download-all'] = None

        # set to None if download_diagnostic (nullable) is None
        # and model_fields_set contains the field
        if self.download_diagnostic is None and "download_diagnostic" in self.model_fields_set:
            _dict['download-diagnostic'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResultMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "activeSession": obj.get("activeSession"),
                        "configUrl": obj.get("configUrl"),
                        "csvURL": obj.get("csvURL"),
                        "displayName": obj.get("displayName"),
                        "download-all": obj.get("download-all"),
                        "download-diagnostic": obj.get("download-diagnostic"),
                        "endTime": obj.get("endTime"),
                        "files": [ResultFileMetadata.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
                        "id": obj.get("id"),
                        "lastModified": obj.get("lastModified"),
                        "markedAsDeleted": MarkedAsDeleted.from_dict(obj["markedAsDeleted"]) if obj.get("markedAsDeleted") is not None else None,
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "pdfURL": obj.get("pdfURL"),
                        "pinned": obj.get("pinned"),
                        "reportingLinks": [APILink.from_dict(_item) for _item in obj["reportingLinks"]] if obj.get("reportingLinks") is not None else None,
                        "resultUrl": obj.get("resultUrl"),
                        "startTime": obj.get("startTime"),
                        "tags": obj.get("tags"),
                        "testName": obj.get("testName"),
                        "type": obj.get("type"),
                        "userTags": obj.get("userTags")
            ,
            "links": obj.get("links")
        })
#        _obj.api_client = client
        return _obj

#    def update(self):
#        self.link_request("self", "PUT", body=self)
#
#   def link_based_request(self, link_name, method, return_type = None, body = None):
#        if self.links == None:
#           raise Exception("You must allow links to be present to use automatic retrieval functions.")
#        if link_name == 'self':
#            self_links = [link for link in self.links if link.rel == link_name]
#        else:
#            self_links = [link for link in self.links if link.rel == "child" and link.name == link_name]
#        if len(self_links) == 0:
#           raise LinkNameException(f"Missing {link_name} link.")
#        self_link = self_links[0]
#        
#        _host = None
#
#        _collection_formats: Dict[str, str] = {
#        }#
#
#        _path_params: Dict[str, str] = {}
#        _query_params: List[Tuple[str, str]] = []
#        _header_params: Dict[str, Optional[str]] = {}
#        _form_params: List[Tuple[str, str]] = []
#        _files: Dict[str, Union[str, bytes]] = {}
#        _body_params: Optional[bytes] = None
#        if body:
#            _body_params = body.to_json().encode('utf-8')
#
#        # set the HTTP header `Accept`
#        if 'Accept' not in _header_params:
#            _header_params['Accept'] = self.api_client.select_header_accept(
#                [
#                    'application/json'
#                ]
#            )
#        if 'Content-Type' not in _header_params:
#            _header_params['Content-Type'] = self.api_client.select_header_content_type(
#                [
#                    'application/json'
#                ]
#            )
#        _auth_settings: List[str] = [
#            'OAuth2',
#        ]
#        _param = self.api_client.param_serialize(
#            method=method,
#           resource_path=self_link.href,
#            path_params=_path_params,
#           query_params=_query_params,
#           body=_body_params,
#            post_params=_form_params,
#            files=_files,
#            auth_settings=_auth_settings,
#            collection_formats=_collection_formats,
#            _host=_host
#        )
#        response_data = self.api_client.call_api(
#            *_param
#        )
#        response_data.read()
#        response_types = {
#            '200': return_type,
#            '500': 'ErrorResponse'
#        }
#        return self.api_client.response_deserialize(response_data, response_types).data
    


