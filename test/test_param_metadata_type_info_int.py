# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.param_metadata_type_info_int import ParamMetadataTypeInfoInt

class TestParamMetadataTypeInfoInt(unittest.TestCase):
    """ParamMetadataTypeInfoInt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParamMetadataTypeInfoInt:
        """Test ParamMetadataTypeInfoInt
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParamMetadataTypeInfoInt`
        """
        model = ParamMetadataTypeInfoInt()
        if include_optional:
            return ParamMetadataTypeInfoInt(
                max_value = 56,
                min_value = 56
            )
        else:
            return ParamMetadataTypeInfoInt(
        )
        """

    def testParamMetadataTypeInfoInt(self):
        """Test ParamMetadataTypeInfoInt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
