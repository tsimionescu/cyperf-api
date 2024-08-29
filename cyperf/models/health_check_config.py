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
from cyperf.models.params import Params
from typing import Optional, Set
from typing_extensions import Self

class HealthCheckConfig(BaseModel):
    """
    The HealthCheck configuration for DUT
    """ # noqa: E501
    enabled: Optional[StrictBool] = Field(default=None, description="A flag indicating if the servers should listen for HealthCheck requests (default: true).", alias="Enabled")
    params: Optional[List[Params]] = Field(default=None, description="A list of additional parameters for the HealthCheck.", alias="Params")
    port: Optional[StrictInt] = Field(default=None, description="The port that the DUT will send HealthCheck requests to the simulated servers. (default: 80)", alias="Port")
    __properties: ClassVar[List[str]] = ["Enabled", "Params", "Port"]

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
        """Create an instance of HealthCheckConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item_params in self.params:
                if _item_params:
                    _items.append(_item_params.to_dict())
            _dict['Params'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HealthCheckConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Enabled": obj.get("Enabled"),
            "Params": [Params.from_dict(_item) for _item in obj["Params"]] if obj.get("Params") is not None else None,
            "Port": obj.get("Port")
        })
        return _obj


