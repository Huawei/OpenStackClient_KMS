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

from osc_lib import utils

from kmclient.v1 import resource
from osc_lib.command import command

from kmclient.common import parser_builder as bpb
from kmclient.common.i18n import _
from kmclient.v1 import parser_builder as pb

LOG = logging.getLogger(__name__)


class CreateKey(command.ShowOne):
    _description = _("List keys")

    def get_parser(self, prog_name):
        parser = super(CreateKey, self).get_parser(prog_name)
        pb.Key.add_alias_arg(parser)
        pb.Key.add_realm_opt(parser)
        pb.Key.add_desc_opt(parser)
        # pb.Key.add_policy_opt(parser)
        # pb.Key.add_usage_opt(parser)
        # pb.Key.add_type_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        kwargs = {
            "description": args.description,
            # "policy": args.policy,
            # "usage": args.usage,
            # "key_type": args.type,
            "sequence": args.sequence,
        }
        key = mgr.create(args.alias, args.realm, **kwargs)
        columns = ["Key ID", "Domain Id"]
        output = key.get_display_data(columns)
        return columns, output


class ListKey(command.Lister):
    _description = _("List keys")

    def get_parser(self, prog_name):
        parser = super(ListKey, self).get_parser(prog_name)
        bpb.BaseParser.add_limit_opt(parser)
        bpb.BaseParser.add_offset_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        result = mgr.list(limit=args.limit, offset=args.offset,
                          sequence=args.sequence)
        return ["Key ID"], [[key, ] for key in result["keys"]]


class ShowKey(command.ShowOne):
    _description = _("Show key detail")

    def get_parser(self, prog_name):
        parser = super(ShowKey, self).get_parser(prog_name)
        pb.Key.add_key_id_arg(parser, 'display')
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        key = mgr.get(args.key, sequence=args.sequence)
        columns = resource.Key.show_column_names
        formatter = resource.Key.formatter
        output = key.get_display_data(columns, formatter)
        return columns, output


class EnableKey(command.Command):
    _description = _("enable key")

    def get_parser(self, prog_name):
        parser = super(EnableKey, self).get_parser(prog_name)
        pb.Key.add_key_id_arg(parser, 'enable')
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        key = mgr.enable(args.key, sequence=args.sequence)
        return "Key %s enabled" % key.id


class DisableKey(command.Command):
    _description = _("disable key")

    def get_parser(self, prog_name):
        parser = super(DisableKey, self).get_parser(prog_name)
        pb.Key.add_key_id_arg(parser, 'disable')
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        key = mgr.disable(args.key, sequence=args.sequence)
        return "Key %s disabled" % key.id


class DeleteKey(command.ShowOne):
    _description = _("delete key by schedule")

    def get_parser(self, prog_name):
        parser = super(DeleteKey, self).get_parser(prog_name)
        pb.Key.add_key_id_arg(parser, 'delete')
        pb.Key.add_days_opt(parser)
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        key = mgr.delete(args.key, args.days, sequence=args.sequence)
        columns = ["Key ID", "Status"]
        output = key.get_display_data(columns)
        return columns, output


class CancelDeleteKey(command.ShowOne):
    _description = _("cancel delete key")

    def get_parser(self, prog_name):
        parser = super(CancelDeleteKey, self).get_parser(prog_name)
        pb.Key.add_key_id_arg(parser, 'cancel delete')
        bpb.BaseParser.add_seq_opt(parser)
        return parser

    def take_action(self, args):
        mgr = self.app.client_manager.key_manager.keys
        key = mgr.cancel_delete(args.key, sequence=args.sequence)
        columns = ["Key ID", "Status"]
        output = key.get_display_data(columns)
        return columns, output
