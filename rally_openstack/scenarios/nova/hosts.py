# Copyright 2016 IBM Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally import consts
from rally.task import validation

from rally_openstack import scenario
from rally_openstack.scenarios.nova import utils


"""Scenarios for Nova hosts."""


@validation.add("required_services", services=[consts.Service.NOVA])
@validation.add("required_platform", platform="openstack", admin=True)
@scenario.configure(name="NovaHosts.list_hosts", platform="openstack")
class ListHosts(utils.NovaScenario):

    def run(self, zone=None):
        """List all nova hosts.

        Measure the "nova host-list" command performance.

        :param zone: List nova hosts in an availability-zone.
                     None (default value) means list hosts in all
                     availability-zones
        """
        self._list_hosts(zone)


@validation.add("required_services", services=[consts.Service.NOVA])
@validation.add("required_platform", platform="openstack", admin=True)
@scenario.configure(name="NovaHosts.list_and_get_hosts", platform="openstack")
class ListAndGetHosts(utils.NovaScenario):

    def run(self, zone=None):
        """List all nova hosts, and get detailed information for compute hosts.

        Measure the "nova host-describe" command performance.

        :param zone: List nova hosts in an availability-zone.
                     None (default value) means list hosts in all
                     availability-zones
        """
        hosts = self._list_hosts(zone, service="compute")

        for host in hosts:
            self._get_host(host.host_name)
