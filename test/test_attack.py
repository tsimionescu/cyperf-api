# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.attack import Attack

class TestAttack(unittest.TestCase):
    """Attack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attack:
        """Test Attack
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attack`
        """
        model = Attack()
        if include_optional:
            return Attack(
                action_timeout = 56,
                active = True,
                client_http_profile = cyperf.models.http_profile.HTTPProfile(
                    additional_headers = null, 
                    connection_persistence = null, 
                    connections_max_transactions = 56, 
                    description = '', 
                    external_resource_url = '', 
                    http_version = null, 
                    headers = null, 
                    is_modified = True, 
                    name = '', 
                    params = [
                        cyperf.models.params.Params(
                            array_element_type = '', 
                            array_elements = [
                                {
                                    'key' : ''
                                    }
                                ], 
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
                            file_value = null, 
                            flow_identifier = True, 
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
                                            track_id = '', 
                                            track_type = null, 
                                            id = '', )
                                        ], 
                                    id = '', )
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
                            type = '', 
                            value = '', 
                            file_upload = [
                                'YQ=='
                                ], 
                            id = , 
                            supports_dynamic_payload = True, 
                            upload_url = '', )
                        ], 
                    use_application_server_headers = True, ),
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
                connections_max_transactions = 56,
                description = '',
                destination_hostname = '',
                dnn_id = '',
                end_point_id = 56,
                endpoints = [
                    cyperf.models.endpoint.Endpoint(
                        name = '', 
                        network_mapping = null, 
                        type = 'Client', 
                        id = '', )
                    ],
                external_resource_url = '',
                index = 56,
                inherit_http_profile = True,
                ip_preference = 'IPV4_ONLY',
                is_deprecated = True,
                iteration_count = 56,
                max_active_limit = 56,
                name = 'YBuLd',
                network_mapping = cyperf.models.network_mapping.NetworkMapping(
                    client_network_tags = [
                        ''
                        ], 
                    excluded_dut_list = [
                        ''
                        ], 
                    server_network_tags = [
                        ''
                        ], ),
                params = [
                    cyperf.models.params.Params(
                        array_element_type = '', 
                        array_elements = [
                            {
                                'key' : ''
                                }
                            ], 
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
                        file_value = null, 
                        flow_identifier = True, 
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
                                        track_id = '', 
                                        track_type = null, 
                                        id = '', )
                                    ], 
                                id = '', )
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
                        type = '', 
                        value = '', 
                        file_upload = [
                            'YQ=='
                            ], 
                        id = , 
                        supports_dynamic_payload = True, 
                        upload_url = '', )
                    ],
                protocol_id = '',
                qos_flow_id = '',
                readonly_max_trans = True,
                server_http_profile = cyperf.models.http_profile.HTTPProfile(
                    additional_headers = null, 
                    connection_persistence = null, 
                    connections_max_transactions = 56, 
                    description = '', 
                    external_resource_url = '', 
                    http_version = null, 
                    headers = null, 
                    is_modified = True, 
                    name = '', 
                    params = [
                        cyperf.models.params.Params(
                            array_element_type = '', 
                            array_elements = [
                                {
                                    'key' : ''
                                    }
                                ], 
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
                            file_value = null, 
                            flow_identifier = True, 
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
                                            track_id = '', 
                                            track_type = null, 
                                            id = '', )
                                        ], 
                                    id = '', )
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
                            type = '', 
                            value = '', 
                            file_upload = [
                                'YQ=='
                                ], 
                            id = , 
                            supports_dynamic_payload = True, 
                            upload_url = '', )
                        ], 
                    use_application_server_headers = True, ),
                supports_client_http_profile = True,
                supports_http_profiles = True,
                supports_server_http_profile = True,
                id = '',
                client_tls_profile = cyperf.models.tls_profile.TLSProfile(
                    certificate_file = null, 
                    cipher = null, 
                    cipher12 = null, 
                    cipher13 = null, 
                    ciphers12 = [
                        'ECDHE-RSA-AES256-GCM-SHA384'
                        ], 
                    ciphers13 = [
                        'AES-256-GCM-SHA384'
                        ], 
                    dh_file = null, 
                    get_tls_conflicts = [
                        'YQ=='
                        ], 
                    immediate_close = True, 
                    key_file = null, 
                    key_file_password = '', 
                    middle_box_enabled = True, 
                    profile_id = '', 
                    resolve_tls_conflicts = [
                        cyperf.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    send_close_notify = True, 
                    session_reuse_count = 56, 
                    session_reuse_method = null, 
                    session_reuse_method12 = null, 
                    session_reuse_method13 = null, 
                    sni_cert_configs = [
                        cyperf.models.cert_config.CertConfig(
                            certificate_file = null, 
                            dh_file = null, 
                            get_sni_conflicts = [
                                'YQ=='
                                ], 
                            id = '', 
                            is_playlist = True, 
                            key_file = null, 
                            key_file_password = '', 
                            playlist_column_name = '', 
                            playlist_filename = '', 
                            resolve_sni_conflicts = [
                                cyperf.models.conflict.Conflict(
                                    name = '', 
                                    path_to_target = '', 
                                    path_vars = {
                                        'key' : ''
                                        }, )
                                ], 
                            sni_hostname = '', )
                        ], 
                    sni_enabled = True, 
                    supported_groups13 = [
                        'P-256'
                        ], 
                    tls12_enabled = True, 
                    tls13_enabled = True, 
                    use_tls_profile = True, 
                    version = 'NONE', ),
                inherit_tls = True,
                server_tls_profile = cyperf.models.tls_profile.TLSProfile(
                    certificate_file = null, 
                    cipher = null, 
                    cipher12 = null, 
                    cipher13 = null, 
                    ciphers12 = [
                        'ECDHE-RSA-AES256-GCM-SHA384'
                        ], 
                    ciphers13 = [
                        'AES-256-GCM-SHA384'
                        ], 
                    dh_file = null, 
                    get_tls_conflicts = [
                        'YQ=='
                        ], 
                    immediate_close = True, 
                    key_file = null, 
                    key_file_password = '', 
                    middle_box_enabled = True, 
                    profile_id = '', 
                    resolve_tls_conflicts = [
                        cyperf.models.conflict.Conflict(
                            name = '', 
                            path_to_target = '', 
                            path_vars = {
                                'key' : ''
                                }, )
                        ], 
                    send_close_notify = True, 
                    session_reuse_count = 56, 
                    session_reuse_method = null, 
                    session_reuse_method12 = null, 
                    session_reuse_method13 = null, 
                    sni_cert_configs = [
                        cyperf.models.cert_config.CertConfig(
                            certificate_file = null, 
                            dh_file = null, 
                            get_sni_conflicts = [
                                'YQ=='
                                ], 
                            id = '', 
                            is_playlist = True, 
                            key_file = null, 
                            key_file_password = '', 
                            playlist_column_name = '', 
                            playlist_filename = '', 
                            resolve_sni_conflicts = [
                                cyperf.models.conflict.Conflict(
                                    name = '', 
                                    path_to_target = '', 
                                    path_vars = {
                                        'key' : ''
                                        }, )
                                ], 
                            sni_hostname = '', )
                        ], 
                    sni_enabled = True, 
                    supported_groups13 = [
                        'P-256'
                        ], 
                    tls12_enabled = True, 
                    tls13_enabled = True, 
                    use_tls_profile = True, 
                    version = 'NONE', ),
                supports_tls = True,
                tracks = [
                    cyperf.models.attack_track.AttackTrack(
                        actions = [
                            null
                            ], 
                        add_actions = [
                            'YQ=='
                            ], 
                        id = '', )
                    ],
                create = [
                    'YQ=='
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
                    ]
            )
        else:
            return Attack(
        )
        """

    def testAttack(self):
        """Test Attack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
