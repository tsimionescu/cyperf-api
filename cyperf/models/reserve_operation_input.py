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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.agent_reservation import AgentReservation
from cyperf.models.payload_meta import PayloadMeta
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "ReserveOperationInput" != "APILink":
    from cyperf.models.api_link import APILink

class ReserveOperationInput(BaseModel):
    """
    ReserveOperationInput
    """ # noqa: E501
    agents_data: Optional[List[AgentReservation]] = Field(default=None, alias="agentsData")
    force: Optional[StrictBool] = None
    owner: Optional[StrictStr] = None
    owner_id: Optional[StrictStr] = Field(default=None, alias="ownerId")
    payloads: Optional[Dict[str, PayloadMeta]] = None
    session_id: Optional[StrictStr] = Field(default=None, alias="sessionId")
    session_name: Optional[StrictStr] = Field(default=None, alias="sessionName")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["agentsData", "force", "owner", "ownerId", "payloads", "sessionId", "sessionName"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_agents_data(self):
#        if self.agents_data is not None:
#            return self.agents_data
#        field_info = self.__class__.__fields__["agents_data"]
#        try:
#            self.agents_data =  self.link_based_request(field_info.alias, "GET", return_type="List[AgentReservation]")
#        except LinkNameException as e:
#            self.agents_data =  self.link_based_request("agents_data", "GET", return_type="List[AgentReservation]")
#        return self.agents_data
#
#    @rest_agents_data.setter
#    def rest_agents_data(self, value):
#        self.agents_data = value

#    @property
#    def rest_force(self):
#        if self.force is not None:
#            return self.force
#        field_info = self.__class__.__fields__["force"]
#        try:
#            self.force =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.force =  self.link_based_request("force", "GET", return_type="bool")
#        return self.force
#
#    @rest_force.setter
#    def rest_force(self, value):
#        self.force = value

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
#    def rest_payloads(self):
#        if self.payloads is not None:
#            return self.payloads
#        field_info = self.__class__.__fields__["payloads"]
#        try:
#            self.payloads =  self.link_based_request(field_info.alias, "GET", return_type="Dict[str, PayloadMeta]")
#        except LinkNameException as e:
#            self.payloads =  self.link_based_request("payloads", "GET", return_type="Dict[str, PayloadMeta]")
#        return self.payloads
#
#    @rest_payloads.setter
#    def rest_payloads(self, value):
#        self.payloads = value

#    @property
#    def rest_session_id(self):
#        if self.session_id is not None:
#            return self.session_id
#        field_info = self.__class__.__fields__["session_id"]
#        try:
#            self.session_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.session_id =  self.link_based_request("session_id", "GET", return_type="str")
#        return self.session_id
#
#    @rest_session_id.setter
#    def rest_session_id(self, value):
#        self.session_id = value

#    @property
#    def rest_session_name(self):
#        if self.session_name is not None:
#            return self.session_name
#        field_info = self.__class__.__fields__["session_name"]
#        try:
#            self.session_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.session_name =  self.link_based_request("session_name", "GET", return_type="str")
#        return self.session_name
#
#    @rest_session_name.setter
#    def rest_session_name(self, value):
#        self.session_name = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReserveOperationInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents_data (list)
        _items = []
        if self.agents_data:
            for _item in self.agents_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agentsData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in payloads (dict)
        _field_dict = {}
        if self.payloads:
            for _key in self.payloads:
                if self.payloads[_key]:
                    _field_dict[_key] = self.payloads[_key].to_dict()
            _dict['payloads'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReserveOperationInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "agentsData": [AgentReservation.from_dict(_item) for _item in obj["agentsData"]] if obj.get("agentsData") is not None else None,
                        "force": obj.get("force"),
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "payloads": dict(
                (_k, PayloadMeta.from_dict(_v))
                for _k, _v in obj["payloads"].items()
            )
            if obj.get("payloads") is not None
            else None,
                        "sessionId": obj.get("sessionId"),
                        "sessionName": obj.get("sessionName")
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
    


