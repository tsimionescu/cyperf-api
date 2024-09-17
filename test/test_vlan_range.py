# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.vlan_range import VLANRange

class TestVLANRange(unittest.TestCase):
    """VLANRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VLANRange:
        """Test VLANRange
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VLANRange`
        """
        model = VLANRange()
        if include_optional:
            return VLANRange(
                count = 56,
                count_per_agent = 56,
                max_count_per_agent = 56,
                priority = 56,
                static_arp_table = [
                    cyperf.models.static_arp_entry.StaticARPEntry(
                        count = 56, 
                        id = '', 
                        remote_ip = '::02:84:9:0cc0:F:CCf', 
                        remote_ip_incr = '::02:84:9:0cc0:F:CCf', 
                        remote_mac = '2E-B0-08-29:0c:01', 
                        remote_mac_incr = '2E-B0-08-29:0c:01', 
                        static_arp_entry_name = 'YBuLd', )
                    ],
                tag_protocol_id = 33024,
                vlan_auto = True,
                vlan_enabled = True,
                vlan_id = 56,
                vlan_incr = 56
            )
        else:
            return VLANRange(
                vlan_auto = True,
        )
        """

    def testVLANRange(self):
        """Test VLANRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
