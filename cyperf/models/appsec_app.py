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
from cyperf.models.application import Application
from typing import Optional, Set
from typing_extensions import Self

class AppsecApp(BaseModel):
    """
    AppsecApp
    """ # noqa: E501
    app: Optional[Application] = Field(default=None, alias="App")
    description: Optional[StrictStr] = Field(default=None, description="The description of the application", alias="Description")
    name: Optional[StrictStr] = Field(default=None, description="The user friendly name of the application", alias="Name")
    static: Optional[StrictBool] = Field(default=None, description="If true, the application/strike is generated from Controller", alias="Static")
    user_defined: Optional[StrictBool] = Field(default=None, description="If true, the application was created by the user", alias="UserDefined")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application")
    owner: Optional[StrictStr] = Field(default=None, description="The friendly display name of the application's owner")
    owner_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the application's owner", alias="ownerId")
    __properties: ClassVar[List[str]] = ["App", "Description", "Name", "Static", "UserDefined", "id", "owner", "ownerId"]

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
        """Create an instance of AppsecApp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "static",
            "user_defined",
            "id",
            "owner",
            "owner_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['App'] = self.app.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppsecApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "App": Application.from_dict(obj["App"]) if obj.get("App") is not None else None,
            "Description": obj.get("Description"),
            "Name": obj.get("Name"),
            "Static": obj.get("Static"),
            "UserDefined": obj.get("UserDefined"),
            "id": obj.get("id"),
            "owner": obj.get("owner"),
            "ownerId": obj.get("ownerId")
        })
        return _obj


