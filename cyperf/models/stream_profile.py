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
from cyperf.models.stream_payload_type import StreamPayloadType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "StreamProfile" != "APILink":
    from cyperf.models.api_link import APILink

class StreamProfile(BaseModel):
    """
    StreamProfile
    """ # noqa: E501
    packet_rate: StrictInt = Field(alias="packetRate")
    payload_size: StrictInt = Field(alias="payloadSize")
    payload_type: StreamPayloadType = Field(alias="payloadType")
    total_estimated_throughput: Optional[StrictStr] = Field(default=None, alias="totalEstimatedThroughput")
    total_estimated_throughput_per_simulated_user: Optional[StrictStr] = Field(default=None, alias="totalEstimatedThroughputPerSimulatedUser")
    unique_pool_size: Optional[StrictInt] = Field(default=None, alias="uniquePoolSize")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["packetRate", "payloadSize", "payloadType", "totalEstimatedThroughput", "totalEstimatedThroughputPerSimulatedUser", "uniquePoolSize"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_packet_rate(self):
#        if self.packet_rate is not None:
#            return self.packet_rate
#        field_info = self.__class__.__fields__["packet_rate"]
#        try:
#            self.packet_rate =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.packet_rate =  self.link_based_request("packet_rate", "GET", return_type="int")
#        return self.packet_rate
#
#    @rest_packet_rate.setter
#    def rest_packet_rate(self, value):
#        self.packet_rate = value

#    @property
#    def rest_payload_size(self):
#        if self.payload_size is not None:
#            return self.payload_size
#        field_info = self.__class__.__fields__["payload_size"]
#        try:
#            self.payload_size =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.payload_size =  self.link_based_request("payload_size", "GET", return_type="int")
#        return self.payload_size
#
#    @rest_payload_size.setter
#    def rest_payload_size(self, value):
#        self.payload_size = value

#    @property
#    def rest_payload_type(self):
#        if self.payload_type is not None:
#            return self.payload_type
#        field_info = self.__class__.__fields__["payload_type"]
#        try:
#            self.payload_type =  self.link_based_request(field_info.alias, "GET", return_type="StreamPayloadType")
#        except LinkNameException as e:
#            self.payload_type =  self.link_based_request("payload_type", "GET", return_type="StreamPayloadType")
#        return self.payload_type
#
#    @rest_payload_type.setter
#    def rest_payload_type(self, value):
#        self.payload_type = value

#    @property
#    def rest_total_estimated_throughput(self):
#        if self.total_estimated_throughput is not None:
#            return self.total_estimated_throughput
#        field_info = self.__class__.__fields__["total_estimated_throughput"]
#        try:
#            self.total_estimated_throughput =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.total_estimated_throughput =  self.link_based_request("total_estimated_throughput", "GET", return_type="str")
#        return self.total_estimated_throughput
#
#    @rest_total_estimated_throughput.setter
#    def rest_total_estimated_throughput(self, value):
#        self.total_estimated_throughput = value

#    @property
#    def rest_total_estimated_throughput_per_simulated_user(self):
#        if self.total_estimated_throughput_per_simulated_user is not None:
#            return self.total_estimated_throughput_per_simulated_user
#        field_info = self.__class__.__fields__["total_estimated_throughput_per_simulated_user"]
#        try:
#            self.total_estimated_throughput_per_simulated_user =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.total_estimated_throughput_per_simulated_user =  self.link_based_request("total_estimated_throughput_per_simulated_user", "GET", return_type="str")
#        return self.total_estimated_throughput_per_simulated_user
#
#    @rest_total_estimated_throughput_per_simulated_user.setter
#    def rest_total_estimated_throughput_per_simulated_user(self, value):
#        self.total_estimated_throughput_per_simulated_user = value

#    @property
#    def rest_unique_pool_size(self):
#        if self.unique_pool_size is not None:
#            return self.unique_pool_size
#        field_info = self.__class__.__fields__["unique_pool_size"]
#        try:
#            self.unique_pool_size =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.unique_pool_size =  self.link_based_request("unique_pool_size", "GET", return_type="int")
#        return self.unique_pool_size
#
#    @rest_unique_pool_size.setter
#    def rest_unique_pool_size(self, value):
#        self.unique_pool_size = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StreamProfile from a JSON string"""
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
        """Create an instance of StreamProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "packetRate": obj.get("packetRate"),
                        "payloadSize": obj.get("payloadSize"),
                        "payloadType": obj.get("payloadType"),
                        "totalEstimatedThroughput": obj.get("totalEstimatedThroughput"),
                        "totalEstimatedThroughputPerSimulatedUser": obj.get("totalEstimatedThroughputPerSimulatedUser"),
                        "uniquePoolSize": obj.get("uniquePoolSize")
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
    


