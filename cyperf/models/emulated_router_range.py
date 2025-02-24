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
from cyperf.models.automatic_ip_type import AutomaticIpType
from cyperf.models.ip_ver import IpVer
from cyperf.models.vlan_range import VLANRange
from typing import Optional, Set, Union, GenericAlias, get_args
from typing_extensions import Self
from pydantic import Field
#from cyperf.models import LinkNameException

if "EmulatedRouterRange" != "APILink":
    from cyperf.models.api_link import APILink

class EmulatedRouterRange(BaseModel):
    """
    EmulatedRouterRange
    """ # noqa: E501
    automatic_ip_type: Optional[AutomaticIpType] = Field(default=None, description="The automatic IP types, either 'ONLY_IPV4', 'ONLY_IPV6' or 'BOTH_IPV4_IPV6'.", alias="AutomaticIpType")
    count: Optional[StrictInt] = Field(default=None, description="The number of IPs generated (default: 1).", alias="Count")
    gw_auto: StrictBool = Field(description="A flag indicating if the gateway settings for the IPRange should be determined automatically (default: true).", alias="GwAuto")
    gw_start: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The gateway start IP for the IPRange (default: 10.0.0.1).", alias="GwStart")
    inner_vlan_range: Optional[VLANRange] = Field(default=None, description="The inner VLAN range assigned to the current IP range configuration", alias="InnerVlanRange")
    ip_auto: StrictBool = Field(description="A flag indicating if IP settings for the IPRange should be determined automatically (default: true).", alias="IpAuto")
    ip_incr: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The IP incrementation rule (default: 0.0.0.1).", alias="IpIncr")
    ip_range_name: Annotated[str, Field(strict=True)] = Field(alias="IpRangeName")
    ip_start: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The start IP for the IPRange (default: 10.0.0.10).", alias="IpStart")
    ip_ver: IpVer = Field(description="The type of the IP. 'IPV4' and 'IPV6' are both supported currently.", alias="IpVer")
    is_emulated_router: Optional[StrictBool] = Field(default=None, alias="IsEmulatedRouter")
    mss: StrictInt = Field(description="The maximum segment size of the TCP header.", alias="Mss")
    mss_auto: StrictBool = Field(description="A flag indicating if Mss settings for the IPRange should be determined automatically (default: false).", alias="MssAuto")
    net_mask: Optional[StrictInt] = Field(default=None, description="The network mask of the IP Range (default: 16).", alias="NetMask")
    net_mask_auto: StrictBool = Field(description="A flag indicating if the network mask of the IPRange should be determined automatically (default: true).", alias="NetMaskAuto")
    id: StrictStr
    max_count_per_agent: Optional[StrictInt] = Field(default=None, description="The maximum number of IPs that should be assigned to each traffic agent for this IP range segment in a valid test (default: 1).", alias="maxCountPerAgent")
    network_tags: Optional[List[StrictStr]] = Field(default=None, description="A list of tags.", alias="networkTags")
    links: Optional[List[APILink]] = Field(default=None, description="Links to other properties")
#    api_client: Optional[Any] = None
    __properties: ClassVar[List[str]] = ["AutomaticIpType", "Count", "GwAuto", "GwStart", "InnerVlanRange", "IpAuto", "IpIncr", "IpRangeName", "IpStart", "IpVer", "IsEmulatedRouter", "Mss", "MssAuto", "NetMask", "NetMaskAuto", "id", "maxCountPerAgent", "networkTags"]

    @field_validator('gw_start')
    def gw_start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('ip_incr')
    def ip_incr_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    @field_validator('ip_range_name')
    def ip_range_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^$|^[^\"\\]+$", value):
            raise ValueError(r"must validate the regular expression /^$|^[^\"\\]+$/")
        return value

    @field_validator('ip_start')
    def ip_start_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$", value):
            raise ValueError(r"must validate the regular expression /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))|(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(([0-9a-fA-F]{1,4}:){5,5}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}|([0-9a-fA-F]{1,4}:){1,4}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){2,2}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){3,3}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){4,4})|:(:[0-9a-fA-F]{1,4}){1,5}):((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


#    @property
#    def rest_automatic_ip_type(self):
#        if self.automatic_ip_type is not None:
#            return self.automatic_ip_type
#        field_info = self.__class__.__fields__["automatic_ip_type"]
#        try:
#            self.automatic_ip_type =  self.link_based_request(field_info.alias, "GET", return_type="AutomaticIpType")
#        except LinkNameException as e:
#            self.automatic_ip_type =  self.link_based_request("automatic_ip_type", "GET", return_type="AutomaticIpType")
#        return self.automatic_ip_type
#
#    @rest_automatic_ip_type.setter
#    def rest_automatic_ip_type(self, value):
#        self.automatic_ip_type = value

#    @property
#    def rest_count(self):
#        if self.count is not None:
#            return self.count
#        field_info = self.__class__.__fields__["count"]
#        try:
#            self.count =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.count =  self.link_based_request("count", "GET", return_type="int")
#        return self.count
#
#    @rest_count.setter
#    def rest_count(self, value):
#        self.count = value

#    @property
#    def rest_gw_auto(self):
#        if self.gw_auto is not None:
#            return self.gw_auto
#        field_info = self.__class__.__fields__["gw_auto"]
#        try:
#            self.gw_auto =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.gw_auto =  self.link_based_request("gw_auto", "GET", return_type="bool")
#        return self.gw_auto
#
#    @rest_gw_auto.setter
#    def rest_gw_auto(self, value):
#        self.gw_auto = value

#    @property
#    def rest_gw_start(self):
#        if self.gw_start is not None:
#            return self.gw_start
#        field_info = self.__class__.__fields__["gw_start"]
#        try:
#            self.gw_start =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.gw_start =  self.link_based_request("gw_start", "GET", return_type="str")
#        return self.gw_start
#
#    @rest_gw_start.setter
#    def rest_gw_start(self, value):
#        self.gw_start = value

#    @property
#    def rest_inner_vlan_range(self):
#        if self.inner_vlan_range is not None:
#            return self.inner_vlan_range
#        field_info = self.__class__.__fields__["inner_vlan_range"]
#        try:
#            self.inner_vlan_range =  self.link_based_request(field_info.alias, "GET", return_type="VLANRange")
#        except LinkNameException as e:
#            self.inner_vlan_range =  self.link_based_request("inner_vlan_range", "GET", return_type="VLANRange")
#        return self.inner_vlan_range
#
#    @rest_inner_vlan_range.setter
#    def rest_inner_vlan_range(self, value):
#        self.inner_vlan_range = value

#    @property
#    def rest_ip_auto(self):
#        if self.ip_auto is not None:
#            return self.ip_auto
#        field_info = self.__class__.__fields__["ip_auto"]
#        try:
#            self.ip_auto =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.ip_auto =  self.link_based_request("ip_auto", "GET", return_type="bool")
#        return self.ip_auto
#
#    @rest_ip_auto.setter
#    def rest_ip_auto(self, value):
#        self.ip_auto = value

#    @property
#    def rest_ip_incr(self):
#        if self.ip_incr is not None:
#            return self.ip_incr
#        field_info = self.__class__.__fields__["ip_incr"]
#        try:
#            self.ip_incr =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.ip_incr =  self.link_based_request("ip_incr", "GET", return_type="str")
#        return self.ip_incr
#
#    @rest_ip_incr.setter
#    def rest_ip_incr(self, value):
#        self.ip_incr = value

#    @property
#    def rest_ip_range_name(self):
#        if self.ip_range_name is not None:
#            return self.ip_range_name
#        field_info = self.__class__.__fields__["ip_range_name"]
#        try:
#            self.ip_range_name =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.ip_range_name =  self.link_based_request("ip_range_name", "GET", return_type="str")
#        return self.ip_range_name
#
#    @rest_ip_range_name.setter
#    def rest_ip_range_name(self, value):
#        self.ip_range_name = value

#    @property
#    def rest_ip_start(self):
#        if self.ip_start is not None:
#            return self.ip_start
#        field_info = self.__class__.__fields__["ip_start"]
#        try:
#            self.ip_start =  self.link_based_request(field_info.alias, "GET", return_type="str")
#        except LinkNameException as e:
#            self.ip_start =  self.link_based_request("ip_start", "GET", return_type="str")
#        return self.ip_start
#
#    @rest_ip_start.setter
#    def rest_ip_start(self, value):
#        self.ip_start = value

#    @property
#    def rest_ip_ver(self):
#        if self.ip_ver is not None:
#            return self.ip_ver
#        field_info = self.__class__.__fields__["ip_ver"]
#        try:
#            self.ip_ver =  self.link_based_request(field_info.alias, "GET", return_type="IpVer")
#        except LinkNameException as e:
#            self.ip_ver =  self.link_based_request("ip_ver", "GET", return_type="IpVer")
#        return self.ip_ver
#
#    @rest_ip_ver.setter
#    def rest_ip_ver(self, value):
#        self.ip_ver = value

#    @property
#    def rest_is_emulated_router(self):
#        if self.is_emulated_router is not None:
#            return self.is_emulated_router
#        field_info = self.__class__.__fields__["is_emulated_router"]
#        try:
#            self.is_emulated_router =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.is_emulated_router =  self.link_based_request("is_emulated_router", "GET", return_type="bool")
#        return self.is_emulated_router
#
#    @rest_is_emulated_router.setter
#    def rest_is_emulated_router(self, value):
#        self.is_emulated_router = value

#    @property
#    def rest_mss(self):
#        if self.mss is not None:
#            return self.mss
#        field_info = self.__class__.__fields__["mss"]
#        try:
#            self.mss =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.mss =  self.link_based_request("mss", "GET", return_type="int")
#        return self.mss
#
#    @rest_mss.setter
#    def rest_mss(self, value):
#        self.mss = value

#    @property
#    def rest_mss_auto(self):
#        if self.mss_auto is not None:
#            return self.mss_auto
#        field_info = self.__class__.__fields__["mss_auto"]
#        try:
#            self.mss_auto =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.mss_auto =  self.link_based_request("mss_auto", "GET", return_type="bool")
#        return self.mss_auto
#
#    @rest_mss_auto.setter
#    def rest_mss_auto(self, value):
#        self.mss_auto = value

#    @property
#    def rest_net_mask(self):
#        if self.net_mask is not None:
#            return self.net_mask
#        field_info = self.__class__.__fields__["net_mask"]
#        try:
#            self.net_mask =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.net_mask =  self.link_based_request("net_mask", "GET", return_type="int")
#        return self.net_mask
#
#    @rest_net_mask.setter
#    def rest_net_mask(self, value):
#        self.net_mask = value

#    @property
#    def rest_net_mask_auto(self):
#        if self.net_mask_auto is not None:
#            return self.net_mask_auto
#        field_info = self.__class__.__fields__["net_mask_auto"]
#        try:
#            self.net_mask_auto =  self.link_based_request(field_info.alias, "GET", return_type="bool")
#        except LinkNameException as e:
#            self.net_mask_auto =  self.link_based_request("net_mask_auto", "GET", return_type="bool")
#        return self.net_mask_auto
#
#    @rest_net_mask_auto.setter
#    def rest_net_mask_auto(self, value):
#        self.net_mask_auto = value

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

#    @property
#    def rest_max_count_per_agent(self):
#        if self.max_count_per_agent is not None:
#            return self.max_count_per_agent
#        field_info = self.__class__.__fields__["max_count_per_agent"]
#        try:
#            self.max_count_per_agent =  self.link_based_request(field_info.alias, "GET", return_type="int")
#        except LinkNameException as e:
#            self.max_count_per_agent =  self.link_based_request("max_count_per_agent", "GET", return_type="int")
#        return self.max_count_per_agent
#
#    @rest_max_count_per_agent.setter
#    def rest_max_count_per_agent(self, value):
#        self.max_count_per_agent = value

#    @property
#    def rest_network_tags(self):
#        if self.network_tags is not None:
#            return self.network_tags
#        field_info = self.__class__.__fields__["network_tags"]
#        try:
#            self.network_tags =  self.link_based_request(field_info.alias, "GET", return_type="List[str]")
#        except LinkNameException as e:
#            self.network_tags =  self.link_based_request("network_tags", "GET", return_type="List[str]")
#        return self.network_tags
#
#    @rest_network_tags.setter
#    def rest_network_tags(self, value):
#        self.network_tags = value



    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EmulatedRouterRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inner_vlan_range
        if self.inner_vlan_range:
            _dict['InnerVlanRange'] = self.inner_vlan_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmulatedRouterRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            _obj = cls.model_validate(obj)
#            _obj.api_client = client
            return _obj

        _obj = cls.model_validate({
            "AutomaticIpType": obj.get("AutomaticIpType"),
                        "Count": obj.get("Count"),
                        "GwAuto": obj.get("GwAuto"),
                        "GwStart": obj.get("GwStart"),
                        "InnerVlanRange": VLANRange.from_dict(obj["InnerVlanRange"]) if obj.get("InnerVlanRange") is not None else None,
                        "IpAuto": obj.get("IpAuto"),
                        "IpIncr": obj.get("IpIncr"),
                        "IpRangeName": obj.get("IpRangeName"),
                        "IpStart": obj.get("IpStart"),
                        "IpVer": obj.get("IpVer"),
                        "IsEmulatedRouter": obj.get("IsEmulatedRouter"),
                        "Mss": obj.get("Mss"),
                        "MssAuto": obj.get("MssAuto"),
                        "NetMask": obj.get("NetMask"),
                        "NetMaskAuto": obj.get("NetMaskAuto"),
                        "id": obj.get("id"),
                        "maxCountPerAgent": obj.get("maxCountPerAgent"),
                        "networkTags": obj.get("networkTags")
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
    


