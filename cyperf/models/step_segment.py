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
from cyperf.models.segment_type import SegmentType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "StepSegment" != "APILink":
    from cyperf.models.api_link import APILink

class StepSegment(BaseModel):
    """
    StepSegment
    """ # noqa: E501
    duration: StrictInt = Field(description="The duration of the timeline segment (default: 600).", alias="Duration")
    segment_type: SegmentType = Field(description="The segment's type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment.", alias="SegmentType")
    warm_up_period: Optional[StrictInt] = Field(default=None, description="Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds).", alias="WarmUpPeriod")
    id: StrictStr
    enabled: StrictBool = Field(description="Whether this timeline segment will be used.", alias="Enabled")
    number_of_steps: StrictInt = Field(description="The number of steps to execute. The step value will be computed based on the SteadySegment with the following formula: StepObjectiveValue = SteadySegment.ObjectiveValue / NumberOfSteps.", alias="NumberOfSteps")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["Duration", "SegmentType", "WarmUpPeriod", "id", "Enabled", "NumberOfSteps"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_duration(self):
#        if self.duration is not None:
#            return self.duration
#        field_info = self.__class__.__fields__["duration"]
#        try:
#            self.duration =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.duration =  self.link_based_request("duration", "GET", return_type="int")
#        return self.duration
#
#    @rest_duration.setter
#    def rest_duration(self, value):
#        self.duration = value

#    @property
#    def rest_segment_type(self):
#        if self.segment_type is not None:
#            return self.segment_type
#        field_info = self.__class__.__fields__["segment_type"]
#        try:
#            self.segment_type =  self.link_based_request(field_info.alias, "GET", return_type="SegmentType")
#        except LinkNameException as e:
#            self.segment_type =  self.link_based_request("segment_type", "GET", return_type="SegmentType")
#        return self.segment_type
#
#    @rest_segment_type.setter
#    def rest_segment_type(self, value):
#        self.segment_type = value

#    @property
#    def rest_warm_up_period(self):
#        if self.warm_up_period is not None:
#            return self.warm_up_period
#        field_info = self.__class__.__fields__["warm_up_period"]
#        try:
#            self.warm_up_period =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.warm_up_period =  self.link_based_request("warm_up_period", "GET", return_type="int")
#        return self.warm_up_period
#
#    @rest_warm_up_period.setter
#    def rest_warm_up_period(self, value):
#        self.warm_up_period = value

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
#    def rest_enabled(self):
#        if self.enabled is not None:
#            return self.enabled
#        field_info = self.__class__.__fields__["enabled"]
#        try:
#            self.enabled =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.enabled =  self.link_based_request("enabled", "GET", return_type="bool")
#        return self.enabled
#
#    @rest_enabled.setter
#    def rest_enabled(self, value):
#        self.enabled = value

#    @property
#    def rest_number_of_steps(self):
#        if self.number_of_steps is not None:
#            return self.number_of_steps
#        field_info = self.__class__.__fields__["number_of_steps"]
#        try:
#            self.number_of_steps =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.number_of_steps =  self.link_based_request("number_of_steps", "GET", return_type="int")
#        return self.number_of_steps
#
#    @rest_number_of_steps.setter
#    def rest_number_of_steps(self, value):
#        self.number_of_steps = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StepSegment from a JSON string"""
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
        """Create an instance of StepSegment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Duration": obj.get("Duration"),
                        "SegmentType": obj.get("SegmentType"),
                        "WarmUpPeriod": obj.get("WarmUpPeriod"),
                        "id": obj.get("id"),
                        "Enabled": obj.get("Enabled"),
                        "NumberOfSteps": obj.get("NumberOfSteps")
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
    


