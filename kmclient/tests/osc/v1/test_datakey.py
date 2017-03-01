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
from kmclient.osc.v1 import datakey
from kmclient.tests import base
from kmclient.v1 import datakey_mgr
from kmclient.v1 import resource


@mock.patch.object(datakey_mgr.DatakeyManager, "_create")
class TestRandomGenerate(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestRandomGenerate, self).setUp()
        self.cmd = datakey.RandomGenerate(self.app, None)

    def test_random(self, mocked_create):
        args = [
            "--random-data-length", "128",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("random_data_length", 128),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        random_ = {
            "random_data":
                "5791C223E87124AB9FC29B5A8AC60BE4B98D168F47A58BB2A"
                "88833E40D6ED32D57E2AAB5410492EB25096873F9CE3D45E0D"
                "22F820A5AB4EEADC33A1A6AE780F1"
        }
        mocked_create.return_value = br.DictWithMeta(random_, "Request-Id")
        result = self.cmd.take_action(parsed_args)

        json = {
            "random_data_length": 128,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/gen-random", json=json, raw=True
        )
        self.assertEqual(random_["random_data"], result)


@mock.patch.object(datakey_mgr.DatakeyManager, "_create")
class TestCreateDatakey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestCreateDatakey, self).setUp()
        self.cmd = datakey.CreateDatakey(self.app, None)

    def test_create_encrypt_data(self, mocked_create):
        args = [
            "--key", "key-id",
            "--datakey-length", "512",
            "--encryption-context", "k1=v1",
            "--encryption-context", "k2=v2",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("datakey_length", 512),
            ("encryption_context", dict(k1="v1", k2="v2")),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        encrypt_data = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "plain_text": "plain_text",
            "cipher_text": "cipher_text",
        }
        mocked_create.return_value = resource.EncryptData(None, encrypt_data)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "encryption_context": dict(k1="v1", k2="v2"),
            "datakey_length": 512,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/create-datakey", json=json
        )

        self.assertEqual(resource.EncryptData.show_column_names, columns)
        expected = ('0d0466b0-e727-4d9c-b35d-f84bb474a37f',
                    'plain_text',
                    'cipher_text',)
        self.assertEqual(expected, data)

    def test_create_encrypt_data_no_plain_text(self, mocked_create):
        args = [
            "--key", "key-id",
            "--encryption-context", "k1=v1",
            "--encryption-context", "k2=v2",
            "--without-plain-text",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("without_plain_text", True),
            ("encryption_context", dict(k1="v1", k2="v2")),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        encrypt_data = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "cipher_text": "cipher_text",
        }
        mocked_create.return_value = resource.EncryptData(None, encrypt_data)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "encryption_context": dict(k1="v1", k2="v2"),
            "datakey_length": 512,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/create-datakey-without-plaintext", json=json
        )

        self.assertEqual(['Key ID', 'Cipher Text'], columns)
        expected = ('0d0466b0-e727-4d9c-b35d-f84bb474a37f',
                    'cipher_text',)
        self.assertEqual(expected, data)


@mock.patch.object(datakey_mgr.DatakeyManager, "_create")
class TestEncryptDatakey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestEncryptDatakey, self).setUp()
        self.cmd = datakey.EncryptDatakey(self.app, None)

    def test_encrypt(self, mocked_create):
        args = [
            "--key", "key-id",
            "--datakey-plain-length", "64",
            "--encryption-context", "k1=v1",
            "--encryption-context", "k2=v2",
            "--plain-text", "some-plain-text",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("plain_text", "some-plain-text"),
            ("datakey_plain_length", 64),
            ("encryption_context", dict(k1="v1", k2="v2")),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        encrypt_data = {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "cipher_text": "cipher_text",
            "datakey_length": "64"
        }
        mocked_create.return_value = resource.EncryptData(None, encrypt_data)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "plain_text": "some-plain-text",
            "encryption_context": dict(k1="v1", k2="v2"),
            "datakey_plain_length": 64,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/encrypt-datakey", json=json
        )
        expected = ('0d0466b0-e727-4d9c-b35d-f84bb474a37f', 'cipher_text')
        self.assertEqual(expected, data)
        self.assertEqual(['Key ID', 'Cipher Text'], columns)


@mock.patch.object(datakey_mgr.DatakeyManager, "_create")
class TestDecryptDatakey(base.KeyManagerBaseTestCase):
    def setUp(self):
        super(TestDecryptDatakey, self).setUp()
        self.cmd = datakey.DecryptDatakey(self.app, None)

    def test_decrypt(self, mocked_create):
        args = [
            "--key", "key-id",
            "--encryption-context", "k1=v1",
            "--encryption-context", "k2=v2",
            "--cipher-text", "some-cipher-text",
            "--sequence", "ThisIsA36BitSequence",
        ]
        verify_args = [
            ("key", "key-id"),
            ("cipher_text", "some-cipher-text"),
            ("encryption_context", dict(k1="v1", k2="v2")),
            ("sequence", "ThisIsA36BitSequence"),
        ]
        parsed_args = self.check_parser(
            self.cmd, args, verify_args
        )

        encrypt_data = {
            "data_key": "data-key",
            "datakey_length": "64",
            "datakey_dgst": "digest",
        }
        mocked_create.return_value = resource.EncryptData(None, encrypt_data)
        columns, data = self.cmd.take_action(parsed_args)

        json = {
            "key_id": "key-id",
            "cipher_text": "some-cipher-text",
            "encryption_context": dict(k1="v1", k2="v2"),
            "datakey_cipher_length": 64,
            "sequence": "ThisIsA36BitSequence",
        }
        mocked_create.assert_called_once_with(
            "/decrypt-datakey", json=json
        )
        expected = ['data-key', 'digest']
        self.assertEqual(expected, data)
        self.assertEqual(["Key", "Digest", ], columns)
