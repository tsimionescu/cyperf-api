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
from typing import Any, ClassVar, Dict, List
from cyperf.models.enc_p2_algorithm import EncP2Algorithm
from cyperf.models.hash_p2_algorithm import HashP2Algorithm
from cyperf.models.pfs_p2_group import PfsP2Group
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "P2Config" != "APILink":
    from cyperf.models.api_link import APILink

class P2Config(BaseModel):
    """
    P2Config
    """ # noqa: E501
    enc_algorithm: EncP2Algorithm = Field(alias="EncAlgorithm")
    hash_algorithm: HashP2Algorithm = Field(alias="HashAlgorithm")
    lifetime: StrictInt = Field(alias="Lifetime")
    nat_enabled: StrictBool = Field(alias="NatEnabled")
    pfs_enabled: StrictBool = Field(alias="PfsEnabled")
    pfs_group: PfsP2Group = Field(alias="PfsGroup")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["EncAlgorithm", "HashAlgorithm", "Lifetime", "NatEnabled", "PfsEnabled", "PfsGroup"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_enc_algorithm(self):
#        if self.enc_algorithm is not None:
#            return self.enc_algorithm
#        field_info = self.__class__.__fields__["enc_algorithm"]
#        try:
#            self.enc_algorithm =  self.link_based_request(field_info.alias, "GET", return_type="EncP2Algorithm")
#        except LinkNameException as e:
#            self.enc_algorithm =  self.link_based_request("enc_algorithm", "GET", return_type="EncP2Algorithm")
#        return self.enc_algorithm
#
#    @rest_enc_algorithm.setter
#    def rest_enc_algorithm(self, value):
#        self.enc_algorithm = value

#    @property
#    def rest_hash_algorithm(self):
#        if self.hash_algorithm is not None:
#            return self.hash_algorithm
#        field_info = self.__class__.__fields__["hash_algorithm"]
#        try:
#            self.hash_algorithm =  self.link_based_request(field_info.alias, "GET", return_type="HashP2Algorithm")
#        except LinkNameException as e:
#            self.hash_algorithm =  self.link_based_request("hash_algorithm", "GET", return_type="HashP2Algorithm")
#        return self.hash_algorithm
#
#    @rest_hash_algorithm.setter
#    def rest_hash_algorithm(self, value):
#        self.hash_algorithm = value

#    @property
#    def rest_lifetime(self):
#        if self.lifetime is not None:
#            return self.lifetime
#        field_info = self.__class__.__fields__["lifetime"]
#        try:
#            self.lifetime =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.lifetime =  self.link_based_request("lifetime", "GET", return_type="int")
#        return self.lifetime
#
#    @rest_lifetime.setter
#    def rest_lifetime(self, value):
#        self.lifetime = value

#    @property
#    def rest_nat_enabled(self):
#        if self.nat_enabled is not None:
#            return self.nat_enabled
#        field_info = self.__class__.__fields__["nat_enabled"]
#        try:
#            self.nat_enabled =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.nat_enabled =  self.link_based_request("nat_enabled", "GET", return_type="bool")
#        return self.nat_enabled
#
#    @rest_nat_enabled.setter
#    def rest_nat_enabled(self, value):
#        self.nat_enabled = value

#    @property
#    def rest_pfs_enabled(self):
#        if self.pfs_enabled is not None:
#            return self.pfs_enabled
#        field_info = self.__class__.__fields__["pfs_enabled"]
#        try:
#            self.pfs_enabled =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.pfs_enabled =  self.link_based_request("pfs_enabled", "GET", return_type="bool")
#        return self.pfs_enabled
#
#    @rest_pfs_enabled.setter
#    def rest_pfs_enabled(self, value):
#        self.pfs_enabled = value

#    @property
#    def rest_pfs_group(self):
#        if self.pfs_group is not None:
#            return self.pfs_group
#        field_info = self.__class__.__fields__["pfs_group"]
#        try:
#            self.pfs_group =  self.link_based_request(field_info.alias, "GET", return_type="PfsP2Group")
#        except LinkNameException as e:
#            self.pfs_group =  self.link_based_request("pfs_group", "GET", return_type="PfsP2Group")
#        return self.pfs_group
#
#    @rest_pfs_group.setter
#    def rest_pfs_group(self, value):
#        self.pfs_group = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of P2Config from a JSON string"""
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
        """Create an instance of P2Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "EncAlgorithm": obj.get("EncAlgorithm"),
                        "HashAlgorithm": obj.get("HashAlgorithm"),
                        "Lifetime": obj.get("Lifetime"),
                        "NatEnabled": obj.get("NatEnabled"),
                        "PfsEnabled": obj.get("PfsEnabled"),
                        "PfsGroup": obj.get("PfsGroup")
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
    


