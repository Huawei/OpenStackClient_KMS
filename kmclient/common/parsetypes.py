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
import argparse
import string
from datetime import datetime

from osc_lib.i18n import _


def int_range_type(from_, to):
    def wrapped(user_input):
        try:
            int_user_input = int(user_input)
        except ValueError:
            msg = _("Not a valid integer value: %s") % user_input
            raise argparse.ArgumentTypeError(msg)

        if int_user_input > to:
            tpl = _("Your input %s is great than max valid value %d")
            msg = tpl % (user_input, to)
            raise argparse.ArgumentTypeError(msg)

        if int_user_input < from_:
            tpl = _("Your input %s is less than min valid value %d")
            msg = tpl % (user_input, from_)
            raise argparse.ArgumentTypeError(msg)

        return int_user_input

    return wrapped
