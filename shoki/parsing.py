#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for parsing Meeting Minutes."""

import re


def meta_headers(text_minutes):
    """Extract the metadata section of a meeting.

    - simple format of Key: Value.
    - Ends with a blank line.
    - Returns a dictionary.
    """
    meta = {}
    for line in text_minutes.split('\n'):
        if line.strip() == '':
            break
        meta_key, meta_value = line.split(':', 1)
        meta[meta_key.strip().lower()] = meta_value.strip()
    return meta


def meeting_date(meta_date):
    """Extract the meeting date.

    parses a date with the format 21 March 2017 and returns 2017-03-21."""
    pattern = re.compile(('(?P<day>\d{1,2})\s+'
                          '(?P<month>\w+)\s+'
                          '(?P<year>\d{4})[\s-]*'
                          '(?P<time>\d{1,2}:\d{1,2})\s+'
                          '(?P<timezone>\w+)'))
    result = pattern.search(meta_date)
    day = result.group('day')
    month = result.group('month')
    year = result.group('year')
    time = result.group('time')
    timezone = result.group('timezone')
    if month == 'March':
        month = '03'
    return '{0}-{1}-{2}'.format(year, month, day)
