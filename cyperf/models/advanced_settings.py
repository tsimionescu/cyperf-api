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
from cyperf.models.agent_optimization_mode import AgentOptimizationMode
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class AdvancedSettings(BaseModel):
    """
    AdvancedSettings
    """ # noqa: E501
    agent_optimization_mode: Optional[AgentOptimizationMode] = Field(default=None, alias="AgentOptimizationMode")
    agent_streaming_purpose_cpu_percent: Optional[StrictInt] = Field(default=None, description="The CPU percentage reserved for streaming purpose use (default: 0).", alias="AgentStreamingPurposeCPUPercent")
    automatic_cpu_percent: Optional[StrictBool] = Field(default=None, description="Deprecated. Use the calibration operation to find the best value for AgentStreamingPurposeCPUPercent for the current assigned agents.", alias="AutomaticCPUPercent")
    connection_graceful_stop_timeout: Optional[StrictInt] = Field(default=None, description="The time the test will wait all connections to be graceful stopped (default: 15 seconds).", alias="ConnectionGracefulStopTimeout")
    warm_up_period: StrictInt = Field(description="The time that servers may need to warm up, when clients should wait (default: 0 seconds).", alias="WarmUpPeriod")
    __properties: ClassVar[List[str]] = ["AgentOptimizationMode", "AgentStreamingPurposeCPUPercent", "AutomaticCPUPercent", "ConnectionGracefulStopTimeout", "WarmUpPeriod"]

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
        """Create an instance of AdvancedSettings from a JSON string"""
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
        """Create an instance of AdvancedSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AgentOptimizationMode": obj.get("AgentOptimizationMode"),
                        "AgentStreamingPurposeCPUPercent": obj.get("AgentStreamingPurposeCPUPercent"),
                        "AutomaticCPUPercent": obj.get("AutomaticCPUPercent"),
                        "ConnectionGracefulStopTimeout": obj.get("ConnectionGracefulStopTimeout"),
                        "WarmUpPeriod": obj.get("WarmUpPeriod")
            ,
            "links": obj.get("links")
        })
        return _obj


