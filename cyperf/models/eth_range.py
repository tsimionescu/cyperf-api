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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cyperf.models.static_arp_entry import StaticARPEntry
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "EthRange" != "APILink":
    from cyperf.models.api_link import APILink

class EthRange(BaseModel):
    """
    The Ethernet Ranges assigned to the current test configuration
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, alias="Count")
    mac_auto: StrictBool = Field(description="A flag indicating if the MAC address for the EthRange should be determined automatically (default: true).", alias="MacAuto")
    mac_incr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The MAC address increment rule for the EthRange (default: 00:00:00:00:00:01).", alias="MacIncr")
    mac_start: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The MAC start address for the EthRange (default: 01:02:03:04:05:06).", alias="MacStart")
    one_mac_per_ip: Optional[StrictBool] = Field(default=None, description="A flag indicating if there is only one MAC address for the EthRange per IPRange (default: true).", alias="OneMacPerIP")
    static_arp_table: Optional[List[StaticARPEntry]] = Field(default=None, alias="StaticARPTable")
    max_count_per_agent: Optional[StrictInt] = Field(default=None, description="The maximum number of MACs that should be assigned to each traffic agent for this Ethernet range segment in a valid test (default: 0, split equally between agents).", alias="maxCountPerAgent")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["Count", "MacAuto", "MacIncr", "MacStart", "OneMacPerIP", "StaticARPTable", "maxCountPerAgent"]

    @field_validator('mac_incr')
    def mac_incr_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|(^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$)", value):
            raise ValueError(r"must validate the regular expression /^$|(^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$)/")
        return value

    @field_validator('mac_start')
    def mac_start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|(^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$)", value):
            raise ValueError(r"must validate the regular expression /^$|(^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$)/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_count(self):
#        if self.count is not None:
#            return self.count
#        field_info = self.__class__.__fields__["count"]
#        try:
#            self.count =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.count =  self.link_based_request("count", "GET", return_type="int")
#        return self.count
#
#    @rest_count.setter
#    def rest_count(self, value):
#        self.count = value

#    @property
#    def rest_mac_auto(self):
#        if self.mac_auto is not None:
#            return self.mac_auto
#        field_info = self.__class__.__fields__["mac_auto"]
#        try:
#            self.mac_auto =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.mac_auto =  self.link_based_request("mac_auto", "GET", return_type="bool")
#        return self.mac_auto
#
#    @rest_mac_auto.setter
#    def rest_mac_auto(self, value):
#        self.mac_auto = value

#    @property
#    def rest_mac_incr(self):
#        if self.mac_incr is not None:
#            return self.mac_incr
#        field_info = self.__class__.__fields__["mac_incr"]
#        try:
#            self.mac_incr =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.mac_incr =  self.link_based_request("mac_incr", "GET", return_type="str")
#        return self.mac_incr
#
#    @rest_mac_incr.setter
#    def rest_mac_incr(self, value):
#        self.mac_incr = value

#    @property
#    def rest_mac_start(self):
#        if self.mac_start is not None:
#            return self.mac_start
#        field_info = self.__class__.__fields__["mac_start"]
#        try:
#            self.mac_start =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.mac_start =  self.link_based_request("mac_start", "GET", return_type="str")
#        return self.mac_start
#
#    @rest_mac_start.setter
#    def rest_mac_start(self, value):
#        self.mac_start = value

#    @property
#    def rest_one_mac_per_ip(self):
#        if self.one_mac_per_ip is not None:
#            return self.one_mac_per_ip
#        field_info = self.__class__.__fields__["one_mac_per_ip"]
#        try:
#            self.one_mac_per_ip =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.one_mac_per_ip =  self.link_based_request("one_mac_per_ip", "GET", return_type="bool")
#        return self.one_mac_per_ip
#
#    @rest_one_mac_per_ip.setter
#    def rest_one_mac_per_ip(self, value):
#        self.one_mac_per_ip = value

#    @property
#    def rest_static_arp_table(self):
#        if self.static_arp_table is not None:
#            return self.static_arp_table
#        field_info = self.__class__.__fields__["static_arp_table"]
#        try:
#            self.static_arp_table =  self.link_based_request(field_info.alias, "GET", return_type="List[StaticARPEntry]")
#        except LinkNameException as e:
#            self.static_arp_table =  self.link_based_request("static_arp_table", "GET", return_type="List[StaticARPEntry]")
#        return self.static_arp_table
#
#    @rest_static_arp_table.setter
#    def rest_static_arp_table(self, value):
#        self.static_arp_table = value

#    @property
#    def rest_max_count_per_agent(self):
#        if self.max_count_per_agent is not None:
#            return self.max_count_per_agent
#        field_info = self.__class__.__fields__["max_count_per_agent"]
#        try:
#            self.max_count_per_agent =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.max_count_per_agent =  self.link_based_request("max_count_per_agent", "GET", return_type="int")
#        return self.max_count_per_agent
#
#    @rest_max_count_per_agent.setter
#    def rest_max_count_per_agent(self, value):
#        self.max_count_per_agent = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EthRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in static_arp_table (list)
        _items = []
        if self.static_arp_table:
            for _item in self.static_arp_table:
                if _item:
                    _items.append(_item.to_dict())
            _dict['StaticARPTable'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EthRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Count": obj.get("Count"),
                        "MacAuto": obj.get("MacAuto"),
                        "MacIncr": obj.get("MacIncr"),
                        "MacStart": obj.get("MacStart"),
                        "OneMacPerIP": obj.get("OneMacPerIP"),
                        "StaticARPTable": [StaticARPEntry.from_dict(_item) for _item in obj["StaticARPTable"]] if obj.get("StaticARPTable") is not None else None,
                        "maxCountPerAgent": obj.get("maxCountPerAgent")
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
    


