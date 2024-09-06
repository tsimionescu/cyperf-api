# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cyperf.api.agents_api import AgentsApi


class TestAgentsApi(unittest.TestCase):
    """AgentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_agents(self) -> None:
        """Test case for delete_agents

        """
        pass

    def test_get_agent_tags(self) -> None:
        """Test case for get_agent_tags

        """
        pass

    def test_get_agents(self) -> None:
        """Test case for get_agents

        """
        pass

    def test_get_agents_by_id(self) -> None:
        """Test case for get_agents_by_id

        """
        pass

    def test_get_controllers(self) -> None:
        """Test case for get_controllers

        """
        pass

    def test_get_controllers_by_id(self) -> None:
        """Test case for get_controllers_by_id

        """
        pass

    def test_patch_agents(self) -> None:
        """Test case for patch_agents

        """
        pass

    def test_poll_controllers_switch_app(self) -> None:
        """Test case for poll_controllers_switch_app

        """
        pass

    def test_poll_root_batch_delete(self) -> None:
        """Test case for poll_root_batch_delete

        """
        pass

    def test_poll_root_export_files(self) -> None:
        """Test case for poll_root_export_files

        """
        pass

    def test_poll_root_reboot(self) -> None:
        """Test case for poll_root_reboot

        """
        pass

    def test_poll_root_release(self) -> None:
        """Test case for poll_root_release

        """
        pass

    def test_poll_root_reserve(self) -> None:
        """Test case for poll_root_reserve

        """
        pass

    def test_poll_root_set_dpdk_mode(self) -> None:
        """Test case for poll_root_set_dpdk_mode

        """
        pass

    def test_poll_root_set_ntp(self) -> None:
        """Test case for poll_root_set_ntp

        """
        pass

    def test_poll_root_update(self) -> None:
        """Test case for poll_root_update

        """
        pass

    def test_start_controllers_switch_app(self) -> None:
        """Test case for start_controllers_switch_app

        """
        pass

    def test_start_root_batch_delete(self) -> None:
        """Test case for start_root_batch_delete

        """
        pass

    def test_start_root_export_files(self) -> None:
        """Test case for start_root_export_files

        """
        pass

    def test_start_root_reboot(self) -> None:
        """Test case for start_root_reboot

        """
        pass

    def test_start_root_release(self) -> None:
        """Test case for start_root_release

        """
        pass

    def test_start_root_reserve(self) -> None:
        """Test case for start_root_reserve

        """
        pass

    def test_start_root_set_dpdk_mode(self) -> None:
        """Test case for start_root_set_dpdk_mode

        """
        pass

    def test_start_root_set_ntp(self) -> None:
        """Test case for start_root_set_ntp

        """
        pass

    def test_start_root_update_agents(self) -> None:
        """Test case for start_root_update_agents

        """
        pass


if __name__ == '__main__':
    unittest.main()
