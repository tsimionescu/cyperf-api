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
from typing import Optional, Set
from typing_extensions import Self

class PreparedTestOptions(BaseModel):
    """
    PreparedTestOptions
    """ # noqa: E501
    add_activity_meta: Optional[StrictBool] = Field(default=None, alias="AddActivityMeta")
    datasource_for_ui_views: Optional[StrictStr] = Field(default=None, alias="DatasourceForUIViews")
    extra_tags: Optional[Dict[str, List[StrictStr]]] = Field(default=None, alias="ExtraTags")
    filter_by_properties: Optional[Dict[str, StrictStr]] = Field(default=None, alias="FilterByProperties")
    format_protocol_name: Optional[StrictBool] = Field(default=None, alias="FormatProtocolName")
    override_properties: Optional[Dict[str, StrictStr]] = Field(default=None, alias="OverrideProperties")
    __properties: ClassVar[List[str]] = ["AddActivityMeta", "DatasourceForUIViews", "ExtraTags", "FilterByProperties", "FormatProtocolName", "OverrideProperties"]

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
        """Create an instance of PreparedTestOptions from a JSON string"""
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
        """Create an instance of PreparedTestOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AddActivityMeta": obj.get("AddActivityMeta"),
            "DatasourceForUIViews": obj.get("DatasourceForUIViews"),
            "ExtraTags": obj.get("ExtraTags"),
            "FilterByProperties": obj.get("FilterByProperties"),
            "FormatProtocolName": obj.get("FormatProtocolName"),
            "OverrideProperties": obj.get("OverrideProperties")
        })
        return _obj


