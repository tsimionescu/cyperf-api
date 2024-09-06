# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.tunnel_stack import TunnelStack

class TestTunnelStack(unittest.TestCase):
    """TunnelStack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TunnelStack:
        """Test TunnelStack
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TunnelStack`
        """
        model = TunnelStack()
        if include_optional:
            return TunnelStack(
                inner_ip_range = cyperf.models.inner_ip_range.InnerIPRange(
                    network_tags = [
                        ''
                        ], ),
                outer_ip_range = cyperf.models.ip_range.IPRange(
                    automatic_ip_type = null, 
                    count = 56, 
                    gw_auto = True, 
                    gw_start = '::02:84:9:0cc0:F:CCf', 
                    inner_vlan_range = null, 
                    ip_auto = True, 
                    ip_incr = '::02:84:9:0cc0:F:CCf', 
                    ip_range_name = 'YBuLd', 
                    ip_start = '::02:84:9:0cc0:F:CCf', 
                    ip_ver = null, 
                    is_emulated_router = True, 
                    mss = 56, 
                    mss_auto = True, 
                    net_mask = 56, 
                    net_mask_auto = True, 
                    id = '', 
                    max_count_per_agent = 56, 
                    network_tags = [
                        ''
                        ], ),
                tunnel_range = cyperf.models.tunnel_range.TunnelRange(
                    cisco_any_connect_settings = null, 
                    dcp_request_timeout = 56, 
                    dns_resolver = null, 
                    f5_settings = null, 
                    fortinet_settings = null, 
                    pangp_settings = null, 
                    tcp_dst_port = 56, 
                    tunnel_count_per_outer_ip = 56, 
                    tunnel_establishment_timeout = 56, 
                    vendor_type = 'CISCO_ANY_CONNECT', ),
                tunnel_stack_name = 'YBuLd',
                id = ''
            )
        else:
            return TunnelStack(
                tunnel_stack_name = 'YBuLd',
                id = '',
        )
        """

    def testTunnelStack(self):
        """Test TunnelStack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
