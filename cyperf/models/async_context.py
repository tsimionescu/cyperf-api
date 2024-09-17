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
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field

class AsyncContext(BaseModel):
    """
    AsyncContext
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID of the async operation")
    message: Optional[StrictStr] = Field(default=None, description="A message to the user about the current state of the operation")
    progress: Optional[StrictInt] = Field(default=None, description="Number between 0 and 100 showing the current progress of the operation")
    result: Optional[Any] = Field(default=None, description="The result of the operation. Appears only if the operation is completed. Not required if resultUrl is populated. The actual type of this field is operation specific.")
    result_url: Optional[StrictStr] = Field(default=None, description="The URL where the result of the operation is stored. Appears only if the operation is completed. Not required if the result is populated.", alias="resultUrl")
    state: Optional[StrictStr] = Field(default=None, description="A string enum showing the state of the async operation")
    type: Optional[StrictStr] = Field(default=None, description="The async operation that is being executed")
    url: Optional[StrictStr] = Field(default=None, description="The URL where the user has to call GET requests until the async operation is completed")
    __properties: ClassVar[List[str]] = ["id", "message", "progress", "result", "resultUrl", "state", "type", "url"]

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
        """Create an instance of AsyncContext from a JSON string"""
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
        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AsyncContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "id": obj.get("id"),
                        "message": obj.get("message"),
                        "progress": obj.get("progress"),
                        "result": obj.get("result"),
                        "resultUrl": obj.get("resultUrl"),
                        "state": obj.get("state"),
                        "type": obj.get("type"),
                        "url": obj.get("url")
            ,
            "links": obj.get("links")
        })
        return _obj


