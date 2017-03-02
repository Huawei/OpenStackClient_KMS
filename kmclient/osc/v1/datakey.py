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
import logging

from osc_lib.command import command

from kmclient.common import parser_builder as bpb
from kmclient.common.i18n import _
from kmclient.v1 import parser_builder as pb
from kmclient.v1 import resource

LOG = logging.getLogger(__name__)


class CreateDatakey(command.ShowOne):
    _description = _("Create encrypt data pair")

    def get_parser(self, prog_name):
        parser = super(CreateDatakey, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_without_plain_text_opt(parser)
        pb.Encryption.add_datakey_length_opt(parser)
        pb.Encryption.add_context_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.datakeys
        kwargs = {
            "datakey_length": args.datakey_length,
            "encryption_context": args.encryption_context,
            "sequence": args.sequence,
        }

        if args.without_plain_text:
            data_pair = mgr.create_no_plain_encrypt_data(args.key_id, **kwargs)
            columns = ["Key ID", "Cipher Text", ]
            output = data_pair.get_display_data(columns)
            return columns, output
        else:
            data_pair = mgr.create_encrypt_data(args.key_id, **kwargs)
            columns = resource.EncryptData.show_column_names
            output = data_pair.get_display_data(columns)
            return columns, output


class EncryptDatakey(command.ShowOne):
    _description = _("encrypt data")

    def get_parser(self, prog_name):
        parser = super(EncryptDatakey, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_plain_text_opt(parser)
        pb.Encryption.add_context_opt(parser)
        pb.Encryption.add_datakey_plain_length_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.datakeys
        kwargs = {
            "plain_text": args.plain_text,
            "datakey_plain_length": args.datakey_plain_length,
            "encryption_context": args.encryption_context,
            "sequence": args.sequence,
        }
        data_pair = mgr.encrypt_data(args.key_id, **kwargs)
        columns = ["Key ID", "Cipher Text", ]
        output = data_pair.get_display_data(columns)
        return columns, output


class DecryptDatakey(command.ShowOne):
    _description = _("decrypt data")

    def get_parser(self, prog_name):
        parser = super(DecryptDatakey, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_cipher_text_opt(parser)
        pb.Encryption.add_context_opt(parser)
        pb.Encryption.add_datakey_cipher_length_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.datakeys
        kwargs = {
            "cipher_text": args.cipher_text,
            "datakey_cipher_length": args.datakey_cipher_length,
            "encryption_context": args.encryption_context,
            "sequence": args.sequence,
        }
        data = mgr.decrypt_data(args.key_id, **kwargs)
        columns = ["Key", "Digest", ]
        output = [data.data_key, data.datakey_dgst]
        return columns, output


class RandomGenerate(command.Command):
    _description = _("create random data")

    def get_parser(self, prog_name):
        parser = super(RandomGenerate, self).get_parser(prog_name)
        pb.Encryption.add_random_data_len_arg(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.datakeys
        data = mgr.random_data(random_data_length=args.random_data_length,
                               sequence=args.sequence)
        return data["random_data"]
