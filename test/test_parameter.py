# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.parameter import Parameter

class TestParameter(unittest.TestCase):
    """Parameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Parameter:
        """Test Parameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Parameter`
        """
        model = Parameter()
        if include_optional:
            return Parameter(
                default_array_elements = [
                    {
                        'key' : ''
                        }
                    ],
                default_source = '',
                default_value = '',
                element_type = '',
                metadata = cyperf.models.parameter_metadata.ParameterMetadata(
                    category = '', 
                    category_index = 56, 
                    default = '', 
                    description = '', 
                    display_name = '', 
                    enum = cyperf.models.enum.Enum(
                        choices = [
                            cyperf.models.choice.Choice(
                                description = '', 
                                hidden = True, 
                                name = '', 
                                value = '', )
                            ], 
                        default = '', ), 
                    flow_identifier = True, 
                    input = '', 
                    legacy_names = [
                        ''
                        ], 
                    mandatory = True, 
                    payload = cyperf.models.payload_metadata.PayloadMetadata(
                        file_extension = '', 
                        file_name = '', 
                        file_type = '', 
                        file_url = '', ), 
                    readonly = True, 
                    shared = True, 
                    type = '', 
                    type_info = cyperf.models.type_info_metadata.TypeInfoMetadata(
                        array_v2 = cyperf.models.type_array_v2_metadata.TypeArrayV2Metadata(
                            elements = [
                                cyperf.models.array_v2_element_metadata.ArrayV2ElementMetadata(
                                    id = '', 
                                    type = '', )
                                ], ), 
                        int = cyperf.models.type_int_metadata.TypeIntMetadata(
                            max_value = 56, 
                            min_value = 56, ), 
                        media = cyperf.models.type_media_metadata.TypeMediaMetadata(
                            track_id = '', 
                            track_type = '', ), 
                        string = cyperf.models.type_string_metadata.TypeStringMetadata(
                            charset = '', 
                            max_length = 56, 
                            min_length = 56, ), ), 
                    unique_value = True, ),
                sources = [
                    ''
                    ],
                type = '',
                var_field = '',
                id = '',
                operator = '',
                query_param = ''
            )
        else:
            return Parameter(
        )
        """

    def testParameter(self):
        """Test Parameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
