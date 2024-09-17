# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.connection import Connection

class TestConnection(unittest.TestCase):
    """Connection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Connection:
        """Test Connection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Connection`
        """
        model = Connection()
        if include_optional:
            return Connection(
                client_endpoint = '',
                client_port = 56,
                closing_end = '',
                disable_encryption = True,
                hostname = '',
                hostname_param = cyperf.models.params.Params(
                    array_elements = [
                        {
                            'key' : ''
                            }
                        ], 
                    array_element_type = '', 
                    category = '', 
                    category_index = 56, 
                    deprecated_previous_source = '', 
                    description = '', 
                    dictionary_value = {
                        'key' : ''
                        }, 
                    enum = cyperf.models.params_enum.Params_Enum(
                        choices = [
                            cyperf.models.choice.Choice(
                                description = '', 
                                hidden = True, 
                                name = '', 
                                value = '', )
                            ], ), 
                    file_upload = [
                        'YQ=='
                        ], 
                    file_value = null, 
                    flow_identifier = True, 
                    id = '', 
                    is_deprecated = True, 
                    is_modified = True, 
                    media_files = [
                        cyperf.models.media_file.MediaFile(
                            file_value = null, 
                            media_tracks = [
                                cyperf.models.media_track.MediaTrack(
                                    bitrate = 56, 
                                    bitrate_kbps = 56, 
                                    codec = '', 
                                    codec_description = '', 
                                    id = '', 
                                    track_id = '', 
                                    track_type = null, )
                                ], )
                        ], 
                    metadata = cyperf.models.param_metadata.ParamMetadata(
                        type_info = cyperf.models.param_metadata_type_info.ParamMetadata_TypeInfo(
                            array_v2 = cyperf.models.param_metadata_type_info_array_v2.ParamMetadata_TypeInfo_arrayV2(
                                elements = [
                                    cyperf.models.param_metadata_type_info_array_v2_elements_inner.ParamMetadata_TypeInfo_arrayV2_elements_inner(
                                        type = '', )
                                    ], ), 
                            int = cyperf.models.param_metadata_type_info_int.ParamMetadata_TypeInfo_int(
                                max_value = 56, 
                                min_value = 56, ), 
                            media = cyperf.models.param_metadata_type_info_media.ParamMetadata_TypeInfo_media(
                                track_id = '', 
                                track_type = '', ), 
                            string = cyperf.models.param_metadata_type_info_string.ParamMetadata_TypeInfo_string(
                                charset = '', 
                                max_length = 56, 
                                min_length = 56, ), ), ), 
                    name = '', 
                    param_id = '', 
                    readonly = True, 
                    source = '', 
                    supported_sources = [
                        ''
                        ], 
                    supports_dynamic_payload = True, 
                    type = '', 
                    upload_url = '', 
                    value = '', ),
                http_forward_proxy_mode = 'INHERIT_DUT',
                id = '',
                is_deprecated = True,
                max_transactions = 56,
                name = '',
                port_settings = cyperf.models.port_settings.PortSettings(
                    automatic = True, 
                    automatic_destination_port = True, 
                    automatic_forward_proxy_port = True, 
                    destination_port = 56, 
                    effective_ports = cyperf.models.effective_ports.EffectivePorts(), 
                    forward_proxy_port = 56, 
                    readonly = True, 
                    server_listen_port = 56, ),
                readonly = True,
                readonly_hostname = True,
                readonly_max_trans = True,
                readonly_type = True,
                server_endpoint = '',
                server_port = 56,
                type = 'http'
            )
        else:
            return Connection(
                client_endpoint = '',
                client_port = 56,
                id = '',
                max_transactions = 56,
                server_port = 56,
        )
        """

    def testConnection(self):
        """Test Connection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
