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
from cyperf.models.consumer import Consumer
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "DiskUsage" != "APILink":
    from cyperf.models.api_link import APILink

class DiskUsage(BaseModel):
    """
    DiskUsage
    """ # noqa: E501
    available: Optional[StrictInt] = Field(default=None, description="The currently available disk space (in bytes)")
    consumers: Optional[List[Consumer]] = Field(default=None, description="A list of consumers for handling logs and diagnostics storage")
    critical_disk_space: Optional[StrictBool] = Field(default=None, description="A flag indicating whether disk space is critical i.e the application may become unstable", alias="criticalDiskSpace")
    low_disk_space: Optional[StrictBool] = Field(default=None, description="A flag indicating whether disk space is low", alias="lowDiskSpace")
    message: Optional[StrictStr] = Field(default=None, description="A user-friendly message about disk usage")
    pretty_available: Optional[StrictStr] = Field(default=None, description="The currently available disk space in human-readable format", alias="prettyAvailable")
    pretty_size: Optional[StrictStr] = Field(default=None, description="The total disk size in human-readable format", alias="prettySize")
    size: Optional[StrictInt] = Field(default=None, description="The total disk size (in bytes)")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["available", "consumers", "criticalDiskSpace", "lowDiskSpace", "message", "prettyAvailable", "prettySize", "size"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_available(self):
#        if self.available is not None:
#            return self.available
#        field_info = self.__class__.__fields__["available"]
#        try:
#            self.available =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.available =  self.link_based_request("available", "GET", return_type="int")
#        return self.available
#
#    @rest_available.setter
#    def rest_available(self, value):
#        self.available = value

#    @property
#    def rest_consumers(self):
#        if self.consumers is not None:
#            return self.consumers
#        field_info = self.__class__.__fields__["consumers"]
#        try:
#            self.consumers =  self.link_based_request(field_info.alias, "GET", return_type="List[Consumer]")
#        except LinkNameException as e:
#            self.consumers =  self.link_based_request("consumers", "GET", return_type="List[Consumer]")
#        return self.consumers
#
#    @rest_consumers.setter
#    def rest_consumers(self, value):
#        self.consumers = value

#    @property
#    def rest_critical_disk_space(self):
#        if self.critical_disk_space is not None:
#            return self.critical_disk_space
#        field_info = self.__class__.__fields__["critical_disk_space"]
#        try:
#            self.critical_disk_space =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.critical_disk_space =  self.link_based_request("critical_disk_space", "GET", return_type="bool")
#        return self.critical_disk_space
#
#    @rest_critical_disk_space.setter
#    def rest_critical_disk_space(self, value):
#        self.critical_disk_space = value

#    @property
#    def rest_low_disk_space(self):
#        if self.low_disk_space is not None:
#            return self.low_disk_space
#        field_info = self.__class__.__fields__["low_disk_space"]
#        try:
#            self.low_disk_space =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.low_disk_space =  self.link_based_request("low_disk_space", "GET", return_type="bool")
#        return self.low_disk_space
#
#    @rest_low_disk_space.setter
#    def rest_low_disk_space(self, value):
#        self.low_disk_space = value

#    @property
#    def rest_message(self):
#        if self.message is not None:
#            return self.message
#        field_info = self.__class__.__fields__["message"]
#        try:
#            self.message =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.message =  self.link_based_request("message", "GET", return_type="str")
#        return self.message
#
#    @rest_message.setter
#    def rest_message(self, value):
#        self.message = value

#    @property
#    def rest_pretty_available(self):
#        if self.pretty_available is not None:
#            return self.pretty_available
#        field_info = self.__class__.__fields__["pretty_available"]
#        try:
#            self.pretty_available =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.pretty_available =  self.link_based_request("pretty_available", "GET", return_type="str")
#        return self.pretty_available
#
#    @rest_pretty_available.setter
#    def rest_pretty_available(self, value):
#        self.pretty_available = value

#    @property
#    def rest_pretty_size(self):
#        if self.pretty_size is not None:
#            return self.pretty_size
#        field_info = self.__class__.__fields__["pretty_size"]
#        try:
#            self.pretty_size =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.pretty_size =  self.link_based_request("pretty_size", "GET", return_type="str")
#        return self.pretty_size
#
#    @rest_pretty_size.setter
#    def rest_pretty_size(self, value):
#        self.pretty_size = value

#    @property
#    def rest_size(self):
#        if self.size is not None:
#            return self.size
#        field_info = self.__class__.__fields__["size"]
#        try:
#            self.size =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.size =  self.link_based_request("size", "GET", return_type="int")
#        return self.size
#
#    @rest_size.setter
#    def rest_size(self, value):
#        self.size = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DiskUsage from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "available",
            "critical_disk_space",
            "low_disk_space",
            "message",
            "pretty_available",
            "pretty_size",
            "size",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in consumers (list)
        _items = []
        if self.consumers:
            for _item in self.consumers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['consumers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DiskUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "available": obj.get("available"),
                        "consumers": [Consumer.from_dict(_item) for _item in obj["consumers"]] if obj.get("consumers") is not None else None,
                        "criticalDiskSpace": obj.get("criticalDiskSpace"),
                        "lowDiskSpace": obj.get("lowDiskSpace"),
                        "message": obj.get("message"),
                        "prettyAvailable": obj.get("prettyAvailable"),
                        "prettySize": obj.get("prettySize"),
                        "size": obj.get("size")
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
    


