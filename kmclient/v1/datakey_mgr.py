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
from keystoneauth1 import exceptions

from kmclient.common.i18n import _
from kmclient.common import manager
from kmclient.common import utils
from kmclient.v1 import resource


class DatakeyManager(manager.Manager):
    """Key Manager datakeys API management"""

    resource_class = resource.EncryptData

    def create_encrypt_data(self, key_id, datakey_length=None,
                            encryption_context=None, sequence=None):
        """create datakeys data pair

        :param datakey_length:
        :param key_id:
        :param encryption_context:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "encryption_context": encryption_context,
            "datakey_length": datakey_length,
            "sequence": sequence,
        })
        return self._create("/create-datakey", json=json)

    def create_no_plain_encrypt_data(self, key_id, datakey_length=None,
                                     encryption_context=None, sequence=None):
        """create datakeys data pair without plain text returned

        :param key_id:
        :param datakey_length: 512 for now
        :param encryption_context:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "encryption_context": encryption_context,
            "datakey_length": datakey_length,
            "sequence": sequence,
        })
        return self._create("/create-datakey-without-plaintext", json=json)

    def encrypt_data(self, key_id, plain_text, datakey_plain_length=None,
                     encryption_context=None, sequence=None):
        """encrypt data

        :param datakey_plain_length:
        :param encryption_context: 64 for now
        :param key_id:
        :param plain_text: 64 bit DEK plain text
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "plain_text": plain_text,
            "encryption_context": encryption_context,
            "datakey_plain_length": datakey_plain_length,
            "sequence": sequence,
        })
        return self._create("/encrypt-datakey", json=json)

    def decrypt_data(self, key_id, cipher_text, datakey_cipher_length=None,
                     encryption_context=None, sequence=None):
        """decrypt data

        :param datakey_cipher_length:
        :param encryption_context:
        :param key_id:
        :param cipher_text: DEK encrypted text
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "cipher_text": cipher_text,
            "encryption_context": encryption_context,
            "datakey_cipher_length": datakey_cipher_length,
            "sequence": sequence,
        })
        return self._create("/decrypt-datakey", json=json)

    def random_data(self, random_data_length=None, sequence=None):
        """random data

        :param random_data_length:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "random_data_length": random_data_length,
            "sequence": sequence,
        })
        return self._create("/gen-random", json=json, raw=True)
