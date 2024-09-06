# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.category import Category

class TestCategory(unittest.TestCase):
    """Category unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Category:
        """Test Category
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Category`
        """
        model = Category()
        if include_optional:
            return Category(
                index = 56,
                name = '',
                values = [
                    cyperf.models.category_value.CategoryValue(
                        items_count = 56, 
                        value = '', )
                    ]
            )
        else:
            return Category(
        )
        """

    def testCategory(self):
        """Test Category"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
