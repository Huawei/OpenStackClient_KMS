#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from kmclient.common import manager
from kmclient.v1 import resource


class JobManager(manager.Manager):
    """Volume backup job API management"""
    resource_class = resource.Job

    def get(self, job_id):
        """get job detail

        :param job_id:
        :rtype: :class:`resource.Job`
        :return: Job resource instance
        """
        return self._get("/jobs/%s" % job_id)
