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

from kmclient.common import resource as br
from kmclient.osc.v1 import key
from kmclient.tests import base
from kmclient.v1 import key_mgr
from kmclient.v1 import resource


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestCreateKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestCreateKey, self).setUp()
        self.cmd = key.CreateKey(self.app, None)

    def test_create_key(self, mocked_create):
        args = [
            "--alias", "new-key-name",
            "--realm", "cn-north-1",
            "--description", "unittests",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("alias", "new-key-name"),
            ("realm", "cn-north-1"),
            ("description", "unittests"),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        mocked_create.return_value = self.mini_key
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_alias": "new-key-name",
            "realm": "cn-north-1",
            "key_description": "unittests",
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/create-key", json=json, key='key_info'
        )
        self.assertEqual(columns, ["Key ID", "Domain Id"])
        self.assertEqual(("bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
                          "b168fe00ff56492495a7d22974df2d0b",), data)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestListKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestListKey, self).setUp()
        self.cmd = key.ListKey(self.app, None)

    def test_list_key(self, mocked_create):
        args = [
            "--limit", "10",
            "--offset", "5",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("limit", 10),
            ("offset", 5),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        return_data = {"keys": ["0a7a3f08-1529-4b30-a7bd-d74d97a908a9",
                                "1c985324-43ff-4f81-bb3f-e818afba65fb",
                                "4074f2b5-3455-4f08-bbbf-b5a321114dc4",
                                "4865d216-8aae-4de3-9162-fcb7cb025449",
                                "5c9bb365-d44f-4860-9d21-d85edd384e9f",
                                "776462d9-2da1-4c17-96e1-430d61da9273",
                                "9bff814e-3c1e-4788-ad6e-cc17bd84ffa5",
                                "ac945d5c-d87e-4f26-a333-622f74a714bb",
                                "b919e712-3743-4f7d-8d9e-8730a94aea0b"],
                       "next_marker": "",
                       "truncated": "false"}

        mocked_create.return_value = br.DictWithMeta(return_data, "RequestId")
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "limit": 10,
            "offset": 5,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/list-keys", json=json, raw=True
        )
        self.assertEqual(columns, ["Key ID"])
        self.assertEqual([[key] for key in return_data["keys"]], data)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestDescribeKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestDescribeKey, self).setUp()
        self.cmd = key.DescribeKey(self.app, None)

    def test_describe_key(self, mocked_create):
        args = [
            "key-id",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _key = {
            "key_id": "0a7a3f08-1529-4b30-a7bd-d74d97a908a9",
            "domain_id": "bb42e2cd2b784ac4bdc350fb660a2bdb",
            "key_alias": "alias_5292",
            "realm": "eu-de",
            "key_description": "",
            "creation_date": "1487741240000",
            "scheduled_deletion_date": "",
            "key_state": "2",
            "default_key_flag": "0",
            "key_type": "1"
        }

        mocked_create.return_value = resource.Key(None, _key)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/describe-key", json=json, key='key_info'
        )
        self.assertEqual(resource.Key.show_column_names, columns)
        expected = ('0a7a3f08-1529-4b30-a7bd-d74d97a908a9',
                    'alias_5292',
                    '1',
                    'Enabled',
                    '',
                    False,
                    'eu-de',
                    'bb42e2cd2b784ac4bdc350fb660a2bdb',
                    '2017-02-22 13:27:20',
                    '')
        self.assertEqual(expected, data)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestEnableKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestEnableKey, self).setUp()
        self.cmd = key.EnableKey(self.app, None)

    def test_enable_key(self, mocked_create):
        args = [
            "key-id",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _key = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "key_state": "2"
        }
        mocked_create.return_value = resource.Key(None, _key)
        result = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/enable-key", json=json, key='key_info'
        )
        self.assertEqual("Key %s enabled" % _key["key_id"], result)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestDisableKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestDisableKey, self).setUp()
        self.cmd = key.DisableKey(self.app, None)

    def test_disable_key(self, mocked_create):
        args = [
            "key-id",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _key = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "key_state": "3"
        }
        mocked_create.return_value = resource.Key(None, _key)
        result = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/disable-key", json=json, key='key_info'
        )
        self.assertEqual("Key %s disabled" % _key["key_id"], result)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestScheduleDeletionKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestScheduleDeletionKey, self).setUp()
        self.cmd = key.ScheduleDeletionKey(self.app, None)

    def test_schedule_deletion_key(self, mocked_create):
        args = [
            "key-id",
            "--pending-days", "10",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("pending_days", 10),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _key = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "key_state": "4"
        }
        mocked_create.return_value = resource.Key(None, _key)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "pending_days": 10,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/schedule-key-deletion", json=json
        )

        self.assertEquals(["Key ID", "Status"], columns)
        expected = ('0d0466b0-e727-4d9c-b35d-f84bb474a37f', 'Pending Deleted')
        self.assertEqual(expected, data)


@mock.patch.object(key_mgr.KeyManager, "_create")
class TestCancelDeletionKey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestCancelDeletionKey, self).setUp()
        self.cmd = key.CancelDeletionKey(self.app, None)

    def test_cancel_delete_key(self, mocked_create):
        args = [
            "key-id",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        _key = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "key_state": "3"
        }
        mocked_create.return_value = resource.Key(None, _key)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/cancel-key-deletion", json=json
        )

        self.assertEquals(["Key ID", "Status"], columns)
        expected = ('0d0466b0-e727-4d9c-b35d-f84bb474a37f', 'Disabled')
        self.assertEqual(expected, data)
