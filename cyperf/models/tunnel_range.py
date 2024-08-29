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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cyperf.models.cisco_any_connect_settings import CiscoAnyConnectSettings
from cyperf.models.dns_resolver import DNSResolver
from cyperf.models.f5_settings import F5Settings
from cyperf.models.fortinet_settings import FortinetSettings
from cyperf.models.pangp_settings import PANGPSettings
from typing import Optional, Set
from typing_extensions import Self

class TunnelRange(BaseModel):
    """
    The Tunnel Range assigned to the current test configuration
    """ # noqa: E501
    cisco_any_connect_settings: Optional[CiscoAnyConnectSettings] = Field(default=None, alias="CiscoAnyConnectSettings")
    dcp_request_timeout: Optional[StrictInt] = Field(default=None, alias="DCPRequestTimeout")
    dns_resolver: Optional[DNSResolver] = Field(default=None, alias="DNSResolver")
    f5_settings: Optional[F5Settings] = Field(default=None, alias="F5Settings")
    fortinet_settings: Optional[FortinetSettings] = Field(default=None, alias="FortinetSettings")
    pangp_settings: Optional[PANGPSettings] = Field(default=None, alias="PANGPSettings")
    tcp_dst_port: StrictInt = Field(alias="TcpDstPort")
    tunnel_count_per_outer_ip: StrictInt = Field(alias="TunnelCountPerOuterIP")
    tunnel_establishment_timeout: Optional[StrictInt] = Field(default=None, alias="TunnelEstablishmentTimeout")
    vendor_type: StrictStr = Field(alias="VendorType")
    __properties: ClassVar[List[str]] = ["CiscoAnyConnectSettings", "DCPRequestTimeout", "DNSResolver", "F5Settings", "FortinetSettings", "PANGPSettings", "TcpDstPort", "TunnelCountPerOuterIP", "TunnelEstablishmentTimeout", "VendorType"]

    @field_validator('vendor_type')
    def vendor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CISCO_ANY_CONNECT', 'PAN_GP', 'FORTINET', 'F5']):
            raise ValueError("must be one of enum values ('CISCO_ANY_CONNECT', 'PAN_GP', 'FORTINET', 'F5')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TunnelRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cisco_any_connect_settings
        if self.cisco_any_connect_settings:
            _dict['CiscoAnyConnectSettings'] = self.cisco_any_connect_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dns_resolver
        if self.dns_resolver:
            _dict['DNSResolver'] = self.dns_resolver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of f5_settings
        if self.f5_settings:
            _dict['F5Settings'] = self.f5_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fortinet_settings
        if self.fortinet_settings:
            _dict['FortinetSettings'] = self.fortinet_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pangp_settings
        if self.pangp_settings:
            _dict['PANGPSettings'] = self.pangp_settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TunnelRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CiscoAnyConnectSettings": CiscoAnyConnectSettings.from_dict(obj["CiscoAnyConnectSettings"]) if obj.get("CiscoAnyConnectSettings") is not None else None,
            "DCPRequestTimeout": obj.get("DCPRequestTimeout"),
            "DNSResolver": DNSResolver.from_dict(obj["DNSResolver"]) if obj.get("DNSResolver") is not None else None,
            "F5Settings": F5Settings.from_dict(obj["F5Settings"]) if obj.get("F5Settings") is not None else None,
            "FortinetSettings": FortinetSettings.from_dict(obj["FortinetSettings"]) if obj.get("FortinetSettings") is not None else None,
            "PANGPSettings": PANGPSettings.from_dict(obj["PANGPSettings"]) if obj.get("PANGPSettings") is not None else None,
            "TcpDstPort": obj.get("TcpDstPort"),
            "TunnelCountPerOuterIP": obj.get("TunnelCountPerOuterIP"),
            "TunnelEstablishmentTimeout": obj.get("TunnelEstablishmentTimeout"),
            "VendorType": obj.get("VendorType")
        })
        return _obj


