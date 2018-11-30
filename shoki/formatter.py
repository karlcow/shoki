#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Minutes Formatters."""

import os
from string import Template
import sys

from shoki import shoki_config


def convert(minutes_data, out_format):
    """Convert the minutes data structure into a defined format.

    This will really create any format of your choice.
    You just need to create the appropriate templates
    in a specific directory.
    See shoki/templates/webcompat_wiki/ for example.
    """
    templates = load_templates(out_format)
    # If there is a list of templates, the format exists.
    if templates:
        if len(minutes_data["scribe"]) > 1:
            scribes = ", ".join(minutes_data["scribe"])
        else:
            scribes = minutes_data["scribe"][0]
        text = ""
        text += templates["main"].substitute(
            title=minutes_data["title"],
            date=minutes_data["meeting_date"],
            previous_date="@@TO_FIX",
            scribe=scribes,
        )
        for discussion in minutes_data["record"]:
            DISCUSSION = True
            # Discussion title and owners
            owner = discussion["owner"]
            if not owner:
                owner = ' {owner} '.format(
                    owner=shoki_config.default_config['topic_owner'])
            text += templates["topic"].substitute(
                topic=discussion["topic"], owner=owner
            )
            # Time for discussion description
            intro = discussion["intro"]
            if not discussion["discussion"]:
                DISCUSSION = False
            if intro and DISCUSSION:
                text += templates["intro"].substitute(intro=intro)
            else:
                text += templates["intro_no_chat"].substitute(intro=intro)
            # Let's go to the flow of the discussion.
            for voice in discussion["discussion"]:
                if voice.get("speaker"):
                    text += templates["voice"].substitute(
                        speaker=voice["speaker"], said=voice["said"]
                    )
                elif voice.get("todo"):
                    text += templates["todo"].substitute(
                        owner=voice["owner"],
                        todo=voice["todo"],
                        deadline=voice["deadline"],
                    )
                else:
                    text += "@@WHATT probably something wrong"
        return text
    else:
        sys.exit("This {f} format does not exist yet.".format(f=out_format))


def load_templates(out_format):
    """Take a string and return a dictionary of templates.

    If the output format doesn't exist. It returns None.
    """
    templates_dir = os.path.join(shoki_config.ROOT, "shoki/templates/", out_format)
    if os.path.isdir(templates_dir):
        t = {}
        for tmpl_name in os.listdir(templates_dir):
            tmpl_key = os.path.splitext(tmpl_name)[0]
            full_path = os.path.join(templates_dir, tmpl_name)
            with open(full_path) as f:
                tmpl = Template(f.read())
            t[tmpl_key] = tmpl
        return t
    return None
