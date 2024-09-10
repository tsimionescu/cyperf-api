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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "NetworkMapping" != "APILink":
    from cyperf.models.api_link import APILink

class NetworkMapping(BaseModel):
    """
    NetworkMapping
    """ # noqa: E501
    client_network_tags: List[StrictStr] = Field(description="A list of tags of Network Segments which serve as clients. (default: Client)", alias="ClientNetworkTags")
    excluded_dut_list: Optional[List[StrictStr]] = Field(default=None, description="A list of DUTs that are excluded from client-server network connections.", alias="ExcludedDUTList")
    server_network_tags: List[StrictStr] = Field(description="A list of tags of Network Segments which serve as servers. (default: Server)", alias="ServerNetworkTags")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["ClientNetworkTags", "ExcludedDUTList", "ServerNetworkTags"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_client_network_tags(self):
#        if self.client_network_tags is not None:
#            return self.client_network_tags
#        field_info = self.__class__.__fields__["client_network_tags"]
#        try:
#            self.client_network_tags =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.client_network_tags =  self.link_based_request("client_network_tags", "GET", return_type="List[str]")
#        return self.client_network_tags
#
#    @rest_client_network_tags.setter
#    def rest_client_network_tags(self, value):
#        self.client_network_tags = value

#    @property
#    def rest_excluded_dut_list(self):
#        if self.excluded_dut_list is not None:
#            return self.excluded_dut_list
#        field_info = self.__class__.__fields__["excluded_dut_list"]
#        try:
#            self.excluded_dut_list =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.excluded_dut_list =  self.link_based_request("excluded_dut_list", "GET", return_type="List[str]")
#        return self.excluded_dut_list
#
#    @rest_excluded_dut_list.setter
#    def rest_excluded_dut_list(self, value):
#        self.excluded_dut_list = value

#    @property
#    def rest_server_network_tags(self):
#        if self.server_network_tags is not None:
#            return self.server_network_tags
#        field_info = self.__class__.__fields__["server_network_tags"]
#        try:
#            self.server_network_tags =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.server_network_tags =  self.link_based_request("server_network_tags", "GET", return_type="List[str]")
#        return self.server_network_tags
#
#    @rest_server_network_tags.setter
#    def rest_server_network_tags(self, value):
#        self.server_network_tags = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NetworkMapping from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "ClientNetworkTags": obj.get("ClientNetworkTags"),
                        "ExcludedDUTList": obj.get("ExcludedDUTList"),
                        "ServerNetworkTags": obj.get("ServerNetworkTags")
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
    


