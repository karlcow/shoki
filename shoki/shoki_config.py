#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Config elements for shoki."""

import os
from urllib.parse import urljoin

# Define the root of this directory
ROOT = os.getcwd()
# Parsing format
# The characters used for marking up the title of a discussion
TOPIC_HEADER = "#"
# string to stop parsing
END = "===========AGENDA ITEMS ABOVE THIS LINE==========="
# Default location for the minutes.
# Can be a URL on the Web or a text file on the computer
MINUTES_PATH = os.path.join(ROOT, "./tests/fixtures/minutes_normal.txt")
LOCATION = urljoin("file://", MINUTES_PATH)
