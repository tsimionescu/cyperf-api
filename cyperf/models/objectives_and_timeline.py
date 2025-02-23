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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.advanced_settings import AdvancedSettings
from cyperf.models.secondary_objective import SecondaryObjective
from cyperf.models.specific_objective import SpecificObjective
from cyperf.models.timeline_segment import TimelineSegment
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "ObjectivesAndTimeline" != "APILink":
    from cyperf.models.api_link import APILink

class ObjectivesAndTimeline(BaseModel):
    """
    ObjectivesAndTimeline
    """ # noqa: E501
    advanced_settings: Optional[AdvancedSettings] = Field(default=None, alias="AdvancedSettings")
    primary_objective: Optional[SpecificObjective] = Field(default=None, alias="PrimaryObjective")
    secondary_objective: Optional[SecondaryObjective] = Field(default=None, alias="SecondaryObjective")
    secondary_objectives: Optional[List[SpecificObjective]] = Field(default=None, description="Deprecated. Use SecondaryObjective instead.", alias="SecondaryObjectives")
    timeline_segments: Optional[List[TimelineSegment]] = Field(default=None, description="Deprecated. Use PrimaryObjective.Timeline instead.", alias="TimelineSegments")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["AdvancedSettings", "PrimaryObjective", "SecondaryObjective", "SecondaryObjectives", "TimelineSegments"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_advanced_settings(self):
#        if self.advanced_settings is not None:
#            return self.advanced_settings
#        field_info = self.__class__.__fields__["advanced_settings"]
#        try:
#            self.advanced_settings =  self.link_based_request(field_info.alias, "GET", return_type="AdvancedSettings")
#        except LinkNameException as e:
#            self.advanced_settings =  self.link_based_request("advanced_settings", "GET", return_type="AdvancedSettings")
#        return self.advanced_settings
#
#    @rest_advanced_settings.setter
#    def rest_advanced_settings(self, value):
#        self.advanced_settings = value

#    @property
#    def rest_primary_objective(self):
#        if self.primary_objective is not None:
#            return self.primary_objective
#        field_info = self.__class__.__fields__["primary_objective"]
#        try:
#            self.primary_objective =  self.link_based_request(field_info.alias, "GET", return_type="SpecificObjective")
#        except LinkNameException as e:
#            self.primary_objective =  self.link_based_request("primary_objective", "GET", return_type="SpecificObjective")
#        return self.primary_objective
#
#    @rest_primary_objective.setter
#    def rest_primary_objective(self, value):
#        self.primary_objective = value

#    @property
#    def rest_secondary_objective(self):
#        if self.secondary_objective is not None:
#            return self.secondary_objective
#        field_info = self.__class__.__fields__["secondary_objective"]
#        try:
#            self.secondary_objective =  self.link_based_request(field_info.alias, "GET", return_type="SecondaryObjective")
#        except LinkNameException as e:
#            self.secondary_objective =  self.link_based_request("secondary_objective", "GET", return_type="SecondaryObjective")
#        return self.secondary_objective
#
#    @rest_secondary_objective.setter
#    def rest_secondary_objective(self, value):
#        self.secondary_objective = value

#    @property
#    def rest_secondary_objectives(self):
#        if self.secondary_objectives is not None:
#            return self.secondary_objectives
#        field_info = self.__class__.__fields__["secondary_objectives"]
#        try:
#            self.secondary_objectives =  self.link_based_request(field_info.alias, "GET", return_type="List[SpecificObjective]")
#        except LinkNameException as e:
#            self.secondary_objectives =  self.link_based_request("secondary_objectives", "GET", return_type="List[SpecificObjective]")
#        return self.secondary_objectives
#
#    @rest_secondary_objectives.setter
#    def rest_secondary_objectives(self, value):
#        self.secondary_objectives = value

#    @property
#    def rest_timeline_segments(self):
#        if self.timeline_segments is not None:
#            return self.timeline_segments
#        field_info = self.__class__.__fields__["timeline_segments"]
#        try:
#            self.timeline_segments =  self.link_based_request(field_info.alias, "GET", return_type="List[TimelineSegment]")
#        except LinkNameException as e:
#            self.timeline_segments =  self.link_based_request("timeline_segments", "GET", return_type="List[TimelineSegment]")
#        return self.timeline_segments
#
#    @rest_timeline_segments.setter
#    def rest_timeline_segments(self, value):
#        self.timeline_segments = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ObjectivesAndTimeline from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of advanced_settings
        if self.advanced_settings:
            _dict['AdvancedSettings'] = self.advanced_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_objective
        if self.primary_objective:
            _dict['PrimaryObjective'] = self.primary_objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_objective
        if self.secondary_objective:
            _dict['SecondaryObjective'] = self.secondary_objective.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secondary_objectives (list)
        _items = []
        if self.secondary_objectives:
            for _item in self.secondary_objectives:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SecondaryObjectives'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in timeline_segments (list)
        _items = []
        if self.timeline_segments:
            for _item in self.timeline_segments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['TimelineSegments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectivesAndTimeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AdvancedSettings": AdvancedSettings.from_dict(obj["AdvancedSettings"]) if obj.get("AdvancedSettings") is not None else None,
                        "PrimaryObjective": SpecificObjective.from_dict(obj["PrimaryObjective"]) if obj.get("PrimaryObjective") is not None else None,
                        "SecondaryObjective": SecondaryObjective.from_dict(obj["SecondaryObjective"]) if obj.get("SecondaryObjective") is not None else None,
                        "SecondaryObjectives": [SpecificObjective.from_dict(_item) for _item in obj["SecondaryObjectives"]] if obj.get("SecondaryObjectives") is not None else None,
                        "TimelineSegments": [TimelineSegment.from_dict(_item) for _item in obj["TimelineSegments"]] if obj.get("TimelineSegments") is not None else None
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
    


