#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for creating the data structure."""

import unittest

from shoki import datacore
from fixtures import minutes_data

FIXTURE_DIR = './tests/fixtures/'

class TestShokiDatacore(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def tearDown(self):
        pass

    def read_minutes(self, minutes_fixture):
        """Reads the fixture for tests."""
        with open(FIXTURE_DIR + minutes_fixture) as f:
            minutes_fixture = f.read()
        return minutes_fixture

    def test_minutes_data(self):
        """Returns the appropriate data structure."""
        actual = minutes_data.minutes_data
        text = self.read_minutes('minutes_normal.txt')
        expected = datacore.minutes_as_data(text)
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
