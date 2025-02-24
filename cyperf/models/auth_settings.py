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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.auth_method_type import AuthMethodType
from cyperf.models.params import Params
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "AuthSettings" != "APILink":
    from cyperf.models.api_link import APILink

class AuthSettings(BaseModel):
    """
    AuthSettings
    """ # noqa: E501
    auth_method: Optional[AuthMethodType] = Field(default=None, alias="AuthMethod")
    auth_param: Optional[Params] = Field(default=None, alias="AuthParam")
    certificate_file: Optional[Params] = Field(default=None, description="The authentication certificate file of the VPN tunnel.", alias="CertificateFile")
    key_file: Optional[Params] = Field(default=None, description="The authentication key file of the VPN tunnel.", alias="KeyFile")
    key_file_password: Optional[StrictStr] = Field(default=None, description="The key file password of the TLS VPN authentication.", alias="KeyFilePassword")
    passwords: Optional[List[StrictStr]] = Field(default=None, alias="Passwords")
    passwords_param: Optional[Params] = Field(default=None, alias="PasswordsParam")
    usernames: Optional[List[StrictStr]] = Field(default=None, alias="Usernames")
    usernames_param: Optional[Params] = Field(default=None, alias="UsernamesParam")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["AuthMethod", "AuthParam", "CertificateFile", "KeyFile", "KeyFilePassword", "Passwords", "PasswordsParam", "Usernames", "UsernamesParam"]

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
#            self.auth_method =  self.link_based_request(field_info.alias, "GET", return_type="AuthMethodType")
#        except LinkNameException as e:
#            self.auth_method =  self.link_based_request("auth_method", "GET", return_type="AuthMethodType")
#        return self.auth_method
#
#    @rest_auth_method.setter
#    def rest_auth_method(self, value):
#        self.auth_method = value

#    @property
#    def rest_auth_param(self):
#        if self.auth_param is not None:
#            return self.auth_param
#        field_info = self.__class__.__fields__["auth_param"]
#        try:
#            self.auth_param =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.auth_param =  self.link_based_request("auth_param", "GET", return_type="Params")
#        return self.auth_param
#
#    @rest_auth_param.setter
#    def rest_auth_param(self, value):
#        self.auth_param = value

#    @property
#    def rest_certificate_file(self):
#        if self.certificate_file is not None:
#            return self.certificate_file
#        field_info = self.__class__.__fields__["certificate_file"]
#        try:
#            self.certificate_file =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.certificate_file =  self.link_based_request("certificate_file", "GET", return_type="Params")
#        return self.certificate_file
#
#    @rest_certificate_file.setter
#    def rest_certificate_file(self, value):
#        self.certificate_file = value

#    @property
#    def rest_key_file(self):
#        if self.key_file is not None:
#            return self.key_file
#        field_info = self.__class__.__fields__["key_file"]
#        try:
#            self.key_file =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.key_file =  self.link_based_request("key_file", "GET", return_type="Params")
#        return self.key_file
#
#    @rest_key_file.setter
#    def rest_key_file(self, value):
#        self.key_file = value

#    @property
#    def rest_key_file_password(self):
#        if self.key_file_password is not None:
#            return self.key_file_password
#        field_info = self.__class__.__fields__["key_file_password"]
#        try:
#            self.key_file_password =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.key_file_password =  self.link_based_request("key_file_password", "GET", return_type="str")
#        return self.key_file_password
#
#    @rest_key_file_password.setter
#    def rest_key_file_password(self, value):
#        self.key_file_password = value

#    @property
#    def rest_passwords(self):
#        if self.passwords is not None:
#            return self.passwords
#        field_info = self.__class__.__fields__["passwords"]
#        try:
#            self.passwords =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.passwords =  self.link_based_request("passwords", "GET", return_type="List[str]")
#        return self.passwords
#
#    @rest_passwords.setter
#    def rest_passwords(self, value):
#        self.passwords = value

#    @property
#    def rest_passwords_param(self):
#        if self.passwords_param is not None:
#            return self.passwords_param
#        field_info = self.__class__.__fields__["passwords_param"]
#        try:
#            self.passwords_param =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.passwords_param =  self.link_based_request("passwords_param", "GET", return_type="Params")
#        return self.passwords_param
#
#    @rest_passwords_param.setter
#    def rest_passwords_param(self, value):
#        self.passwords_param = value

#    @property
#    def rest_usernames(self):
#        if self.usernames is not None:
#            return self.usernames
#        field_info = self.__class__.__fields__["usernames"]
#        try:
#            self.usernames =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.usernames =  self.link_based_request("usernames", "GET", return_type="List[str]")
#        return self.usernames
#
#    @rest_usernames.setter
#    def rest_usernames(self, value):
#        self.usernames = value

#    @property
#    def rest_usernames_param(self):
#        if self.usernames_param is not None:
#            return self.usernames_param
#        field_info = self.__class__.__fields__["usernames_param"]
#        try:
#            self.usernames_param =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.usernames_param =  self.link_based_request("usernames_param", "GET", return_type="Params")
#        return self.usernames_param
#
#    @rest_usernames_param.setter
#    def rest_usernames_param(self, value):
#        self.usernames_param = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AuthSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth_param
        if self.auth_param:
            _dict['AuthParam'] = self.auth_param.to_dict()
        # override the default output from pydantic by calling `to_dict()` of certificate_file
        if self.certificate_file:
            _dict['CertificateFile'] = self.certificate_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of key_file
        if self.key_file:
            _dict['KeyFile'] = self.key_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passwords_param
        if self.passwords_param:
            _dict['PasswordsParam'] = self.passwords_param.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usernames_param
        if self.usernames_param:
            _dict['UsernamesParam'] = self.usernames_param.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AuthMethod": obj.get("AuthMethod"),
                        "AuthParam": Params.from_dict(obj["AuthParam"]) if obj.get("AuthParam") is not None else None,
                        "CertificateFile": Params.from_dict(obj["CertificateFile"]) if obj.get("CertificateFile") is not None else None,
                        "KeyFile": Params.from_dict(obj["KeyFile"]) if obj.get("KeyFile") is not None else None,
                        "KeyFilePassword": obj.get("KeyFilePassword"),
                        "Passwords": obj.get("Passwords"),
                        "PasswordsParam": Params.from_dict(obj["PasswordsParam"]) if obj.get("PasswordsParam") is not None else None,
                        "Usernames": obj.get("Usernames"),
                        "UsernamesParam": Params.from_dict(obj["UsernamesParam"]) if obj.get("UsernamesParam") is not None else None
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
    


