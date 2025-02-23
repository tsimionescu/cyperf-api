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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.effective_ports import EffectivePorts
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "PortSettings" != "APILink":
    from cyperf.models.api_link import APILink

class PortSettings(BaseModel):
    """
    PortSettings
    """ # noqa: E501
    automatic: StrictBool = Field(alias="Automatic")
    automatic_destination_port: StrictBool = Field(alias="AutomaticDestinationPort")
    automatic_forward_proxy_port: StrictBool = Field(alias="AutomaticForwardProxyPort")
    destination_port: StrictInt = Field(alias="DestinationPort")
    effective_ports: Optional[EffectivePorts] = Field(default=None, alias="EffectivePorts")
    forward_proxy_port: StrictInt = Field(alias="ForwardProxyPort")
    readonly: Optional[StrictBool] = Field(default=None, description="If true, the port can't be selected by the user", alias="Readonly")
    server_listen_port: StrictInt = Field(alias="ServerListenPort")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["Automatic", "AutomaticDestinationPort", "AutomaticForwardProxyPort", "DestinationPort", "EffectivePorts", "ForwardProxyPort", "Readonly", "ServerListenPort"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_automatic(self):
#        if self.automatic is not None:
#            return self.automatic
#        field_info = self.__class__.__fields__["automatic"]
#        try:
#            self.automatic =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.automatic =  self.link_based_request("automatic", "GET", return_type="bool")
#        return self.automatic
#
#    @rest_automatic.setter
#    def rest_automatic(self, value):
#        self.automatic = value

#    @property
#    def rest_automatic_destination_port(self):
#        if self.automatic_destination_port is not None:
#            return self.automatic_destination_port
#        field_info = self.__class__.__fields__["automatic_destination_port"]
#        try:
#            self.automatic_destination_port =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.automatic_destination_port =  self.link_based_request("automatic_destination_port", "GET", return_type="bool")
#        return self.automatic_destination_port
#
#    @rest_automatic_destination_port.setter
#    def rest_automatic_destination_port(self, value):
#        self.automatic_destination_port = value

#    @property
#    def rest_automatic_forward_proxy_port(self):
#        if self.automatic_forward_proxy_port is not None:
#            return self.automatic_forward_proxy_port
#        field_info = self.__class__.__fields__["automatic_forward_proxy_port"]
#        try:
#            self.automatic_forward_proxy_port =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.automatic_forward_proxy_port =  self.link_based_request("automatic_forward_proxy_port", "GET", return_type="bool")
#        return self.automatic_forward_proxy_port
#
#    @rest_automatic_forward_proxy_port.setter
#    def rest_automatic_forward_proxy_port(self, value):
#        self.automatic_forward_proxy_port = value

#    @property
#    def rest_destination_port(self):
#        if self.destination_port is not None:
#            return self.destination_port
#        field_info = self.__class__.__fields__["destination_port"]
#        try:
#            self.destination_port =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.destination_port =  self.link_based_request("destination_port", "GET", return_type="int")
#        return self.destination_port
#
#    @rest_destination_port.setter
#    def rest_destination_port(self, value):
#        self.destination_port = value

#    @property
#    def rest_effective_ports(self):
#        if self.effective_ports is not None:
#            return self.effective_ports
#        field_info = self.__class__.__fields__["effective_ports"]
#        try:
#            self.effective_ports =  self.link_based_request(field_info.alias, "GET", return_type="EffectivePorts")
#        except LinkNameException as e:
#            self.effective_ports =  self.link_based_request("effective_ports", "GET", return_type="EffectivePorts")
#        return self.effective_ports
#
#    @rest_effective_ports.setter
#    def rest_effective_ports(self, value):
#        self.effective_ports = value

#    @property
#    def rest_forward_proxy_port(self):
#        if self.forward_proxy_port is not None:
#            return self.forward_proxy_port
#        field_info = self.__class__.__fields__["forward_proxy_port"]
#        try:
#            self.forward_proxy_port =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.forward_proxy_port =  self.link_based_request("forward_proxy_port", "GET", return_type="int")
#        return self.forward_proxy_port
#
#    @rest_forward_proxy_port.setter
#    def rest_forward_proxy_port(self, value):
#        self.forward_proxy_port = value

#    @property
#    def rest_readonly(self):
#        if self.readonly is not None:
#            return self.readonly
#        field_info = self.__class__.__fields__["readonly"]
#        try:
#            self.readonly =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.readonly =  self.link_based_request("readonly", "GET", return_type="bool")
#        return self.readonly
#
#    @rest_readonly.setter
#    def rest_readonly(self, value):
#        self.readonly = value

#    @property
#    def rest_server_listen_port(self):
#        if self.server_listen_port is not None:
#            return self.server_listen_port
#        field_info = self.__class__.__fields__["server_listen_port"]
#        try:
#            self.server_listen_port =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.server_listen_port =  self.link_based_request("server_listen_port", "GET", return_type="int")
#        return self.server_listen_port
#
#    @rest_server_listen_port.setter
#    def rest_server_listen_port(self, value):
#        self.server_listen_port = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PortSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of effective_ports
        if self.effective_ports:
            _dict['EffectivePorts'] = self.effective_ports.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PortSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Automatic": obj.get("Automatic"),
                        "AutomaticDestinationPort": obj.get("AutomaticDestinationPort"),
                        "AutomaticForwardProxyPort": obj.get("AutomaticForwardProxyPort"),
                        "DestinationPort": obj.get("DestinationPort"),
                        "EffectivePorts": EffectivePorts.from_dict(obj["EffectivePorts"]) if obj.get("EffectivePorts") is not None else None,
                        "ForwardProxyPort": obj.get("ForwardProxyPort"),
                        "Readonly": obj.get("Readonly"),
                        "ServerListenPort": obj.get("ServerListenPort")
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
    


