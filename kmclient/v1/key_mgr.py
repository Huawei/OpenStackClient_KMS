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


class KeyManager(manager.Manager):
    """Key Manager Key API management"""

    resource_class = resource.Key

    def find(self, name):
        """find key by key-id

        :param name: key-id
        :rtype: resource.Key
        :return: Key which id equal to 'name'
        """
        try:
            return self.get(name)
        except exceptions.ClientException as e:
            pass

        # results = self.list(name=id_or_name)
        # filtered = [result for result in results if result.name == id_or_name]
        # matched_number = len(filtered)
        # if matched_number > 1:
        #     raise execs.NotUniqueMatch
        # elif matched_number == 1:
        #     return filtered[0]
        message = _("No Key with ID '%s' exists.") % name
        raise exceptions.NotFound(message)

    def create(self, alias, realm, description=None, policy=None, usage=None,
               key_type=None, sequence=None):
        """

        :param key_type:
        :param usage:
        :param policy:
        :param alias:
        :param realm:
        :param description:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_alias": alias,
            "realm": realm,
            "key_description": description,
            "key_policy": policy,
            "key_usage": usage,
            "key_type": key_type,
            "sequence": sequence,
        })
        return self._create('/create-key', json=json, key="key_info")

    def list(self, limit=None, offset=None, sequence=None):
        """list keys

        :param limit:
        :param offset:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "limit": limit,
            "marker": offset,
            "sequence": sequence,
        })
        return self._create("/list-keys", json=json, raw=True)

    def get(self, key_id, sequence=None):
        """get key detail

        :param key_id:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "sequence": sequence,
        })
        return self._create("/describe-key", json=json, key="key_info")

    def enable(self, key_id, sequence=None):
        """enable key

        :param key_id:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "sequence": sequence,
        })
        return self._create("/enable-key", json=json, key="key_info")

    def disable(self, key_id, sequence=None):
        """disable key

        :param key_id:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "sequence": sequence,
        })
        return self._create("/disable-key", json=json, key="key_info")

    def delete(self, key_id, pending_days, sequence=None):
        """delete key

        :param key_id:
        :param pending_days: delete after days
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "pending_days": pending_days,
            "sequence": sequence,
        })
        return self._create("/schedule-key-deletion", json=json)

    def cancel_delete(self, key_id, sequence=None):
        """delete key

        :param key_id:
        :param sequence:
        :return:
        """
        json = utils.remove_empty_from_dict({
            "key_id": key_id,
            "sequence": sequence,
        })
        return self._create("/cancel-key-deletion", json=json)
