#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Run the minutes."""

import argparse
import sys

from shoki import datacore


USAGE = """Usage:
shoki <command> [arg,[...]]
commands:
\tcreate
"""


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
        "-t", "--test", metavar="", help="Create sample minutes using the test file"
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
    else:
        print(USAGE)
        sys.exit()


if __name__ == "__main__":
    main()
