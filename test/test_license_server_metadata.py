# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.license_server_metadata import LicenseServerMetadata

class TestLicenseServerMetadata(unittest.TestCase):
    """LicenseServerMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LicenseServerMetadata:
        """Test LicenseServerMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LicenseServerMetadata`
        """
        model = LicenseServerMetadata()
        if include_optional:
            return LicenseServerMetadata(
                connection_status = '',
                fingerprint = '',
                host_name = '',
                id = 56,
                interactive_fingerprint_verification = True,
                password = '',
                pretty_conn_status = '',
                trust_new = True,
                tunnel_host_name = '',
                user = ''
            )
        else:
            return LicenseServerMetadata(
        )
        """

    def testLicenseServerMetadata(self):
        """Test LicenseServerMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
