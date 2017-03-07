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
import os

from kmclient.common import parsetypes
from kmclient.common.i18n import _
from osc_lib.cli import parseractions


class Key(object):

    @staticmethod
    def add_key_id_arg(parser, op):
        parser.add_argument(
            "key",
            metavar="<key-id>",
            help=_("Key to %s (ID)" % op)
        )

    @staticmethod
    def add_alias_arg(parser):
        parser.add_argument(
            "alias",
            metavar="<alias>",
            help=_("Key alias name, should match regex "
                   "'^[a-zAZ0-9:/_-]{1,255}$', and not end with '/default' "
                   "which has been used by system")
        )

    @staticmethod
    def add_realm_opt(parser):
        parser.add_argument(
            "--realm",
            metavar="<realm>",
            required=True,
            help=_("Realm which key belong to (example: cn-north-1)")
        )

    @staticmethod
    def add_desc_opt(parser):
        parser.add_argument(
            "--description",
            metavar="<description>",
            required=False,
            help=_("Key description (length 0-255)")
        )

    @staticmethod
    def add_policy_opt(parser):
        parser.add_argument(
            "--policy",
            metavar="<key-policy>",
            required=False,
            help=_("Key policy (length 0-255, json format)")
        )

    @staticmethod
    def add_usage_opt(parser):
        parser.add_argument(
            "--usage",
            metavar="<key-usage>",
            required=False,
            help=_("Key usage (default: Encrypt_Decrypt)")
        )

    @staticmethod
    def add_type_opt(parser):
        parser.add_argument(
            "--type",
            metavar="<key-type>",
            required=False,
            help=_("Key type")
        )

    @staticmethod
    def add_days_opt(parser):
        parser.add_argument(
            "--pending-days",
            metavar="<number>",
            required=True,
            type=parsetypes.int_range_type(7, 1096),
            help=_("Delete key after days (number range: 7-1096)")
        )


class Encryption(object):

    @staticmethod
    def add_context_opt(parser):
        parser.add_argument(
            "--encryption-context",
            metavar="<key=value>",
            required=False,
            action=parseractions.KeyValueAction,
            help=_("Name-value pair that specifies the encryption context to "
                   "be used for authenticated encryption. If used here, "
                   "the same value must be supplied to the decrypt API "
                   "or decryption will fail.")
        )

    @staticmethod
    def add_plain_text_opt(parser):
        parser.add_argument(
            "--plain-text",
            metavar="<blob>",
            required=True,
            type=parsetypes.blob_or_filepath,
            help=_("Data to be encrypted. Could be blob (blob-text) "
                   "or file-path (file://absolute-path), if file-path, "
                   "will read file content as blob.")
        )

    @staticmethod
    def add_cipher_text_opt(parser):
        parser.add_argument(
            "--cipher-text",
            metavar="<blob>",
            required=True,
            type=parsetypes.blob_or_filepath,
            help=_("Data to be decrypted. Could be blob (blob-text) "
                   "or file-path (file://absolute-path), if file-path, "
                   "will read file content as blob.")
        )

    @staticmethod
    def add_key_id_opt(parser):
        parser.add_argument(
            "--key-id",
            metavar="<key-id>",
            required=True,
            help=_("Key used for encrypt/decrypt (ID)")
        )

    @staticmethod
    def add_without_plain_text_opt(parser):
        parser.add_argument(
            "--without-plain-text",
            required=False,
            default=False,
            action="store_true",
            help=_("Do not show plain text")
        )

    @staticmethod
    def add_random_data_len_arg(parser):
        parser.add_argument(
            "random_data_length",
            metavar="<length>",
            type=int,
            help=_("The length of the random byte string")
        )

    @staticmethod
    def add_datakey_length_opt(parser):
        parser.add_argument(
            "--datakey-length",
            metavar="<length>",
            type=int,
            default=512,
            help=_("The length of the data encryption key in bytes")
        )

    @staticmethod
    def add_datakey_plain_length_opt(parser):
        parser.add_argument(
            "--datakey-plain-length",
            metavar="<length>",
            type=int,
            default=64,
            help=_("DEK plain text length")
        )

    @staticmethod
    def add_datakey_cipher_length_opt(parser):
        parser.add_argument(
            "--datakey-cipher-length",
            metavar="<length>",
            type=int,
            default=64,
            help=_("DEK cipher text length")
        )
