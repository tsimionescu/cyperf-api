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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cyperf.models.inner_ip_range import InnerIPRange
from cyperf.models.ip_range import IPRange
from cyperf.models.tunnel_range import TunnelRange
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "TunnelStack" != "APILink":
    from cyperf.models.api_link import APILink

class TunnelStack(BaseModel):
    """
    The tunnel stack assigned to the current test configuration
    """ # noqa: E501
    inner_ip_range: Optional[InnerIPRange] = Field(default=None, alias="InnerIPRange")
    outer_ip_range: Optional[IPRange] = Field(default=None, alias="OuterIPRange")
    tunnel_range: Optional[TunnelRange] = Field(default=None, alias="TunnelRange")
    tunnel_stack_name: Annotated[str, Field(strict=True)] = Field(alias="TunnelStackName")
    id: StrictStr
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["InnerIPRange", "OuterIPRange", "TunnelRange", "TunnelStackName", "id"]

    @field_validator('tunnel_stack_name')
    def tunnel_stack_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^$|^[^\"\\]+$", value):
            raise ValueError(r"must validate the regular expression /^$|^[^\"\\]+$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_inner_ip_range(self):
#        if self.inner_ip_range is not None:
#            return self.inner_ip_range
#        field_info = self.__class__.__fields__["inner_ip_range"]
#        try:
#            self.inner_ip_range =  self.link_based_request(field_info.alias, "GET", return_type="InnerIPRange")
#        except LinkNameException as e:
#            self.inner_ip_range =  self.link_based_request("inner_ip_range", "GET", return_type="InnerIPRange")
#        return self.inner_ip_range
#
#    @rest_inner_ip_range.setter
#    def rest_inner_ip_range(self, value):
#        self.inner_ip_range = value

#    @property
#    def rest_outer_ip_range(self):
#        if self.outer_ip_range is not None:
#            return self.outer_ip_range
#        field_info = self.__class__.__fields__["outer_ip_range"]
#        try:
#            self.outer_ip_range =  self.link_based_request(field_info.alias, "GET", return_type="IPRange")
#        except LinkNameException as e:
#            self.outer_ip_range =  self.link_based_request("outer_ip_range", "GET", return_type="IPRange")
#        return self.outer_ip_range
#
#    @rest_outer_ip_range.setter
#    def rest_outer_ip_range(self, value):
#        self.outer_ip_range = value

#    @property
#    def rest_tunnel_range(self):
#        if self.tunnel_range is not None:
#            return self.tunnel_range
#        field_info = self.__class__.__fields__["tunnel_range"]
#        try:
#            self.tunnel_range =  self.link_based_request(field_info.alias, "GET", return_type="TunnelRange")
#        except LinkNameException as e:
#            self.tunnel_range =  self.link_based_request("tunnel_range", "GET", return_type="TunnelRange")
#        return self.tunnel_range
#
#    @rest_tunnel_range.setter
#    def rest_tunnel_range(self, value):
#        self.tunnel_range = value

#    @property
#    def rest_tunnel_stack_name(self):
#        if self.tunnel_stack_name is not None:
#            return self.tunnel_stack_name
#        field_info = self.__class__.__fields__["tunnel_stack_name"]
#        try:
#            self.tunnel_stack_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.tunnel_stack_name =  self.link_based_request("tunnel_stack_name", "GET", return_type="str")
#        return self.tunnel_stack_name
#
#    @rest_tunnel_stack_name.setter
#    def rest_tunnel_stack_name(self, value):
#        self.tunnel_stack_name = value

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



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TunnelStack from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of inner_ip_range
        if self.inner_ip_range:
            _dict['InnerIPRange'] = self.inner_ip_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outer_ip_range
        if self.outer_ip_range:
            _dict['OuterIPRange'] = self.outer_ip_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tunnel_range
        if self.tunnel_range:
            _dict['TunnelRange'] = self.tunnel_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TunnelStack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "InnerIPRange": InnerIPRange.from_dict(obj["InnerIPRange"]) if obj.get("InnerIPRange") is not None else None,
                        "OuterIPRange": IPRange.from_dict(obj["OuterIPRange"]) if obj.get("OuterIPRange") is not None else None,
                        "TunnelRange": TunnelRange.from_dict(obj["TunnelRange"]) if obj.get("TunnelRange") is not None else None,
                        "TunnelStackName": obj.get("TunnelStackName"),
                        "id": obj.get("id")
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
    


