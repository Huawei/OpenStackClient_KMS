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
from osc_lib import utils

from kmclient.common import display
from kmclient.common import resource


class Job(resource.Resource, display.Display):
    """Volume Backup Job resource instance"""

    show_column_names = [
        "Id",
        "Type",
        "Begin Time",
        "End Time",
        "Entities",
        "Status",
    ]

    column_2_property = {
        "Id": "job_id",
        "Type": "job_type",
    }

    formatter = {
        "Entities": utils.format_dict
    }

    def get_show_column_names(self):
        column_names = self.show_column_names[:]
        if "fail_reason" in self.original and self.fail_reason:
            column_names.insert(5, "Fail Reason")
        if "error_code" in self.original and self.error_code:
            column_names.insert(5, "Error Code")
        return column_names
