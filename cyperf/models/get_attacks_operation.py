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
from cyperf.models.category_filter import CategoryFilter
from cyperf.models.sort_body_field import SortBodyField
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "GetAttacksOperation" != "APILink":
    from cyperf.models.api_link import APILink

class GetAttacksOperation(BaseModel):
    """
    GetAttacksOperation
    """ # noqa: E501
    categories: Optional[List[CategoryFilter]] = None
    filter_mode: Optional[StrictStr] = Field(default=None, alias="filterMode")
    search_col: Optional[List[StrictStr]] = Field(default=None, alias="searchCol")
    search_val: Optional[List[StrictStr]] = Field(default=None, alias="searchVal")
    skip: Optional[StrictStr] = None
    sort: Optional[List[SortBodyField]] = None
    take: Optional[StrictStr] = None
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["categories", "filterMode", "searchCol", "searchVal", "skip", "sort", "take"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_categories(self):
#        if self.categories is not None:
#            return self.categories
#        field_info = self.__class__.__fields__["categories"]
#        try:
#            self.categories =  self.link_based_request(field_info.alias, "GET", return_type="List[CategoryFilter]")
#        except LinkNameException as e:
#            self.categories =  self.link_based_request("categories", "GET", return_type="List[CategoryFilter]")
#        return self.categories
#
#    @rest_categories.setter
#    def rest_categories(self, value):
#        self.categories = value

#    @property
#    def rest_filter_mode(self):
#        if self.filter_mode is not None:
#            return self.filter_mode
#        field_info = self.__class__.__fields__["filter_mode"]
#        try:
#            self.filter_mode =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.filter_mode =  self.link_based_request("filter_mode", "GET", return_type="str")
#        return self.filter_mode
#
#    @rest_filter_mode.setter
#    def rest_filter_mode(self, value):
#        self.filter_mode = value

#    @property
#    def rest_search_col(self):
#        if self.search_col is not None:
#            return self.search_col
#        field_info = self.__class__.__fields__["search_col"]
#        try:
#            self.search_col =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.search_col =  self.link_based_request("search_col", "GET", return_type="List[str]")
#        return self.search_col
#
#    @rest_search_col.setter
#    def rest_search_col(self, value):
#        self.search_col = value

#    @property
#    def rest_search_val(self):
#        if self.search_val is not None:
#            return self.search_val
#        field_info = self.__class__.__fields__["search_val"]
#        try:
#            self.search_val =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.search_val =  self.link_based_request("search_val", "GET", return_type="List[str]")
#        return self.search_val
#
#    @rest_search_val.setter
#    def rest_search_val(self, value):
#        self.search_val = value

#    @property
#    def rest_skip(self):
#        if self.skip is not None:
#            return self.skip
#        field_info = self.__class__.__fields__["skip"]
#        try:
#            self.skip =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.skip =  self.link_based_request("skip", "GET", return_type="str")
#        return self.skip
#
#    @rest_skip.setter
#    def rest_skip(self, value):
#        self.skip = value

#    @property
#    def rest_sort(self):
#        if self.sort is not None:
#            return self.sort
#        field_info = self.__class__.__fields__["sort"]
#        try:
#            self.sort =  self.link_based_request(field_info.alias, "GET", return_type="List[SortBodyField]")
#        except LinkNameException as e:
#            self.sort =  self.link_based_request("sort", "GET", return_type="List[SortBodyField]")
#        return self.sort
#
#    @rest_sort.setter
#    def rest_sort(self, value):
#        self.sort = value

#    @property
#    def rest_take(self):
#        if self.take is not None:
#            return self.take
#        field_info = self.__class__.__fields__["take"]
#        try:
#            self.take =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.take =  self.link_based_request("take", "GET", return_type="str")
#        return self.take
#
#    @rest_take.setter
#    def rest_take(self, value):
#        self.take = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetAttacksOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sort (list)
        _items = []
        if self.sort:
            for _item in self.sort:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sort'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetAttacksOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "categories": [CategoryFilter.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
                        "filterMode": obj.get("filterMode"),
                        "searchCol": obj.get("searchCol"),
                        "searchVal": obj.get("searchVal"),
                        "skip": obj.get("skip"),
                        "sort": [SortBodyField.from_dict(_item) for _item in obj["sort"]] if obj.get("sort") is not None else None,
                        "take": obj.get("take")
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
    


