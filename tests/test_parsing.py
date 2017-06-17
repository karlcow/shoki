#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for parsing Meeting Minutes."""

import unittest

from shoki.parsing import meeting_date

FIXTURE_DIR = './tests/fixtures/'


class TestShokiParsing(unittest.TestCase):
    def setUp(self):
        self.minutes = self.read_minutes('minutes_normal.txt')

    def tearDown(self):
        pass

    def read_minutes(self, minutes_fixture):
        """Reads the fixture for tests."""
        with open(FIXTURE_DIR + minutes_fixture) as f:
            minutes_fixture = f.read()
        return minutes_fixture

    def test_meeting_date(self):
        """Extract the meeting date."""
        actual = meeting_date(self.minutes)
        expected = '2017-03-21'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
