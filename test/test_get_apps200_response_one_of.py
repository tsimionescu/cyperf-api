# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_apps200_response_one_of import GetApps200ResponseOneOf

class TestGetApps200ResponseOneOf(unittest.TestCase):
    """GetApps200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApps200ResponseOneOf:
        """Test GetApps200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApps200ResponseOneOf`
        """
        model = GetApps200ResponseOneOf()
        if include_optional:
            return GetApps200ResponseOneOf(
                data = [
                    cyperf.models.appsec_app.AppsecApp(
                        app = null, 
                        description = '', 
                        name = '', 
                        static = True, 
                        user_defined = True, 
                        id = '', 
                        owner = '', 
                        owner_id = '', )
                    ],
                total_count = 56
            )
        else:
            return GetApps200ResponseOneOf(
        )
        """

    def testGetApps200ResponseOneOf(self):
        """Test GetApps200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
