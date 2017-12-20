#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# flake8: noqa
"""Data examples for a meeting record."""

minutes_data = {
    'title': 'Web Compatibility',
    'scribe': ['Aminata', ],
    'meeting_date': '2017-03-21',
    'attendees': [],
    'record': [
        {'topic': 'Walden',
         'owner': 'Henry David Thoreau',
         'discussion': [
            {'speaker': 'henry',
             'said': 'To be awake is to be alive.'},
            {'speaker': 'david',
             'said': 'I have always been regretting that I was not as wise as the day I was born.'},],
         'intro': 'Let us first be as simple and well as Nature ourselves, dispel the clouds which hang over our brows, and take up a little life into our pores. Do not stay to be an overseer of the poor, but endeavor to become one of the worthies of the world.'
         },
        {'topic': 'A Moveable Feast',
         'owner': 'Hemingway',
         'discussion': [
            {'said': 'We would have to shut the windows in the night against the rain and the cold wind would strip the leaves from the trees in the Place Contrescarpe. https://en.wikipedia.org/wiki/Ernest_Hemingway',
             'speaker': 'ernest'},
            {'said': 'The leaves lay sodden in the rain and the wind drove the rain against the big green autobus at the terminal and the Café des Amateurs was crowded and the windows misted over from the heat and the smoke inside.',
             'speaker': 'hemingway'},],
         'intro': 'Then there was the bad weather. It would come in one day when the fall was over.',
        },
        {'topic': 'Topic without owner',
         'owner': None,
         'discussion': [
            {'said': 'Who proposed this?',
             'speaker': 'virginia'},
            {'said': 'No idea, but is it really worth discussing?',
             'speaker': 'woolf'},],
         'intro': "It's happening sometimes that people forget to own an agenda item."
        },
        {'topic': 'Non verbal updates',
         'owner': 'Virginia Woolf',
         'discussion': [],
         'intro': 'I am rooted, but I flow.'
        },
        {'topic': 'Worth discussing',
         'owner': 'Julien Gracq',
         'discussion': [
            {'said': "there was no description, but I'm fine.",
             'speaker': 'julien'},
            {'said': 'And the scribe minutes me on multiple lines because he can. sometimes with spaces.',
             'speaker': 'gracq'},
            {'deadline': '2017-06-20',
             'owner': 'julien',
             'todo': 'check if it break the tests.'},
            {'deadline': '2017-06-21',
             'owner': 'paul',
             'todo': 'test if action and todo are handled the same.'},],
         'intro': '',
        }
    ]

}
