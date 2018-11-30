#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Config elements for shoki."""

import json
import pathlib

# Define the root of this directory
ROOT = pathlib.Path.cwd()
MINUTES_SAMPLE = './tests/fixtures/minutes_normal.txt'
MINUTES_LOCATION = pathlib.Path(ROOT, MINUTES_SAMPLE).as_uri()

# USER CONFIGURATION
USER_PATH = pathlib.Path.home()
USER_CONFIG_PATH = USER_PATH / '.shoki'
CONFIG_NAME = 'shoki_config.json'
USER_CONFIG_FILE = pathlib.Path(USER_CONFIG_PATH, CONFIG_NAME)

if pathlib.Path(USER_CONFIG_FILE).exists():
    # we use the local user configuration file
    data = USER_CONFIG_FILE.read_text()
    default_config = json.loads(data)
else:
    # use these defaults
    default_config = {
        'end': '--end--',
        'output_format': 'webcompatwiki',
        'topic_header': '#',
        'topic_owner': '👹',
    }

# MESSAGES
FORMAT_ERROR = """
The formatter has failed.
The file you are dealing with is probably in the wrong format.
shoki accepts only plain text files.

Error: {error}
"""
