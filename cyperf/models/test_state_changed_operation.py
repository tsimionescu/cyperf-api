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
#from cyperf.models import LinkNameException

if "TestStateChangedOperation" != "APILink":
    from cyperf.models.api_link import APILink

class TestStateChangedOperation(BaseModel):
    """
    TestStateChangedOperation
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="An optional message that describes the reason the test ended")
    new_state: Optional[StrictStr] = Field(default=None, description="An optional enum that identifies the current state of the test", alias="newState")
    old_state: Optional[StrictStr] = Field(default=None, description="An optional enum that identifies the previous state of the test", alias="oldState")
    owner: Optional[StrictStr] = Field(default=None, description="An optional friendly display name for the user which initiated the operation")
    owner_id: Optional[StrictStr] = Field(default=None, description="An optional identifier that uniquely identifies the user which initiated the operation", alias="ownerId")
    reason: Optional[StrictStr] = Field(default=None, description="An optional enum that identifies the underlying reason for the test's end")
    test_id: Optional[StrictStr] = Field(default=None, description="The test to which the state change refers", alias="testId")
    timestamp: Optional[StrictInt] = Field(default=None, description="An optional Unix timestamp that indicates when the test state was changed")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["message", "newState", "oldState", "owner", "ownerId", "reason", "testId", "timestamp"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_message(self):
#        if self.message is not None:
#            return self.message
#        field_info = self.__class__.__fields__["message"]
#        try:
#            self.message =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.message =  self.link_based_request("message", "GET", return_type="str")
#        return self.message
#
#    @rest_message.setter
#    def rest_message(self, value):
#        self.message = value

#    @property
#    def rest_new_state(self):
#        if self.new_state is not None:
#            return self.new_state
#        field_info = self.__class__.__fields__["new_state"]
#        try:
#            self.new_state =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.new_state =  self.link_based_request("new_state", "GET", return_type="str")
#        return self.new_state
#
#    @rest_new_state.setter
#    def rest_new_state(self, value):
#        self.new_state = value

#    @property
#    def rest_old_state(self):
#        if self.old_state is not None:
#            return self.old_state
#        field_info = self.__class__.__fields__["old_state"]
#        try:
#            self.old_state =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.old_state =  self.link_based_request("old_state", "GET", return_type="str")
#        return self.old_state
#
#    @rest_old_state.setter
#    def rest_old_state(self, value):
#        self.old_state = value

#    @property
#    def rest_owner(self):
#        if self.owner is not None:
#            return self.owner
#        field_info = self.__class__.__fields__["owner"]
#        try:
#            self.owner =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.owner =  self.link_based_request("owner", "GET", return_type="str")
#        return self.owner
#
#    @rest_owner.setter
#    def rest_owner(self, value):
#        self.owner = value

#    @property
#    def rest_owner_id(self):
#        if self.owner_id is not None:
#            return self.owner_id
#        field_info = self.__class__.__fields__["owner_id"]
#        try:
#            self.owner_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.owner_id =  self.link_based_request("owner_id", "GET", return_type="str")
#        return self.owner_id
#
#    @rest_owner_id.setter
#    def rest_owner_id(self, value):
#        self.owner_id = value

#    @property
#    def rest_reason(self):
#        if self.reason is not None:
#            return self.reason
#        field_info = self.__class__.__fields__["reason"]
#        try:
#            self.reason =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.reason =  self.link_based_request("reason", "GET", return_type="str")
#        return self.reason
#
#    @rest_reason.setter
#    def rest_reason(self, value):
#        self.reason = value

#    @property
#    def rest_test_id(self):
#        if self.test_id is not None:
#            return self.test_id
#        field_info = self.__class__.__fields__["test_id"]
#        try:
#            self.test_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.test_id =  self.link_based_request("test_id", "GET", return_type="str")
#        return self.test_id
#
#    @rest_test_id.setter
#    def rest_test_id(self, value):
#        self.test_id = value

#    @property
#    def rest_timestamp(self):
#        if self.timestamp is not None:
#            return self.timestamp
#        field_info = self.__class__.__fields__["timestamp"]
#        try:
#            self.timestamp =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.timestamp =  self.link_based_request("timestamp", "GET", return_type="int")
#        return self.timestamp
#
#    @rest_timestamp.setter
#    def rest_timestamp(self, value):
#        self.timestamp = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TestStateChangedOperation from a JSON string"""
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
        """Create an instance of TestStateChangedOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "message": obj.get("message"),
                        "newState": obj.get("newState"),
                        "oldState": obj.get("oldState"),
                        "owner": obj.get("owner"),
                        "ownerId": obj.get("ownerId"),
                        "reason": obj.get("reason"),
                        "testId": obj.get("testId"),
                        "timestamp": obj.get("timestamp")
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
    


