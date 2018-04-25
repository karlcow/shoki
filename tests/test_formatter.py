#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Tests for formatting the minutes data into a text."""

import unittest

from shoki import formatter


class TestShokiFormatter(unittest.TestCase):
    """Tests for the text formatting."""

    def setUp(self):
        """Set up tests."""
        pass

    def tearDown(self):
        """Tear down tests."""
        pass

    def test_convert_unknown_format(self):
        """Returns the appropriate data structure."""
        with self.assertRaises(SystemExit) as err:
            formatter.convert([], "zorglub")
        self.assertEqual("This zorglub format does not exist yet.", str(err.exception))


if __name__ == "__main__":
    unittest.main()
