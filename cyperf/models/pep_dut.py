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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cyperf.models.params import Params
from cyperf.models.simulated_id_p import SimulatedIdP
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "PepDUT" != "APILink":
    from cyperf.models.api_link import APILink

class PepDUT(BaseModel):
    """
    The Policy Enforcement Point (PEP) device under test (also known as Zero Trust device)
    """ # noqa: E501
    auth_method: Optional[Params] = Field(default=None, alias="AuthMethod")
    auth_profile_params: Optional[List[Params]] = Field(default=None, alias="AuthProfileParams")
    auth_profile_type: Optional[StrictStr] = Field(default=None, alias="AuthProfileType")
    hostname_suffix: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A suffix to be added to the Host header of all Apps/Attacks running through the DUT (default: empty string).", alias="HostnameSuffix")
    idp_type: Optional[Params] = Field(default=None, alias="IDPType")
    is_explicit_proxy: Optional[StrictBool] = Field(default=None, description="A flag indicating if PEP for the selected authentication profile is an explicit proxy", alias="IsExplicitProxy")
    pep_host: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The hostname where the traffic goes if PEP device is active.", alias="PEPHost")
    pep_port: Optional[StrictInt] = Field(default=None, description="The listen port for PEP DUT (default: 443).", alias="PEPPort")
    simulated_id_p: Optional[SimulatedIdP] = Field(default=None, alias="SimulatedIdP")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["AuthMethod", "AuthProfileParams", "AuthProfileType", "HostnameSuffix", "IDPType", "IsExplicitProxy", "PEPHost", "PEPPort", "SimulatedIdP"]

    @field_validator('hostname_suffix')
    def hostname_suffix_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$", value):
            raise ValueError(r"must validate the regular expression /^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/")
        return value

    @field_validator('pep_host')
    def pep_host_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$", value):
            raise ValueError(r"must validate the regular expression /^$|^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$/")
        return value

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
#            self.auth_method =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.auth_method =  self.link_based_request("auth_method", "GET", return_type="Params")
#        return self.auth_method
#
#    @rest_auth_method.setter
#    def rest_auth_method(self, value):
#        self.auth_method = value

#    @property
#    def rest_auth_profile_params(self):
#        if self.auth_profile_params is not None:
#            return self.auth_profile_params
#        field_info = self.__class__.__fields__["auth_profile_params"]
#        try:
#            self.auth_profile_params =  self.link_based_request(field_info.alias, "GET", return_type="List[Params]")
#        except LinkNameException as e:
#            self.auth_profile_params =  self.link_based_request("auth_profile_params", "GET", return_type="List[Params]")
#        return self.auth_profile_params
#
#    @rest_auth_profile_params.setter
#    def rest_auth_profile_params(self, value):
#        self.auth_profile_params = value

#    @property
#    def rest_auth_profile_type(self):
#        if self.auth_profile_type is not None:
#            return self.auth_profile_type
#        field_info = self.__class__.__fields__["auth_profile_type"]
#        try:
#            self.auth_profile_type =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.auth_profile_type =  self.link_based_request("auth_profile_type", "GET", return_type="str")
#        return self.auth_profile_type
#
#    @rest_auth_profile_type.setter
#    def rest_auth_profile_type(self, value):
#        self.auth_profile_type = value

#    @property
#    def rest_hostname_suffix(self):
#        if self.hostname_suffix is not None:
#            return self.hostname_suffix
#        field_info = self.__class__.__fields__["hostname_suffix"]
#        try:
#            self.hostname_suffix =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.hostname_suffix =  self.link_based_request("hostname_suffix", "GET", return_type="str")
#        return self.hostname_suffix
#
#    @rest_hostname_suffix.setter
#    def rest_hostname_suffix(self, value):
#        self.hostname_suffix = value

#    @property
#    def rest_idp_type(self):
#        if self.idp_type is not None:
#            return self.idp_type
#        field_info = self.__class__.__fields__["idp_type"]
#        try:
#            self.idp_type =  self.link_based_request(field_info.alias, "GET", return_type="Params")
#        except LinkNameException as e:
#            self.idp_type =  self.link_based_request("idp_type", "GET", return_type="Params")
#        return self.idp_type
#
#    @rest_idp_type.setter
#    def rest_idp_type(self, value):
#        self.idp_type = value

#    @property
#    def rest_is_explicit_proxy(self):
#        if self.is_explicit_proxy is not None:
#            return self.is_explicit_proxy
#        field_info = self.__class__.__fields__["is_explicit_proxy"]
#        try:
#            self.is_explicit_proxy =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.is_explicit_proxy =  self.link_based_request("is_explicit_proxy", "GET", return_type="bool")
#        return self.is_explicit_proxy
#
#    @rest_is_explicit_proxy.setter
#    def rest_is_explicit_proxy(self, value):
#        self.is_explicit_proxy = value

#    @property
#    def rest_pep_host(self):
#        if self.pep_host is not None:
#            return self.pep_host
#        field_info = self.__class__.__fields__["pep_host"]
#        try:
#            self.pep_host =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.pep_host =  self.link_based_request("pep_host", "GET", return_type="str")
#        return self.pep_host
#
#    @rest_pep_host.setter
#    def rest_pep_host(self, value):
#        self.pep_host = value

#    @property
#    def rest_pep_port(self):
#        if self.pep_port is not None:
#            return self.pep_port
#        field_info = self.__class__.__fields__["pep_port"]
#        try:
#            self.pep_port =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.pep_port =  self.link_based_request("pep_port", "GET", return_type="int")
#        return self.pep_port
#
#    @rest_pep_port.setter
#    def rest_pep_port(self, value):
#        self.pep_port = value

#    @property
#    def rest_simulated_id_p(self):
#        if self.simulated_id_p is not None:
#            return self.simulated_id_p
#        field_info = self.__class__.__fields__["simulated_id_p"]
#        try:
#            self.simulated_id_p =  self.link_based_request(field_info.alias, "GET", return_type="SimulatedIdP")
#        except LinkNameException as e:
#            self.simulated_id_p =  self.link_based_request("simulated_id_p", "GET", return_type="SimulatedIdP")
#        return self.simulated_id_p
#
#    @rest_simulated_id_p.setter
#    def rest_simulated_id_p(self, value):
#        self.simulated_id_p = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PepDUT from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in auth_profile_params (list)
        _items = []
        if self.auth_profile_params:
            for _item in self.auth_profile_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['AuthProfileParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of idp_type
        if self.idp_type:
            _dict['IDPType'] = self.idp_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of simulated_id_p
        if self.simulated_id_p:
            _dict['SimulatedIdP'] = self.simulated_id_p.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PepDUT from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AuthMethod": Params.from_dict(obj["AuthMethod"]) if obj.get("AuthMethod") is not None else None,
                        "AuthProfileParams": [Params.from_dict(_item) for _item in obj["AuthProfileParams"]] if obj.get("AuthProfileParams") is not None else None,
                        "AuthProfileType": obj.get("AuthProfileType"),
                        "HostnameSuffix": obj.get("HostnameSuffix"),
                        "IDPType": Params.from_dict(obj["IDPType"]) if obj.get("IDPType") is not None else None,
                        "IsExplicitProxy": obj.get("IsExplicitProxy"),
                        "PEPHost": obj.get("PEPHost"),
                        "PEPPort": obj.get("PEPPort"),
                        "SimulatedIdP": SimulatedIdP.from_dict(obj["SimulatedIdP"]) if obj.get("SimulatedIdP") is not None else None
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
    


