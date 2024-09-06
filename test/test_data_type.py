# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.data_type import DataType

class TestDataType(unittest.TestCase):
    """DataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataType:
        """Test DataType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataType`
        """
        model = DataType()
        if include_optional:
            return DataType(
                values = [
                    cyperf.models.data_type_values_inner.DataType_Values_inner(
                        id = '', 
                        value_type = '', )
                    ],
                id = ''
            )
        else:
            return DataType(
        )
        """

    def testDataType(self):
        """Test DataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
