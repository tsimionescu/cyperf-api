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
from cyperf.models.track_type import TrackType
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "MediaTrack" != "APILink":
    from cyperf.models.api_link import APILink

class MediaTrack(BaseModel):
    """
    MediaTrack
    """ # noqa: E501
    bitrate: Optional[StrictInt] = Field(default=None, alias="Bitrate")
    bitrate_kbps: Optional[StrictInt] = Field(default=None, alias="BitrateKbps")
    codec: Optional[StrictStr] = Field(default=None, alias="Codec")
    codec_description: Optional[StrictStr] = Field(default=None, alias="CodecDescription")
    track_id: StrictStr = Field(alias="TrackId")
    track_type: TrackType = Field(alias="TrackType")
    id: StrictStr
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["Bitrate", "BitrateKbps", "Codec", "CodecDescription", "TrackId", "TrackType", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_bitrate(self):
#        if self.bitrate is not None:
#            return self.bitrate
#        field_info = self.__class__.__fields__["bitrate"]
#        try:
#            self.bitrate =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.bitrate =  self.link_based_request("bitrate", "GET", return_type="int")
#        return self.bitrate
#
#    @rest_bitrate.setter
#    def rest_bitrate(self, value):
#        self.bitrate = value

#    @property
#    def rest_bitrate_kbps(self):
#        if self.bitrate_kbps is not None:
#            return self.bitrate_kbps
#        field_info = self.__class__.__fields__["bitrate_kbps"]
#        try:
#            self.bitrate_kbps =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.bitrate_kbps =  self.link_based_request("bitrate_kbps", "GET", return_type="int")
#        return self.bitrate_kbps
#
#    @rest_bitrate_kbps.setter
#    def rest_bitrate_kbps(self, value):
#        self.bitrate_kbps = value

#    @property
#    def rest_codec(self):
#        if self.codec is not None:
#            return self.codec
#        field_info = self.__class__.__fields__["codec"]
#        try:
#            self.codec =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.codec =  self.link_based_request("codec", "GET", return_type="str")
#        return self.codec
#
#    @rest_codec.setter
#    def rest_codec(self, value):
#        self.codec = value

#    @property
#    def rest_codec_description(self):
#        if self.codec_description is not None:
#            return self.codec_description
#        field_info = self.__class__.__fields__["codec_description"]
#        try:
#            self.codec_description =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.codec_description =  self.link_based_request("codec_description", "GET", return_type="str")
#        return self.codec_description
#
#    @rest_codec_description.setter
#    def rest_codec_description(self, value):
#        self.codec_description = value

#    @property
#    def rest_track_id(self):
#        if self.track_id is not None:
#            return self.track_id
#        field_info = self.__class__.__fields__["track_id"]
#        try:
#            self.track_id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.track_id =  self.link_based_request("track_id", "GET", return_type="str")
#        return self.track_id
#
#    @rest_track_id.setter
#    def rest_track_id(self, value):
#        self.track_id = value

#    @property
#    def rest_track_type(self):
#        if self.track_type is not None:
#            return self.track_type
#        field_info = self.__class__.__fields__["track_type"]
#        try:
#            self.track_type =  self.link_based_request(field_info.alias, "GET", return_type="TrackType")
#        except LinkNameException as e:
#            self.track_type =  self.link_based_request("track_type", "GET", return_type="TrackType")
#        return self.track_type
#
#    @rest_track_type.setter
#    def rest_track_type(self, value):
#        self.track_type = value

#    @property
#    def rest_id(self):
#        if self.id is not None:
#            return self.id
#        field_info = self.__class__.__fields__["id"]
#        try:
#            self.id =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.id =  self.link_based_request("id", "GET", return_type="str")
#        return self.id
#
#    @rest_id.setter
#    def rest_id(self, value):
#        self.id = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MediaTrack from a JSON string"""
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
        """Create an instance of MediaTrack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "Bitrate": obj.get("Bitrate"),
                        "BitrateKbps": obj.get("BitrateKbps"),
                        "Codec": obj.get("Codec"),
                        "CodecDescription": obj.get("CodecDescription"),
                        "TrackId": obj.get("TrackId"),
                        "TrackType": obj.get("TrackType"),
                        "id": obj.get("id")
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
    


