#!/usr/bin/env python
# thecloud.py - Micro-sized Twitter client.
# Copyright (C) 2012  Amanda Folson <amanda@incredibl.org>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys
import tweepy

CONSUMER_KEY = 'H0bdGOfmNffauOUwMqjViw'
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

statuses = ['Welcome to Linodecom.', 'This is Linodecom.', 'Welcome.', 'You can do anything at Linodecom.', 'Anything at all.', 'The only limit is yourself.', 'Yes.', 'This is Linodecom and welcome to you who have come to Linodecom.', 'Anything is possible at Linodecom.', 'You can do anything at Linodecom.', 'The infinite is possible at Linodecom.', 'The unattainable is unknown at Linodecom.']

from random import choice
api.update_status(choice(statuses))
