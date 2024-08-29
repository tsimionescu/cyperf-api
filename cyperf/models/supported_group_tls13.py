# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SupportedGroupTLS13(str, Enum):
    """
    The TLSv1.3 supported groups (default: P-256).
    """

    """
    allowed enum values
    """
    P_MINUS_256 = 'P-256'
    P_MINUS_384 = 'P-384'
    P_MINUS_521 = 'P-521'
    X25519_KYBER768 = 'X25519_KYBER768'
    X25519_KYBER512 = 'X25519_KYBER512'
    X25519_MLKEM512 = 'X25519_MLKEM512'
    X25519_MLKEM768 = 'X25519_MLKEM768'
    KYBER768 = 'KYBER768'
    MLKEM768 = 'MLKEM768'
    KYBER512 = 'KYBER512'
    MLKEM512 = 'MLKEM512'
    KYBER1024 = 'KYBER1024'
    MLKEM1024 = 'MLKEM1024'
    P384_KYBER768 = 'P384_KYBER768'
    P256_KYBER512 = 'P256_KYBER512'
    P384_MLKEM1024 = 'P384_MLKEM1024'
    X448_MLKEM768 = 'X448_MLKEM768'
    P384_MLKEM768 = 'P384_MLKEM768'
    P256_MLKEM768 = 'P256_MLKEM768'
    P256_MLKEM512 = 'P256_MLKEM512'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SupportedGroupTLS13 from a JSON string"""
        return cls(json.loads(json_str))


