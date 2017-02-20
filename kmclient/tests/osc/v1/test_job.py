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
import copy

import mock
import six

from kmclient.osc.v1 import job
from kmclient.tests import base
from kmclient.v1 import job_mgr
from kmclient.v1 import resource


@mock.patch.object(job_mgr.JobManager, "_get")
class TestShowJob(base.VolumeBackupBaseTestCase):
    def __init__(self, *args, **kwargs):
        super(TestShowJob, self).__init__(*args, **kwargs)
        self.job = {
            "status": "SUCCESS",
            "entities": {
                "bks_create_volume_name": "autobk_volume",
                "backup_id": "ba5401a2-7cd2-4c01-8c0d-c936ab412d6d",
                "volume_id": "7e5fdc5a-5e36-4b22-8bcc-7f17037290cc",
                "snapshot_id": "a77a96bf-dd18-40bf-a446-fdcefc1719ec"
            },
            "job_id": "4010b39b5281d3590152874bfa3b1604",
            "job_type": "bksCreateBackup",
            "begin_time": "2016-01-28T16:14:09.466Z",
            "end_time": "2016-01-28T16:25:27.690Z",
            "error_code": None,
            "fail_reason": None
        }

    def setUp(self):
        super(TestShowJob, self).setUp()
        self.cmd = job.ShowJob(self.app, None)

    def test_show_job_success(self, mocked_get):
        args = [
            "job-id-1",
        ]
        verify_args = [
            ("job_id", "job-id-1"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        mocked_get.return_value = resource.Job(
            mock.Mock(), self.job, "request-id"
        )
        columns, data = self.cmd.take_action(parsed_args)

        self.assertEqual(columns, [
            "Id",
            "Type",
            "Begin Time",
            "End Time",
            "Entities",
            "Status",
        ])

        entities = six.text_type(
            "backup_id='ba5401a2-7cd2-4c01-8c0d-c936ab412d6d', "
            "bks_create_volume_name='autobk_volume', "
            "snapshot_id='a77a96bf-dd18-40bf-a446-fdcefc1719ec', "
            "volume_id='7e5fdc5a-5e36-4b22-8bcc-7f17037290cc'"
        )

        self.assertEqual(data, (
            "4010b39b5281d3590152874bfa3b1604",
            "bksCreateBackup",
            "2016-01-28T16:14:09.466Z",
            "2016-01-28T16:25:27.690Z",
            entities,
            "SUCCESS",
        ))

    def test_show_failed_job(self, mocked_get):
        args = [
            "job-id-1",
        ]
        verify_args = [
            ("job_id", "job-id-1"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _job = copy.deepcopy(self.job)
        _job["error_code"] = "10086"
        _job["fail_reason"] = "unittest"
        mocked_get.return_value = resource.Job(
            mock.Mock(), _job, "request-id"
        )
        columns, data = self.cmd.take_action(parsed_args)

        self.assertEqual(columns, [
            "Id",
            "Type",
            "Begin Time",
            "End Time",
            "Entities",
            "Error Code",
            "Fail Reason",
            "Status",
        ])

        entities = six.text_type(
            "backup_id='ba5401a2-7cd2-4c01-8c0d-c936ab412d6d', "
            "bks_create_volume_name='autobk_volume', "
            "snapshot_id='a77a96bf-dd18-40bf-a446-fdcefc1719ec', "
            "volume_id='7e5fdc5a-5e36-4b22-8bcc-7f17037290cc'"
        )

        self.assertEqual(data, (
            "4010b39b5281d3590152874bfa3b1604",
            "bksCreateBackup",
            "2016-01-28T16:14:09.466Z",
            "2016-01-28T16:25:27.690Z",
            entities,
            "10086",
            "unittest",
            "SUCCESS",
        ))