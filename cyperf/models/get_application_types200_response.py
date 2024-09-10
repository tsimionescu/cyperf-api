# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cyperf.models.application_type import ApplicationType
from cyperf.models.get_application_types200_response_one_of import GetApplicationTypes200ResponseOneOf
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETAPPLICATIONTYPES200RESPONSE_ONE_OF_SCHEMAS = ["GetApplicationTypes200ResponseOneOf", "List[ApplicationType]"]

class GetApplicationTypes200Response(BaseModel):
    """
    GetApplicationTypes200Response
    """
    # data type: List[ApplicationType]
    oneof_schema_1_validator: Optional[List[ApplicationType]] = None
    # data type: GetApplicationTypes200ResponseOneOf
    oneof_schema_2_validator: Optional[GetApplicationTypes200ResponseOneOf] = None
    actual_instance: Optional[Union[GetApplicationTypes200ResponseOneOf, List[ApplicationType]]] = None
    one_of_schemas: Set[str] = { "GetApplicationTypes200ResponseOneOf", "List[ApplicationType]" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetApplicationTypes200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: List[ApplicationType]
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: GetApplicationTypes200ResponseOneOf
        if not isinstance(v, GetApplicationTypes200ResponseOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GetApplicationTypes200ResponseOneOf`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetApplicationTypes200Response with oneOf schemas: GetApplicationTypes200ResponseOneOf, List[ApplicationType]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetApplicationTypes200Response with oneOf schemas: GetApplicationTypes200ResponseOneOf, List[ApplicationType]. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
#        instance.api_client = client
        error_messages = []
        match = 0

        # deserialize data into List[ApplicationType]
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GetApplicationTypes200ResponseOneOf
        try:
            instance.actual_instance = GetApplicationTypes200ResponseOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetApplicationTypes200Response with oneOf schemas: GetApplicationTypes200ResponseOneOf, List[ApplicationType]. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetApplicationTypes200Response with oneOf schemas: GetApplicationTypes200ResponseOneOf, List[ApplicationType]. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], GetApplicationTypes200ResponseOneOf, List[ApplicationType]]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


