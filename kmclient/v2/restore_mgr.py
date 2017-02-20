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

from kmclient.common import manager
from kmclient.v2 import resource


class VolumeBackupRestoreManager(manager.Manager):
    """Volume backup API management"""
    resource_class = resource.VolumeBackupRestore

    def restore(self, backup_id, volume_id):
        """Restore a backup to a volume.

        :param backup_id: The ID of the backup to restore.
        :param volume_id: The ID of the volume to restore the backup to.
        :rtype: :class:`DictWithMeta`
        """
        data = {'restore': {'volume_id': volume_id}}
        return self._create("/cloudbackups/%s/restore" % backup_id,
                            json=data,
                            raw=True)
