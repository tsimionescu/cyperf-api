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
from typing import Any, ClassVar, Dict, List
from cyperf.models.mos_mode import MosMode
from cyperf.models.rtp_encryption_mode import RTPEncryptionMode
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "RTPProfile" != "APILink":
    from cyperf.models.api_link import APILink

class RTPProfile(BaseModel):
    """
    RTPProfile
    """ # noqa: E501
    encryption_mode: RTPEncryptionMode = Field(alias="EncryptionMode")
    mos_mode: MosMode = Field(alias="MosMode")
    profile_id: StrictStr = Field(description="The ID of the RTP profile (default: VoiceProfile).", alias="ProfileId")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["EncryptionMode", "MosMode", "ProfileId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_encryption_mode(self):
#        if self.encryption_mode is not None:
#            return self.encryption_mode
#        field_info = self.__class__.__fields__["encryption_mode"]
#        try:
#            self.encryption_mode =  self.link_based_request(field_info.alias, "GET", return_type="RTPEncryptionMode")
#        except LinkNameException as e:
#            self.encryption_mode =  self.link_based_request("encryption_mode", "GET", return_type="RTPEncryptionMode")
#        return self.encryption_mode
#
#    @rest_encryption_mode.setter
#    def rest_encryption_mode(self, value):
#        self.encryption_mode = value

#    @property
#    def rest_mos_mode(self):
#        if self.mos_mode is not None:
#            return self.mos_mode
#        field_info = self.__class__.__fields__["mos_mode"]
#        try:
#            self.mos_mode =  self.link_based_request(field_info.alias, "GET", return_type="MosMode")
#        except LinkNameException as e:
#            self.mos_mode =  self.link_based_request("mos_mode", "GET", return_type="MosMode")
#        return self.mos_mode
#
#    @rest_mos_mode.setter
#    def rest_mos_mode(self, value):
#        self.mos_mode = value

#    @property
#    def rest_profile_id(self):
#        if self.profile_id is not None:
#            return self.profile_id
#        field_info = self.__class__.__fields__["profile_id"]
#        try:
#            self.profile_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.profile_id =  self.link_based_request("profile_id", "GET", return_type="str")
#        return self.profile_id
#
#    @rest_profile_id.setter
#    def rest_profile_id(self, value):
#        self.profile_id = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RTPProfile from a JSON string"""
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
        """Create an instance of RTPProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "EncryptionMode": obj.get("EncryptionMode"),
                        "MosMode": obj.get("MosMode"),
                        "ProfileId": obj.get("ProfileId")
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
    


