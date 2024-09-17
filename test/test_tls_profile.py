# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.tls_profile import TLSProfile

class TestTLSProfile(unittest.TestCase):
    """TLSProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TLSProfile:
        """Test TLSProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TLSProfile`
        """
        model = TLSProfile()
        if include_optional:
            return TLSProfile(
                certificate_file = cyperf.models.params.Params(
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
                cipher = 'ECDHE-RSA-AES256-GCM-SHA384',
                cipher12 = 'ECDHE-RSA-AES256-GCM-SHA384',
                cipher13 = 'AES-256-GCM-SHA384',
                ciphers12 = [
                    'ECDHE-RSA-AES256-GCM-SHA384'
                    ],
                ciphers13 = [
                    'AES-256-GCM-SHA384'
                    ],
                dh_file = cyperf.models.params.Params(
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
                get_tls_conflicts = [
                    'YQ=='
                    ],
                immediate_close = True,
                key_file = cyperf.models.params.Params(
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
                session_reuse_method = 'DISABLE',
                session_reuse_method12 = 'DISABLE',
                session_reuse_method13 = 'DISABLE',
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
                version = 'NONE'
            )
        else:
            return TLSProfile(
                profile_id = '',
                sni_enabled = True,
                tls12_enabled = True,
                version = 'NONE',
        )
        """

    def testTLSProfile(self):
        """Test TLSProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
