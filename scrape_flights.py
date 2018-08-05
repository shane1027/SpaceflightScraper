#!/usr/bin/env python2.7

# scrape and filter launch dates to save in a database

import requests
import os
import re
import sys
from bs4 import BeautifulSoup

# set default mission dictionary format

mission_default = {
    "date":"None",
    "vehicle":"None",
    "location":"None:",
    "name":"None",
    "time":"None",
    "description":"None"
}

missions = list()

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

    # scrape webpage information
    response = requests.get(input_url, headers=input_header)

    if response.status_code != 200:
        print 'spaceflight website unavailable :('
        sys.exit(1)
    else:
        print 'reached ' + URL + ' successfully'

    # transform into useful content
    soup = BeautifulSoup(response.content, 'html.parser')

    # extract the date, name, and vehicle
    for datename in soup.find_all('div', class_='datename'):
        tmp_dict = {}

        # the vehicle and name are separated by a bullet point
        combined = datename.find('span',
            class_='mission').get_text().split(u"\u2022")

        tmp_dict['vehicle'] = combined[0].strip()
        tmp_dict['name'] = combined[1].strip()
        tmp_dict['date'] = datename.find('span',
                class_='launchdate').get_text()
        missions.append(tmp_dict)

    # extract the launch time and site
    i = 0
    for timesite in soup.find_all('div', class_='missiondata'):

        combined= timesite.get_text().split('\n')

        ##TODO: handle 'approx.' times here
        missions[i]['time'] = combined[0].split(':')[1].strip().split(' ')[0].strip()

        missions[i]['location'] = combined[1].split(':')[1].strip()
        i = i+1

    print missions





get_JSON(URL, headers)


