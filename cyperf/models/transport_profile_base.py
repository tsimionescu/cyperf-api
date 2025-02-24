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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.http_profile import HTTPProfile
from cyperf.models.rtp_profile import RTPProfile
from cyperf.models.tcp_profile import TcpProfile
from cyperf.models.tls_profile import TLSProfile
from cyperf.models.udp_profile import UdpProfile
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "TransportProfileBase" != "APILink":
    from cyperf.models.api_link import APILink

class TransportProfileBase(BaseModel):
    """
    TransportProfileBase
    """ # noqa: E501
    client_http_profile: Optional[HTTPProfile] = Field(default=None, description="The client HTTP profile used in the Scenario.", alias="ClientHTTPProfile")
    client_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ClientTLSProfile")
    client_tcp_profile: Optional[TcpProfile] = Field(default=None, alias="ClientTcpProfile")
    ip_tos: Optional[StrictInt] = Field(default=None, alias="IpTos")
    rtp_profile: Optional[RTPProfile] = Field(default=None, alias="RTPProfile")
    server_http_profile: Optional[HTTPProfile] = Field(default=None, description="The server HTTP profile used in the Scenario.", alias="ServerHTTPProfile")
    server_tls_profile: Optional[TLSProfile] = Field(default=None, alias="ServerTLSProfile")
    server_tcp_profile: Optional[TcpProfile] = Field(default=None, alias="ServerTcpProfile")
    udp_profile: Optional[UdpProfile] = Field(default=None, alias="UdpProfile")
    vlan_prio: Optional[StrictInt] = Field(default=None, alias="VlanPrio")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["ClientHTTPProfile", "ClientTLSProfile", "ClientTcpProfile", "IpTos", "RTPProfile", "ServerHTTPProfile", "ServerTLSProfile", "ServerTcpProfile", "UdpProfile", "VlanPrio"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_client_http_profile(self):
#        if self.client_http_profile is not None:
#            return self.client_http_profile
#        field_info = self.__class__.__fields__["client_http_profile"]
#        try:
#            self.client_http_profile =  self.link_based_request(field_info.alias, "GET", return_type="HTTPProfile")
#        except LinkNameException as e:
#            self.client_http_profile =  self.link_based_request("client_http_profile", "GET", return_type="HTTPProfile")
#        return self.client_http_profile
#
#    @rest_client_http_profile.setter
#    def rest_client_http_profile(self, value):
#        self.client_http_profile = value

#    @property
#    def rest_client_tls_profile(self):
#        if self.client_tls_profile is not None:
#            return self.client_tls_profile
#        field_info = self.__class__.__fields__["client_tls_profile"]
#        try:
#            self.client_tls_profile =  self.link_based_request(field_info.alias, "GET", return_type="TLSProfile")
#        except LinkNameException as e:
#            self.client_tls_profile =  self.link_based_request("client_tls_profile", "GET", return_type="TLSProfile")
#        return self.client_tls_profile
#
#    @rest_client_tls_profile.setter
#    def rest_client_tls_profile(self, value):
#        self.client_tls_profile = value

#    @property
#    def rest_client_tcp_profile(self):
#        if self.client_tcp_profile is not None:
#            return self.client_tcp_profile
#        field_info = self.__class__.__fields__["client_tcp_profile"]
#        try:
#            self.client_tcp_profile =  self.link_based_request(field_info.alias, "GET", return_type="TcpProfile")
#        except LinkNameException as e:
#            self.client_tcp_profile =  self.link_based_request("client_tcp_profile", "GET", return_type="TcpProfile")
#        return self.client_tcp_profile
#
#    @rest_client_tcp_profile.setter
#    def rest_client_tcp_profile(self, value):
#        self.client_tcp_profile = value

#    @property
#    def rest_ip_tos(self):
#        if self.ip_tos is not None:
#            return self.ip_tos
#        field_info = self.__class__.__fields__["ip_tos"]
#        try:
#            self.ip_tos =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.ip_tos =  self.link_based_request("ip_tos", "GET", return_type="int")
#        return self.ip_tos
#
#    @rest_ip_tos.setter
#    def rest_ip_tos(self, value):
#        self.ip_tos = value

#    @property
#    def rest_rtp_profile(self):
#        if self.rtp_profile is not None:
#            return self.rtp_profile
#        field_info = self.__class__.__fields__["rtp_profile"]
#        try:
#            self.rtp_profile =  self.link_based_request(field_info.alias, "GET", return_type="RTPProfile")
#        except LinkNameException as e:
#            self.rtp_profile =  self.link_based_request("rtp_profile", "GET", return_type="RTPProfile")
#        return self.rtp_profile
#
#    @rest_rtp_profile.setter
#    def rest_rtp_profile(self, value):
#        self.rtp_profile = value

#    @property
#    def rest_server_http_profile(self):
#        if self.server_http_profile is not None:
#            return self.server_http_profile
#        field_info = self.__class__.__fields__["server_http_profile"]
#        try:
#            self.server_http_profile =  self.link_based_request(field_info.alias, "GET", return_type="HTTPProfile")
#        except LinkNameException as e:
#            self.server_http_profile =  self.link_based_request("server_http_profile", "GET", return_type="HTTPProfile")
#        return self.server_http_profile
#
#    @rest_server_http_profile.setter
#    def rest_server_http_profile(self, value):
#        self.server_http_profile = value

#    @property
#    def rest_server_tls_profile(self):
#        if self.server_tls_profile is not None:
#            return self.server_tls_profile
#        field_info = self.__class__.__fields__["server_tls_profile"]
#        try:
#            self.server_tls_profile =  self.link_based_request(field_info.alias, "GET", return_type="TLSProfile")
#        except LinkNameException as e:
#            self.server_tls_profile =  self.link_based_request("server_tls_profile", "GET", return_type="TLSProfile")
#        return self.server_tls_profile
#
#    @rest_server_tls_profile.setter
#    def rest_server_tls_profile(self, value):
#        self.server_tls_profile = value

#    @property
#    def rest_server_tcp_profile(self):
#        if self.server_tcp_profile is not None:
#            return self.server_tcp_profile
#        field_info = self.__class__.__fields__["server_tcp_profile"]
#        try:
#            self.server_tcp_profile =  self.link_based_request(field_info.alias, "GET", return_type="TcpProfile")
#        except LinkNameException as e:
#            self.server_tcp_profile =  self.link_based_request("server_tcp_profile", "GET", return_type="TcpProfile")
#        return self.server_tcp_profile
#
#    @rest_server_tcp_profile.setter
#    def rest_server_tcp_profile(self, value):
#        self.server_tcp_profile = value

#    @property
#    def rest_udp_profile(self):
#        if self.udp_profile is not None:
#            return self.udp_profile
#        field_info = self.__class__.__fields__["udp_profile"]
#        try:
#            self.udp_profile =  self.link_based_request(field_info.alias, "GET", return_type="UdpProfile")
#        except LinkNameException as e:
#            self.udp_profile =  self.link_based_request("udp_profile", "GET", return_type="UdpProfile")
#        return self.udp_profile
#
#    @rest_udp_profile.setter
#    def rest_udp_profile(self, value):
#        self.udp_profile = value

#    @property
#    def rest_vlan_prio(self):
#        if self.vlan_prio is not None:
#            return self.vlan_prio
#        field_info = self.__class__.__fields__["vlan_prio"]
#        try:
#            self.vlan_prio =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.vlan_prio =  self.link_based_request("vlan_prio", "GET", return_type="int")
#        return self.vlan_prio
#
#    @rest_vlan_prio.setter
#    def rest_vlan_prio(self, value):
#        self.vlan_prio = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransportProfileBase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_http_profile
        if self.client_http_profile:
            _dict['ClientHTTPProfile'] = self.client_http_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_tls_profile
        if self.client_tls_profile:
            _dict['ClientTLSProfile'] = self.client_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of client_tcp_profile
        if self.client_tcp_profile:
            _dict['ClientTcpProfile'] = self.client_tcp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rtp_profile
        if self.rtp_profile:
            _dict['RTPProfile'] = self.rtp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_http_profile
        if self.server_http_profile:
            _dict['ServerHTTPProfile'] = self.server_http_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_tls_profile
        if self.server_tls_profile:
            _dict['ServerTLSProfile'] = self.server_tls_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_tcp_profile
        if self.server_tcp_profile:
            _dict['ServerTcpProfile'] = self.server_tcp_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of udp_profile
        if self.udp_profile:
            _dict['UdpProfile'] = self.udp_profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportProfileBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "ClientHTTPProfile": HTTPProfile.from_dict(obj["ClientHTTPProfile"]) if obj.get("ClientHTTPProfile") is not None else None,
                        "ClientTLSProfile": TLSProfile.from_dict(obj["ClientTLSProfile"]) if obj.get("ClientTLSProfile") is not None else None,
                        "ClientTcpProfile": TcpProfile.from_dict(obj["ClientTcpProfile"]) if obj.get("ClientTcpProfile") is not None else None,
                        "IpTos": obj.get("IpTos"),
                        "RTPProfile": RTPProfile.from_dict(obj["RTPProfile"]) if obj.get("RTPProfile") is not None else None,
                        "ServerHTTPProfile": HTTPProfile.from_dict(obj["ServerHTTPProfile"]) if obj.get("ServerHTTPProfile") is not None else None,
                        "ServerTLSProfile": TLSProfile.from_dict(obj["ServerTLSProfile"]) if obj.get("ServerTLSProfile") is not None else None,
                        "ServerTcpProfile": TcpProfile.from_dict(obj["ServerTcpProfile"]) if obj.get("ServerTcpProfile") is not None else None,
                        "UdpProfile": UdpProfile.from_dict(obj["UdpProfile"]) if obj.get("UdpProfile") is not None else None,
                        "VlanPrio": obj.get("VlanPrio")
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
    


