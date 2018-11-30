#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Run the minutes."""

import argparse
import json
import logging
import pathlib
import sys

from shoki import datacore
from shoki import shoki_config


# APPLICATION MESSAGES
USAGE = """Usage:
shoki <command> [arg,[...]]
commands:
\tcreate
\t\tWill create the minutes of your meeting
\tinit
\t\tWill create a config file the first time
"""
CONFIG_EXIST = """User configuration already exists.
You may manually edit the JSON file at:
{loc}
"""

# LOGGING
log = logging.getLogger(__name__)


def create(args):
    """CLI for creating minutes with shoki."""
    parser = argparse.ArgumentParser(
        description="shoki is formatting your minutes.",
        argument_default=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--location",
        metavar="location",
        type=str,
        nargs="?",
        help="Location of the minutes (file:// or http://)",
    )
    parser.add_argument(
        "-t", "--test",
        metavar="",
        help="Create sample minutes using the test file"
    )
    parser.add_argument(
        "--out_format",
        metavar="out_format",
        type=str,
        nargs="?",
        help="Format of the output",
    )
    parsed_args = vars(parser.parse_args(args))
    return datacore.create_minutes(**parsed_args)


def init():
    """Initialize shoki project."""
    user_config_file = shoki_config.USER_CONFIG_FILE
    user_config_path = shoki_config.USER_CONFIG_PATH
    if not pathlib.Path(user_config_file).exists():
        user_config_path.mkdir(mode=0o700, parents=True, exist_ok=True)
        log.debug('Created user config dir {dir}'.format(dir=user_config_path))
        create_user_config(user_config_file)
    else:
        print(CONFIG_EXIST.format(loc=user_config_file))


def create_user_config(user_config_file):
    """Create a user config file."""
    data = json.dumps(shoki_config.default_config,
                      ensure_ascii=False, sort_keys=True, indent=4)
    user_config_file.write_text(data)
    log.info('Created new user config file')


def main():
    """Core for the CLI."""
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit()

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "create":
        content = create(args)
        print(content)
    elif command == "init":
        init()
    else:
        print(USAGE)
        sys.exit()

if __name__ == "__main__":
    main()
