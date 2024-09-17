# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.models.objectives_and_timeline import ObjectivesAndTimeline

class TestObjectivesAndTimeline(unittest.TestCase):
    """ObjectivesAndTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectivesAndTimeline:
        """Test ObjectivesAndTimeline
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectivesAndTimeline`
        """
        model = ObjectivesAndTimeline()
        if include_optional:
            return ObjectivesAndTimeline(
                advanced_settings = cyperf.models.advanced_settings.AdvancedSettings(
                    agent_optimization_mode = null, 
                    agent_streaming_purpose_cpu_percent = 56, 
                    automatic_cpu_percent = True, 
                    connection_graceful_stop_timeout = 56, 
                    warm_up_period = 56, ),
                primary_objective = cyperf.models.specific_objective.SpecificObjective(
                    id = '', 
                    max_pending_simulated_users = '80728', 
                    max_simulated_users_per_interval = 56, 
                    timeline = [
                        null
                        ], 
                    type = null, 
                    unit = null, ),
                secondary_objective = cyperf.models.secondary_objective.SecondaryObjective(
                    enabled = True, 
                    max_pending_simulated_users = '4', 
                    max_simulated_users_per_interval = 56, 
                    objective_unit = '', 
                    objective_value = 1.337, 
                    type = null, ),
                secondary_objectives = [
                    cyperf.models.specific_objective.SpecificObjective(
                        id = '', 
                        max_pending_simulated_users = '80728', 
                        max_simulated_users_per_interval = 56, 
                        timeline = [
                            null
                            ], 
                        type = null, 
                        unit = null, )
                    ],
                timeline_segments = [
                    null
                    ]
            )
        else:
            return ObjectivesAndTimeline(
        )
        """

    def testObjectivesAndTimeline(self):
        """Test ObjectivesAndTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
