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


class BaseTestCase(utils.TestCommand):
    """Base Test case class for all unit tests."""
    pass


class VolumeBackupBaseTestCase(BaseTestCase):
    """Base test case class for HuaWei Volume Backup management API."""

    def __init__(self, *args, **kwargs):
        super(VolumeBackupBaseTestCase, self).__init__(*args, **kwargs)
        self.cmd = None

    def setUp(self):
        super(VolumeBackupBaseTestCase, self).setUp()
        fake_vb_client = fakes.FakeVolumeBackupClient()
        self.app.client_manager.volume_backup = fake_vb_client
        self.app.client_manager.volume = mock.Mock(
            volumes=mock.Mock(), backups=mock.Mock()
        )
