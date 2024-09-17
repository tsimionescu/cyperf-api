# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.media_file import MediaFile

class TestMediaFile(unittest.TestCase):
    """MediaFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MediaFile:
        """Test MediaFile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaFile`
        """
        model = MediaFile()
        if include_optional:
            return MediaFile(
                file_value = cyperf.models.file_value.FileValue(
                    file_name = '', 
                    payload = [
                        'YQ=='
                        ], 
                    resource_url = '', 
                    value = '', ),
                id = '',
                media_tracks = [
                    cyperf.models.media_track.MediaTrack(
                        bitrate = 56, 
                        bitrate_kbps = 56, 
                        codec = '', 
                        codec_description = '', 
                        id = '', 
                        track_id = '', 
                        track_type = null, )
                    ]
            )
        else:
            return MediaFile(
        )
        """

    def testMediaFile(self):
        """Test MediaFile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
