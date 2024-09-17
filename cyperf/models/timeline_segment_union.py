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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cyperf.models.segment_type import SegmentType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class TimelineSegmentUnion(BaseModel):
    """
    TimelineSegmentUnion
    """ # noqa: E501
    duration: StrictInt = Field(description="The duration of the timeline segment (default: 600).", alias="Duration")
    segment_type: SegmentType = Field(description="The segment's type. Must be one of: SteadySegment, StepUpSegment, StepDownSegment.", alias="SegmentType")
    warm_up_period: Optional[StrictInt] = Field(default=None, description="Deprecated. Use ObjectivesAndTimeline.WarmUp instead. The time that servers may need to warm up, when clients should wait (default: 0 seconds).", alias="WarmUpPeriod")
    id: StrictStr
    objective_unit: StrictStr = Field(alias="ObjectiveUnit")
    objective_value: Union[StrictFloat, StrictInt] = Field(alias="ObjectiveValue")
    enabled: StrictBool = Field(description="Whether this timeline segment will be used.", alias="Enabled")
    number_of_steps: StrictInt = Field(description="The number of steps to execute. The step value will be computed based on the SteadySegment with the following formula: StepObjectiveValue = SteadySegment.ObjectiveValue / NumberOfSteps.", alias="NumberOfSteps")
    __properties: ClassVar[List[str]] = ["Duration", "SegmentType", "WarmUpPeriod", "id", "ObjectiveUnit", "ObjectiveValue", "Enabled", "NumberOfSteps"]

    @field_validator('objective_unit')
    def objective_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['', 'bps', 'Kbps', 'Mbps', 'Gbps']):
            raise ValueError("must be one of enum values ('', 'bps', 'Kbps', 'Mbps', 'Gbps')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TimelineSegmentUnion from a JSON string"""
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
        """Create an instance of TimelineSegmentUnion from a dict"""
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
                        "ObjectiveUnit": obj.get("ObjectiveUnit"),
                        "ObjectiveValue": obj.get("ObjectiveValue"),
                        "Enabled": obj.get("Enabled"),
                        "NumberOfSteps": obj.get("NumberOfSteps")
            ,
            "links": obj.get("links")
        })
        return _obj


