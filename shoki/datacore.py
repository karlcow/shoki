#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Modeling the minutes."""

import shoki_config as cfg
from shoki import parsing

def minutes_as_data(text):
    """Returns a data structure for the minutes."""
    minutes_data = {}
    # Handling the meta data of the meeting
    meta = parsing.meta_headers(text)
    mtg_date = parsing.meeting_date(meta['date'])
    minutes_data['title'] = meta['meeting']
    minutes_data['scribe'] = [meta['scribe']]
    minutes_data['meeting_date'] = mtg_date
    minutes_data['attendees'] = []
    minutes_data['record'] = []
    # Handling the discussions record
    blocks = parsing.extract_blocks(text)
    for block in blocks:
        discussion = parsing.extract_topic(block['topic_line'])
        discussion['discussion'] = parsing.extract_prose(block['prose'])
        minutes_data['record'].append(discussion)
    return minutes_data
