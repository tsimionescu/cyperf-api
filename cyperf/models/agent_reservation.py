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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "AgentReservation" != "APILink":
    from cyperf.models.api_link import APILink

class AgentReservation(BaseModel):
    """
    AgentReservation
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, alias="agentId")
    agent_payload_names: Optional[List[StrictStr]] = Field(default=None, alias="agentPayloadNames")
    general_purpose_cpu_percent: Optional[StrictInt] = Field(default=None, alias="generalPurposeCPUPercent")
    interfaces: Optional[List[StrictStr]] = None
    ip_address_version_used: Optional[StrictStr] = Field(default=None, alias="ipAddressVersionUsed")
    optimization_mode: Optional[StrictStr] = Field(default=None, alias="optimizationMode")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["agentId", "agentPayloadNames", "generalPurposeCPUPercent", "interfaces", "ipAddressVersionUsed", "optimizationMode"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_agent_id(self):
#        if self.agent_id is not None:
#            return self.agent_id
#        field_info = self.__class__.__fields__["agent_id"]
#        try:
#            self.agent_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.agent_id =  self.link_based_request("agent_id", "GET", return_type="str")
#        return self.agent_id
#
#    @rest_agent_id.setter
#    def rest_agent_id(self, value):
#        self.agent_id = value

#    @property
#    def rest_agent_payload_names(self):
#        if self.agent_payload_names is not None:
#            return self.agent_payload_names
#        field_info = self.__class__.__fields__["agent_payload_names"]
#        try:
#            self.agent_payload_names =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.agent_payload_names =  self.link_based_request("agent_payload_names", "GET", return_type="List[str]")
#        return self.agent_payload_names
#
#    @rest_agent_payload_names.setter
#    def rest_agent_payload_names(self, value):
#        self.agent_payload_names = value

#    @property
#    def rest_general_purpose_cpu_percent(self):
#        if self.general_purpose_cpu_percent is not None:
#            return self.general_purpose_cpu_percent
#        field_info = self.__class__.__fields__["general_purpose_cpu_percent"]
#        try:
#            self.general_purpose_cpu_percent =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.general_purpose_cpu_percent =  self.link_based_request("general_purpose_cpu_percent", "GET", return_type="int")
#        return self.general_purpose_cpu_percent
#
#    @rest_general_purpose_cpu_percent.setter
#    def rest_general_purpose_cpu_percent(self, value):
#        self.general_purpose_cpu_percent = value

#    @property
#    def rest_interfaces(self):
#        if self.interfaces is not None:
#            return self.interfaces
#        field_info = self.__class__.__fields__["interfaces"]
#        try:
#            self.interfaces =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.interfaces =  self.link_based_request("interfaces", "GET", return_type="List[str]")
#        return self.interfaces
#
#    @rest_interfaces.setter
#    def rest_interfaces(self, value):
#        self.interfaces = value

#    @property
#    def rest_ip_address_version_used(self):
#        if self.ip_address_version_used is not None:
#            return self.ip_address_version_used
#        field_info = self.__class__.__fields__["ip_address_version_used"]
#        try:
#            self.ip_address_version_used =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.ip_address_version_used =  self.link_based_request("ip_address_version_used", "GET", return_type="str")
#        return self.ip_address_version_used
#
#    @rest_ip_address_version_used.setter
#    def rest_ip_address_version_used(self, value):
#        self.ip_address_version_used = value

#    @property
#    def rest_optimization_mode(self):
#        if self.optimization_mode is not None:
#            return self.optimization_mode
#        field_info = self.__class__.__fields__["optimization_mode"]
#        try:
#            self.optimization_mode =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.optimization_mode =  self.link_based_request("optimization_mode", "GET", return_type="str")
#        return self.optimization_mode
#
#    @rest_optimization_mode.setter
#    def rest_optimization_mode(self, value):
#        self.optimization_mode = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AgentReservation from a JSON string"""
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
        """Create an instance of AgentReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
                        "agentPayloadNames": obj.get("agentPayloadNames"),
                        "generalPurposeCPUPercent": obj.get("generalPurposeCPUPercent"),
                        "interfaces": obj.get("interfaces"),
                        "ipAddressVersionUsed": obj.get("ipAddressVersionUsed"),
                        "optimizationMode": obj.get("optimizationMode")
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
    


