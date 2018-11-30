#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Modeling the minutes."""

import urllib.request

from shoki import formatter
from shoki import parsing
from shoki import shoki_config


def minutes_as_data(text):
    """Return a data structure for the minutes."""
    minutes_data = {}
    # Handling the meta data of the meeting
    meta = parsing.meta_headers(text)
    mtg_date = parsing.meeting_date(meta["date"])
    minutes_data["title"] = meta["meeting"]
    minutes_data["scribe"] = [meta["scribe"]]
    minutes_data["meeting_date"] = mtg_date
    minutes_data["attendees"] = []
    minutes_data["record"] = []
    # Handling the discussions record
    blocks = parsing.extract_blocks(text)
    for block in blocks:
        discussion = parsing.extract_topic(block["topic_line"])
        discussion["discussion"], description = parsing.extract_prose(block["prose"])  # noqa
        discussion["intro"] = description
        minutes_data["record"].append(discussion)
    return minutes_data


def create_minutes(location=shoki_config.MINUTES_LOCATION,
                   out_format="webcompatwiki"):
    """Create Minutes."""
    minutes = ""
    with urllib.request.urlopen(location) as f:
        raw_text = f.read().decode("utf-8")

    try:
        minutes = formatter.convert(minutes_as_data(raw_text), out_format)
    except Exception as e:
        print(shoki_config.FORMAT_ERROR.format(error=e))
    return minutes
