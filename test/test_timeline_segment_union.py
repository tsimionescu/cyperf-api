# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.timeline_segment_union import TimelineSegmentUnion

class TestTimelineSegmentUnion(unittest.TestCase):
    """TimelineSegmentUnion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimelineSegmentUnion:
        """Test TimelineSegmentUnion
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimelineSegmentUnion`
        """
        model = TimelineSegmentUnion()
        if include_optional:
            return TimelineSegmentUnion(
                duration = 56,
                segment_type = 'SteadySegment',
                warm_up_period = 56,
                id = '',
                objective_unit = '',
                objective_value = 1.337,
                enabled = True,
                number_of_steps = 56
            )
        else:
            return TimelineSegmentUnion(
                duration = 56,
                segment_type = 'SteadySegment',
                id = '',
                objective_unit = '',
                objective_value = 1.337,
                enabled = True,
                number_of_steps = 56,
        )
        """

    def testTimelineSegmentUnion(self):
        """Test TimelineSegmentUnion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
