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
from cyperf.models.enum import Enum
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "Metadata" != "APILink":
    from cyperf.models.api_link import APILink

class Metadata(BaseModel):
    """
    Metadata
    """ # noqa: E501
    auth_method: Optional[Enum] = Field(default=None, alias="AuthMethod")
    explicit_proxy: Optional[StrictBool] = Field(default=None, description="This is an authentication profile used along with an explicit proxy", alias="ExplicitProxy")
    idp_type: Optional[Enum] = Field(default=None, alias="IDPType")
    sgw_name: Optional[StrictStr] = Field(default=None, description="The name of the secure gateway", alias="SGWName")
    sgw_type: Optional[StrictStr] = Field(default=None, description="The type of the secure gateway", alias="SGWType")
    sgw_type_value: Optional[StrictStr] = Field(default=None, description="The agent secure gateway type value of the secure gateway type", alias="SGWTypeValue")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["AuthMethod", "ExplicitProxy", "IDPType", "SGWName", "SGWType", "SGWTypeValue"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_auth_method(self):
#        if self.auth_method is not None:
#            return self.auth_method
#        field_info = self.__class__.__fields__["auth_method"]
#        try:
#            self.auth_method =  self.link_based_request(field_info.alias, "GET", return_type="Enum")
#        except LinkNameException as e:
#            self.auth_method =  self.link_based_request("auth_method", "GET", return_type="Enum")
#        return self.auth_method
#
#    @rest_auth_method.setter
#    def rest_auth_method(self, value):
#        self.auth_method = value

#    @property
#    def rest_explicit_proxy(self):
#        if self.explicit_proxy is not None:
#            return self.explicit_proxy
#        field_info = self.__class__.__fields__["explicit_proxy"]
#        try:
#            self.explicit_proxy =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.explicit_proxy =  self.link_based_request("explicit_proxy", "GET", return_type="bool")
#        return self.explicit_proxy
#
#    @rest_explicit_proxy.setter
#    def rest_explicit_proxy(self, value):
#        self.explicit_proxy = value

#    @property
#    def rest_idp_type(self):
#        if self.idp_type is not None:
#            return self.idp_type
#        field_info = self.__class__.__fields__["idp_type"]
#        try:
#            self.idp_type =  self.link_based_request(field_info.alias, "GET", return_type="Enum")
#        except LinkNameException as e:
#            self.idp_type =  self.link_based_request("idp_type", "GET", return_type="Enum")
#        return self.idp_type
#
#    @rest_idp_type.setter
#    def rest_idp_type(self, value):
#        self.idp_type = value

#    @property
#    def rest_sgw_name(self):
#        if self.sgw_name is not None:
#            return self.sgw_name
#        field_info = self.__class__.__fields__["sgw_name"]
#        try:
#            self.sgw_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.sgw_name =  self.link_based_request("sgw_name", "GET", return_type="str")
#        return self.sgw_name
#
#    @rest_sgw_name.setter
#    def rest_sgw_name(self, value):
#        self.sgw_name = value

#    @property
#    def rest_sgw_type(self):
#        if self.sgw_type is not None:
#            return self.sgw_type
#        field_info = self.__class__.__fields__["sgw_type"]
#        try:
#            self.sgw_type =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.sgw_type =  self.link_based_request("sgw_type", "GET", return_type="str")
#        return self.sgw_type
#
#    @rest_sgw_type.setter
#    def rest_sgw_type(self, value):
#        self.sgw_type = value

#    @property
#    def rest_sgw_type_value(self):
#        if self.sgw_type_value is not None:
#            return self.sgw_type_value
#        field_info = self.__class__.__fields__["sgw_type_value"]
#        try:
#            self.sgw_type_value =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.sgw_type_value =  self.link_based_request("sgw_type_value", "GET", return_type="str")
#        return self.sgw_type_value
#
#    @rest_sgw_type_value.setter
#    def rest_sgw_type_value(self, value):
#        self.sgw_type_value = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Metadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_method
        if self.auth_method:
            _dict['AuthMethod'] = self.auth_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of idp_type
        if self.idp_type:
            _dict['IDPType'] = self.idp_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Metadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AuthMethod": Enum.from_dict(obj["AuthMethod"]) if obj.get("AuthMethod") is not None else None,
                        "ExplicitProxy": obj.get("ExplicitProxy"),
                        "IDPType": Enum.from_dict(obj["IDPType"]) if obj.get("IDPType") is not None else None,
                        "SGWName": obj.get("SGWName"),
                        "SGWType": obj.get("SGWType"),
                        "SGWTypeValue": obj.get("SGWTypeValue")
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
    


