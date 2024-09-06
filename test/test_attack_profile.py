# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.attack_profile import AttackProfile

class TestAttackProfile(unittest.TestCase):
    """AttackProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttackProfile:
        """Test AttackProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttackProfile`
        """
        model = AttackProfile()
        if include_optional:
            return AttackProfile(
                active = True,
                traffic_settings = cyperf.models.traffic_settings.TrafficSettings(
                    default_transport_profile = null, ),
                id = '',
                attacks = [
                    null
                    ],
                default_network_mapping = cyperf.models.network_mapping.NetworkMapping(
                    client_network_tags = [
                        ''
                        ], 
                    excluded_dut_list = [
                        ''
                        ], 
                    server_network_tags = [
                        ''
                        ], ),
                name = '',
                objectives_and_timeline = cyperf.models.attack_objectives_and_timeline.AttackObjectivesAndTimeline(
                    timeline_segments = [
                        null
                        ], ),
                add_attacks = [
                    cyperf.models.external_resource_info.ExternalResourceInfo(
                        external_resource_url = '', )
                    ],
                modify_excluded_dut_recursively = [
                    cyperf.models.update_network_mapping.UpdateNetworkMapping(
                        client_network_tags = [
                            ''
                            ], 
                        excluded_dut_list = [
                            ''
                            ], 
                        select_tags = True, 
                        server_network_tags = [
                            ''
                            ], )
                    ],
                modify_tags_recursively = [
                    cyperf.models.update_network_mapping.UpdateNetworkMapping(
                        client_network_tags = [
                            ''
                            ], 
                        excluded_dut_list = [
                            ''
                            ], 
                        select_tags = True, 
                        server_network_tags = [
                            ''
                            ], )
                    ],
                reset_tags_to_default = [
                    'YQ=='
                    ]
            )
        else:
            return AttackProfile(
                name = '',
        )
        """

    def testAttackProfile(self):
        """Test AttackProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
