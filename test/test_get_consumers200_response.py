# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_consumers200_response import GetConsumers200Response

class TestGetConsumers200Response(unittest.TestCase):
    """GetConsumers200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetConsumers200Response:
        """Test GetConsumers200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetConsumers200Response`
        """
        model = GetConsumers200Response()
        if include_optional:
            return GetConsumers200Response(
                data = [
                    cyperf.models.consumer.Consumer(
                        id = '', 
                        pretty_size = '', 
                        size = 56, )
                    ],
                total_count = 56
            )
        else:
            return GetConsumers200Response(
        )
        """

    def testGetConsumers200Response(self):
        """Test GetConsumers200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
