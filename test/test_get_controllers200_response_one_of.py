# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_controllers200_response_one_of import GetControllers200ResponseOneOf

class TestGetControllers200ResponseOneOf(unittest.TestCase):
    """GetControllers200ResponseOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetControllers200ResponseOneOf:
        """Test GetControllers200ResponseOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetControllers200ResponseOneOf`
        """
        model = GetControllers200ResponseOneOf()
        if include_optional:
            return GetControllers200ResponseOneOf(
                data = [
                    cyperf.models.controller.Controller(
                        compute_nodes = [
                            cyperf.models.compute_node.ComputeNode(
                                app_mode = cyperf.models.app_mode.AppMode(
                                    app_id = '', 
                                    ui_app_id = '', ), 
                                id = '', 
                                mode = '', 
                                name = '', 
                                ports = [
                                    cyperf.models.port.Port(
                                        disabled = True, 
                                        id = '', 
                                        name = '', 
                                        speed = '', )
                                    ], 
                                type = '', )
                            ], 
                        id = '', 
                        name = '', 
                        serial = '', 
                        type = '', )
                    ],
                total_count = 56
            )
        else:
            return GetControllers200ResponseOneOf(
        )
        """

    def testGetControllers200ResponseOneOf(self):
        """Test GetControllers200ResponseOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
