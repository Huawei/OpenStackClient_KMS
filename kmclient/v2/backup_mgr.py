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
from kmclient.common import utils
from kmclient.v2 import resource


class VolumeBackupManager(manager.Manager):
    """Volume backup API management"""
    resource_class = resource.VolumeBackup

    def create(self, volume_id, name=None, description=None):
        """Creates a volume backup

        :param volume_id: The ID of the volume to backup.
        :param name: The name of the backup.
        :param description: The description of the backup.
        :rtype: :class:`DictWithMeta

        """
        backup = utils.remove_empty_from_dict({
            'volume_id': volume_id,
            'name': name,
            'description': description
        })
        json = {'backup': backup}
        return self._create('/cloudbackups', json=json, raw=True)
