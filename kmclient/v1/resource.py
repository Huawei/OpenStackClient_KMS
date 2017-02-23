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

from kmclient.common import display
from kmclient.common import resource
from kmclient.common import utils


class Key(resource.Resource, display.Display):
    """Key Manager Key resource instance"""

    show_column_names = [
        "ID",
        "alias",
        "type",
        "status",
        "description",
        "Default Key",
        "Realm",
        "Domain ID",
        "Creation date",
        "Scheduled deletion date",
    ]

    formatter = {
        "Creation date": utils.format_time,
        "Scheduled deletion date": utils.format_time,
    }

    column_2_property = {
        "alias": "key_alias",
        "type": "key_type",
    }

    @property
    def id(self):
        return self.key_id

    @property
    def status(self):
        if self.key_state == "2":
            return "Enabled"
        if self.key_state == "3":
            return "Disabled"
        if self.key_state == "4":
            return "Pending Deleted"

    @property
    def default_key(self):
        return self.default_key_flag == "1"


class EncryptData(resource.Resource, display.Display):
    """encryption data pair instance"""

    show_column_names = [
        "Key ID",
        "Plain Text",
        "Cipher Text",
    ]
