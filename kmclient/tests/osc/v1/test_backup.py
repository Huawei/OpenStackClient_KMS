#   Copyright 2016 Huawei, Inc. All rights reserved.
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

from osc_lib import utils
from kmclient.common import resource

from kmclient.osc.v1 import backup
from kmclient.tests import base
from kmclient.v1 import backup_mgr
from kmclient.v1 import restore_mgr


@mock.patch.object(backup_mgr.VolumeBackupManager, "_create")
@mock.patch.object(utils, "find_resource")
class TestCreateVolumeBackup(base.VolumeBackupBaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestCreateVolumeBackup, self).__init__(*args, **kwargs)

    def setUp(self):
        super(TestCreateVolumeBackup, self).setUp()
        self.cmd = backup.CreateVolumeBackup(self.app, None)

    def test_create_volume_backup(self, mocked_find, mocked_create):
        args = [
            "volume-1",
            "--name", "volume-1-backup-1",
            "--description", "unittests"
        ]
        verify_args = [
            ("volume", "volume-1"),
            ("name", "volume-1-backup-1"),
            ("description", "unittests"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        mocked_find.return_value = mock.Mock(id='volume-id-1')
        mocked_create.return_value = resource.DictWithMeta(
            dict(job_id="fake_job_id"), 'Request-Id'
        )
        data = self.cmd.take_action(parsed_args)

        volumes = self.app.client_manager.volume.volumes
        mocked_find.assert_called_once_with(volumes, 'volume-1')

        json = {
            'backup': {
                'volume_id': 'volume-id-1',
                'name': "volume-1-backup-1",
                'description': "unittests"
            }
        }
        mocked_create.assert_called_once_with(
            "/cloudbackups", json=json, raw=True
        )
        self.assertEqual(data, "Request Received, job id: fake_job_id")


@mock.patch.object(restore_mgr.VolumeBackupRestoreManager, "_create")
@mock.patch.object(utils, "find_resource")
class TestRestoreVolumeBackup(base.VolumeBackupBaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestRestoreVolumeBackup, self).__init__(*args, **kwargs)

    def setUp(self):
        super(TestRestoreVolumeBackup, self).setUp()
        self.cmd = backup.RestoreVolumeBackup(self.app, None)

    def test_create_volume_backup(self, mocked_find, mocked_create):
        args = [
            "volume-backup-1",
            "volume-1",
        ]
        verify_args = [
            ("backup", "volume-backup-1"),
            ("volume", "volume-1"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        mocked_find.side_effect = [
            mock.Mock(id='volume-backup-id-1'),
            mock.Mock(id='volume-id-1'),
        ]
        mocked_create.return_value = resource.DictWithMeta(
            dict(job_id="fake_job_id"), 'Request-Id'
        )
        data = self.cmd.take_action(parsed_args)

        volumes = self.app.client_manager.volume.volumes
        backups = self.app.client_manager.volume.backups
        calls = [
            mock.call(backups, 'volume-backup-1'),
            mock.call(volumes, 'volume-1'),
        ]
        mocked_find.assert_has_calls(calls)
        json = {
            'restore': {
                'volume_id': 'volume-id-1',
            }
        }
        mocked_create.assert_called_once_with(
            "/cloudbackups/volume-backup-id-1/restore", json=json, raw=True
        )
        self.assertEqual(data, "Request Received, job id: fake_job_id")
