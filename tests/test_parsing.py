#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for parsing Meeting Minutes."""

from unittest.mock import patch
import unittest

from shoki.parsing import extract_blocks
from shoki.parsing import extract_prose
from shoki.parsing import extract_todo
from shoki.parsing import extract_topic
from shoki.parsing import meeting_date
from shoki.parsing import meta_headers

FIXTURE_DIR = "./tests/fixtures/"


class TestShokiParsing(unittest.TestCase):
    """Test the parsing rules for the minutes."""

    def setUp(self):
        """Set up the tests."""
        self.minutes = self.read_minutes("minutes_normal.txt")
        self.minutes_basic = self.read_minutes("minutes_normal_no_cruft.txt")
        self.headers = meta_headers(self.minutes)

    def tearDown(self):
        """Tear down the tests."""
        pass

    def read_minutes(self, minutes_fixture):
        """Read the fixture for tests."""
        with open(FIXTURE_DIR + minutes_fixture) as f:
            minutes_fixture = f.read()
        return minutes_fixture

    def test_meeting_date(self):
        """Extract the meeting date."""
        self.assertEqual(meeting_date(
            "30 October 2017 - 08:00 USA Central time"), "2017-10-30"
        )
        self.assertEqual(
            meeting_date("3 March 2017 - 08:00 USA Central time"), "2017-03-03"
        )
        self.assertEqual(meeting_date("3 March 2017 - 1:00 PDT"), "2017-03-03")

    def test_meta_headers(self):
        """Return the dictionary for meeting metatada."""
        actual = meta_headers(self.minutes)
        expected = {
            "meeting": "Web Compatibility",
            "date": "21 March 2017 - 6:00 PDT",
            "minutes": "https://example.org/meetings/2017-03-21",
            "scribe": "Aminata",
        }
        self.assertIs(type(actual), dict)
        self.assertDictEqual(actual, expected)

    def test_topic_owner(self):
        """Extract the topic and owner of a discussion."""
        actual = extract_topic("# Walden (Henry David Thoreau) ")
        expected = {"topic": "Walden", "owner": "Henry David Thoreau"}
        self.assertIs(type(actual), dict)
        self.assertDictEqual(actual, expected)
        actual2 = extract_topic("# topic without owner")
        expected2 = {"topic": "topic without owner", "owner": None}
        self.assertIs(type(actual2), dict)
        self.assertDictEqual(actual2, expected2)
        actual3 = extract_topic("#topic and spaces(owner)")
        expected3 = {"topic": "topic and spaces", "owner": "owner"}
        self.assertIs(type(actual3), dict)
        self.assertDictEqual(actual3, expected3)

    @patch('shoki.datacore.shoki_config.END', '--endtest--')
    def test_minutes_blocks(self):
        """Extract minutes into blocks."""
        actual = extract_blocks(self.minutes_basic)
        expected = [
            {
                "prose": ["Intro1", "speaker1: Été", "speaker2: 愛"],
                "topic_line": "# Topic1 (Owner1)",
            },
            {
                "prose": ["Intro2", "speaker1: Blah", "speaker2: Booh"],
                "topic_line": "# Topic2 (Owner2)",
            },
        ]
        self.assertIs(type(actual), list)
        self.assertListEqual(actual, expected)

    @patch('shoki.datacore.shoki_config.END', '--endtest--')
    def test_from_blocks_to_structure(self):
        """Extract the discussion structure from list of lines."""
        blocks = extract_blocks(self.minutes)
        # Let's first test the Walden block
        walden = blocks[0]["prose"]
        actual = extract_prose(walden)
        expected = (
            [
                {"speaker": "henry", "said": "To be awake is to be alive."},
                {
                    "speaker": "david",
                    "said": "I have always been regretting that I was not as wise as the day I was born.",  # noqa: E501
                },
            ],
            "Let us first be as simple and well as Nature ourselves, dispel the clouds which hang over our brows, and take up a little life into our pores. Do not stay to be an overseer of the poor, but endeavor to become one of the worthies of the world.",  # noqa: E501
        )  # noqa: E501
        self.assertIs(type(actual), tuple)
        self.assertTupleEqual(actual, expected)
        worth = blocks[4]["prose"]
        actual = extract_prose(worth)
        expected = (
            [
                {
                    "speaker": "julien",
                    "said": "there was no description, but I'm fine.",
                },
                {
                    "speaker": "gracq",
                    "said": "And the scribe minutes me on multiple lines because he can. sometimes with spaces.",  # noqa: E501
                },
                {
                    "owner": "julien",
                    "todo": "check if it break the tests.",
                    "deadline": "2017-06-20",
                },
                {
                    "deadline": "2017-06-21",
                    "owner": "paul",
                    "todo": "test if action and todo are handled the same.",
                },
            ],
            "",
        )
        self.assertTupleEqual(actual, expected)
        non_verbal = blocks[3]["prose"]
        actual = extract_prose(non_verbal)
        expected = ([], "I am rooted, but I flow.")
        self.assertTupleEqual(actual, expected)

    def test_extract_todo(self):
        """Todo lines are parsed correctly."""
        flag = "TODO"
        text = "julien to check if it break the tests. 2017-06-20"
        actual = extract_todo(flag, text)
        expected = {
            "owner": "julien",
            "todo": "check if it break the tests.",
            "deadline": "2017-06-20",
        }
        self.assertIs(type(actual), dict)
        self.assertDictEqual(actual, expected)
        flag = "ACTION"
        text = "paul to test if action and todo are handled the same. 2017-06-21"  # noqa
        actual = extract_todo(flag, text)
        expected = {
            "owner": "paul",
            "todo": "test if action and todo are handled the same.",
            "deadline": "2017-06-21",
        }
        self.assertIs(type(actual), dict)
        self.assertDictEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
