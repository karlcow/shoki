#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for parsing Meeting Minutes."""

import unittest

from shoki.parsing import meeting_date
from shoki.parsing import meta_headers

FIXTURE_DIR = './tests/fixtures/'


class TestShokiParsing(unittest.TestCase):
    def setUp(self):
        self.minutes = self.read_minutes('minutes_normal.txt')
        self.headers = meta_headers(self.minutes)
        self.meta_date = self.headers['date']

    def tearDown(self):
        pass

    def read_minutes(self, minutes_fixture):
        """Reads the fixture for tests."""
        with open(FIXTURE_DIR + minutes_fixture) as f:
            minutes_fixture = f.read()
        return minutes_fixture

    def test_meeting_date(self):
        """Extracts the meeting date."""
        actual = meeting_date(self.meta_date)
        expected = '2017-03-21'
        self.assertEqual(actual, expected)

    def test_meta_headers(self):
        """Returns the dictionary for meeting metatada."""
        actual = meta_headers(self.minutes)
        expected = {"meeting": "Web Compatibility",
                    "date": "21 March 2017 - 6:00 PDT",
                    "minutes": "https://example.org/meetings/2017-03-21",
                    "scribe": "Aminata"}
        self.assertIs(type(actual), dict)
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
