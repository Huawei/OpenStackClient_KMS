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
from osc_lib.command import command

from kmclient.common.i18n import _

LOG = logging.getLogger(__name__)


class CreateVolumeBackup(command.Command):
    _description = _("Create new volume backup (HuaWei custom)")

    def get_parser(self, prog_name):
        parser = super(CreateVolumeBackup, self).get_parser(prog_name)
        parser.add_argument(
            "volume",
            metavar="<volume>",
            help=_("Volume to backup (name or ID)")
        )

        parser.add_argument(
            "--name",
            metavar="<name>",
            help=_("Name of the backup")
        )

        parser.add_argument(
            "--description",
            required=False,
            metavar="<description>",
            help=_("Description of the backup")
        )
        return parser

    def take_action(self, args):
        volume_client = self.app.client_manager.volume
        volume_id = utils.find_resource(volume_client.volumes, args.volume).id
        mgr = self.app.client_manager.volume_backup.backup_mgr
        job = mgr.create(volume_id, name=args.name,
                         description=args.description)
        return 'Request Received, job id: ' + job['job_id']


class RestoreVolumeBackup(command.Command):
    _description = _("Restore volume backup")

    def get_parser(self, prog_name):
        parser = super(RestoreVolumeBackup, self).get_parser(prog_name)
        parser.add_argument(
            "backup",
            metavar="<backup>",
            help=_("Backup to restore (name or ID)")
        )
        parser.add_argument(
            "volume",
            metavar="<volume>",
            help=_("Volume to restore to (name or ID)")
        )
        return parser

    def take_action(self, args):
        volume_client = self.app.client_manager.volume
        backup = utils.find_resource(volume_client.backups, args.backup)
        volume = utils.find_resource(volume_client.volumes, args.volume)
        mgr = self.app.client_manager.volume_backup.restore_mgr
        job = mgr.restore(backup.id, volume.id)
        return 'Request Received, job id: ' + job['job_id']
