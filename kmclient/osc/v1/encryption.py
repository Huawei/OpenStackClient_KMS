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


class CreateEncryptData(command.ShowOne):
    _description = _("Create encrypt data pair")

    def get_parser(self, prog_name):
        parser = super(CreateEncryptData, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_no_plain_text_opt(parser)
        pb.Encryption.add_context_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.encryption
        kwargs = {
            "context": args.context,
            "sequence": args.sequence,
        }

        if args.no_plain_text:
            data_pair = mgr.create_no_plain_encrypt_data(args.key, **kwargs)
            columns = ["Key ID", "Cipher Text", ]
            output = data_pair.get_display_data(columns)
            return columns, output
        else:
            data_pair = mgr.create_encrypt_data(args.key, **kwargs)
            columns = resource.EncryptData.show_column_names
            output = data_pair.get_display_data(columns)
            return columns, output


class EncryptData(command.ShowOne):
    _description = _("encrypt data")

    def get_parser(self, prog_name):
        parser = super(EncryptData, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_plain_text_opt(parser)
        pb.Encryption.add_context_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.encryption
        kwargs = {
            "plain_text": args.plain_text,
            "context": args.context,
            "sequence": args.sequence,
        }
        data_pair = mgr.encrypt_data(args.key, **kwargs)
        columns = ["Key ID", "Cipher Text", ]
        output = data_pair.get_display_data(columns)
        return columns, output


class DecryptData(command.ShowOne):
    _description = _("decrypt data")

    def get_parser(self, prog_name):
        parser = super(DecryptData, self).get_parser(prog_name)
        pb.Encryption.add_key_id_opt(parser)
        pb.Encryption.add_cipher_text_opt(parser)
        pb.Encryption.add_context_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.encryption
        kwargs = {
            "cipher_text": args.cipher_text,
            "context": args.context,
            "sequence": args.sequence,
        }
        data = mgr.decrypt_data(args.key, **kwargs)
        columns = ["Key", "Digest", ]
        output = [data.data_key, data.datakey_dgst]
        return columns, output


class RandomData(command.Command):
    _description = _("create random data")

    def get_parser(self, prog_name):
        parser = super(RandomData, self).get_parser(prog_name)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.encryption
        data = mgr.random_data(sequence=args.sequence)
        return data["random_data"]
