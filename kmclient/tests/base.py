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
import mock

from osc_lib.tests import utils

from kmclient.tests import fakes
from kmclient.v1 import resource


class BaseTestCase(utils.TestCommand):
    """Base Test case class for all unit tests."""
    pass


class KeyManagerBaseTestCase(BaseTestCase):
    """Base test case class for HuaWei Volume Backup management API."""

    def __init__(self, *args, **kwargs):
        super(KeyManagerBaseTestCase, self).__init__(*args, **kwargs)
        self.cmd = None
        self.mini_key = None

    def setUp(self):
        super(KeyManagerBaseTestCase, self).setUp()
        fake_km_client = fakes.FakeKeyManagerClient()
        self.app.client_manager.key_manager = fake_km_client
        self.mini_key = resource.Key(None, {
            "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
            "domain_id": "b168fe00ff56492495a7d22974df2d0b"
        })
