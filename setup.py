#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Shoki setup."""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='shoki',
    version='1.0.1',
    description='Generate minutes from a text file',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/karlcow/shoki',
    author='Karl Dubost',
    author_email='karl+shoki@la-grange.net',
    license='MPL',
    classifiers=[
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=["shoki"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "shoki=shoki.cli:main",
        ]
    },
)
