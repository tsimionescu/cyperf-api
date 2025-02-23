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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response" != "APILink":
    from cyperf.models.api_link import APILink

class AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response(BaseModel):
    """
    AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response
    """ # noqa: E501
    access_token: Optional[StrictStr] = Field(default=None, description="The access token. Set this in the Authorization HTTP Header to authenticate requests.")
    expires_in: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The access token lifetime.")
    refresh_expires_in: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The refresh token lifetime.")
    refresh_token: Optional[StrictStr] = Field(default=None, description="Token that can be used with this request and grant_type: refresh_token to get a new access_token if the current one expires.")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["access_token", "expires_in", "refresh_expires_in", "refresh_token"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_access_token(self):
#        if self.access_token is not None:
#            return self.access_token
#        field_info = self.__class__.__fields__["access_token"]
#        try:
#            self.access_token =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.access_token =  self.link_based_request("access_token", "GET", return_type="str")
#        return self.access_token
#
#    @rest_access_token.setter
#    def rest_access_token(self, value):
#        self.access_token = value

#    @property
#    def rest_expires_in(self):
#        if self.expires_in is not None:
#            return self.expires_in
#        field_info = self.__class__.__fields__["expires_in"]
#        try:
#            self.expires_in =  self.link_based_request(field_info.alias, "GET", return_type="float")
#        except LinkNameException as e:
#            self.expires_in =  self.link_based_request("expires_in", "GET", return_type="float")
#        return self.expires_in
#
#    @rest_expires_in.setter
#    def rest_expires_in(self, value):
#        self.expires_in = value

#    @property
#    def rest_refresh_expires_in(self):
#        if self.refresh_expires_in is not None:
#            return self.refresh_expires_in
#        field_info = self.__class__.__fields__["refresh_expires_in"]
#        try:
#            self.refresh_expires_in =  self.link_based_request(field_info.alias, "GET", return_type="float")
#        except LinkNameException as e:
#            self.refresh_expires_in =  self.link_based_request("refresh_expires_in", "GET", return_type="float")
#        return self.refresh_expires_in
#
#    @rest_refresh_expires_in.setter
#    def rest_refresh_expires_in(self, value):
#        self.refresh_expires_in = value

#    @property
#    def rest_refresh_token(self):
#        if self.refresh_token is not None:
#            return self.refresh_token
#        field_info = self.__class__.__fields__["refresh_token"]
#        try:
#            self.refresh_token =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.refresh_token =  self.link_based_request("refresh_token", "GET", return_type="str")
#        return self.refresh_token
#
#    @rest_refresh_token.setter
#    def rest_refresh_token(self, value):
#        self.refresh_token = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response from a JSON string"""
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
        """Create an instance of AuthRealmsKeysightProtocolOpenidConnectTokenPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
                        "expires_in": obj.get("expires_in"),
                        "refresh_expires_in": obj.get("refresh_expires_in"),
                        "refresh_token": obj.get("refresh_token")
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
    


