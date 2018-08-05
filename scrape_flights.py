#!/usr/bin/env python2.7

# scrape and filter launch dates to save in a database

import requests
import os
import re
import sys

# set some defaults

LIMIT=10

# usage function

def usage(status=0):
    print 'Usage: TBD!'
    sys.exit(status)

args = sys.argv[1:]

while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    # TODO: Parse command line arguments
    if arg == '-h':
        usage(0)
    else:
        usage(1)

if len(args) > 1:
    usage(1)

# define the url and header for fetching spaceflight data
URL = 'https://spaceflightnow.com/launch-schedule/'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0)\
        Gecko/20100101 Firefox/10.0'}

# function to obtain the necessary JSON data
def get_JSON(input_url, input_header):

    response = requests.get(input_url, headers=input_header)

    if response.status_code != 200:
        print 'spaceflight website unavailable :('
        sys.exit(1)
    else:
        print 'reached ' + URL + ' successfully'

    print response.text


get_JSON(URL, headers)


