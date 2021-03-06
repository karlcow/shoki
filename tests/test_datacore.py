#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for creating the data structure."""

from unittest.mock import patch
import unittest

from tests.fixtures import minutes_data
from shoki import datacore

FIXTURE_DIR = "./tests/fixtures/"


class TestShokiDatacore(unittest.TestCase):
    """Tests for the core data structure."""

    test_config = {
        'topic_header': '#',
        'end': '--endtest--',
        'output_format': 'webcompatwiki',
        'topic_owner': '🔧'
    }

    def setUp(self):
        """Set up tests."""
        self.maxDiff = None

    def tearDown(self):
        """Tear down tests."""
        pass

    def read_minutes(self, minutes_fixture):
        """Read the fixture for tests."""
        with open(FIXTURE_DIR + minutes_fixture) as f:
            minutes_fixture = f.read()
        return minutes_fixture

    @patch('shoki.datacore.shoki_config.default_config', test_config)
    def test_minutes_data(self):
        """Return the appropriate data structure."""
        actual = minutes_data.minutes_data
        text = self.read_minutes("minutes_normal.txt")
        expected = datacore.minutes_as_data(text)
        self.assertDictEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
