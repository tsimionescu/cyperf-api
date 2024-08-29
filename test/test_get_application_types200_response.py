# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.get_application_types200_response import GetApplicationTypes200Response

class TestGetApplicationTypes200Response(unittest.TestCase):
    """GetApplicationTypes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApplicationTypes200Response:
        """Test GetApplicationTypes200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApplicationTypes200Response`
        """
        model = GetApplicationTypes200Response()
        if include_optional:
            return GetApplicationTypes200Response(
                data = [
                    cyperf.models.application_type.ApplicationType(
                        commands = [
                            cyperf.models.command.Command(
                                action_id = '', 
                                description = '', 
                                exchanges = [
                                    cyperf.models.exchange.Exchange(
                                        client_endpoint = '', 
                                        name = '', 
                                        server_endpoint = '', 
                                        id = '', )
                                    ], 
                                is_strike = True, 
                                metadata = cyperf.models.metadata.Metadata(
                                    auth_method = cyperf.models.enum.Enum(
                                        choices = [
                                            cyperf.models.choice.Choice(
                                                description = '', 
                                                hidden = True, 
                                                name = '', 
                                                value = '', )
                                            ], 
                                        default = '', ), 
                                    explicit_proxy = True, 
                                    idp_type = cyperf.models.enum.Enum(
                                        default = '', ), 
                                    sgw_name = '', 
                                    sgw_type = '', 
                                    sgw_type_value = '', ), 
                                name = '', 
                                parameters = [
                                    cyperf.models.parameter.Parameter(
                                        default_array_elements = [
                                            {
                                                'key' : ''
                                                }
                                            ], 
                                        default_source = '', 
                                        default_value = '', 
                                        element_type = '', 
                                        sources = [
                                            ''
                                            ], 
                                        type = '', 
                                        field = '', 
                                        id = '', 
                                        operator = '', 
                                        query_param = '', )
                                    ], )
                            ], 
                        connections = [
                            cyperf.models.connection.Connection(
                                client_endpoint = '', 
                                client_port = 56, 
                                closing_end = '', 
                                disable_encryption = True, 
                                hostname = '', 
                                hostname_param = null, 
                                http_forward_proxy_mode = 'INHERIT_DUT', 
                                is_deprecated = True, 
                                max_transactions = 56, 
                                name = '', 
                                port_settings = null, 
                                readonly = True, 
                                readonly_hostname = True, 
                                readonly_max_trans = True, 
                                readonly_type = True, 
                                server_endpoint = '', 
                                server_port = 56, 
                                type = 'http', 
                                id = '', )
                            ], 
                        custom_stats = [
                            cyperf.models.custom_stat.CustomStat(
                                function = '', 
                                path = '', )
                            ], 
                        data_types = [
                            cyperf.models.data_type.DataType(
                                values = [
                                    cyperf.models.data_type_values_inner.DataType_Values_inner(
                                        id = '', 
                                        value_type = '', )
                                    ], 
                                id = '', )
                            ], 
                        definition = cyperf.models.definition.Definition(
                            xml = 'YQ==', ), 
                        description = '', 
                        endpoints = [
                            cyperf.models.endpoint.Endpoint(
                                name = '', 
                                network_mapping = null, 
                                type = 'Client', 
                                id = '', )
                            ], 
                        file_name = '', 
                        has_banner_command = True, 
                        md5_content = '', 
                        md5_metadata = '', 
                        metadata = cyperf.models.metadata.Metadata(
                            explicit_proxy = True, 
                            sgw_name = '', 
                            sgw_type = '', 
                            sgw_type_value = '', ), 
                        name = '', 
                        parameters = [
                            cyperf.models.parameter.Parameter(
                                default_source = '', 
                                default_value = '', 
                                element_type = '', 
                                type = '', 
                                field = '', 
                                id = '', 
                                operator = '', 
                                query_param = '', )
                            ], 
                        strikes = [
                            cyperf.models.command.Command(
                                action_id = '', 
                                description = '', 
                                is_strike = True, 
                                name = '', )
                            ], 
                        supports_calibration = True, 
                        supports_client_http_profile = True, 
                        supports_http_profiles = True, 
                        supports_server_http_profile = True, 
                        supports_strikes = True, 
                        supports_tls = True, 
                        id = '', )
                    ],
                total_count = 56
            )
        else:
            return GetApplicationTypes200Response(
        )
        """

    def testGetApplicationTypes200Response(self):
        """Test GetApplicationTypes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
