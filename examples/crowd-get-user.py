from pprint import pprint
from atlassian import Crowd
import os
import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

CROWD_URL = os.environ.get('CROWD_URL', 'http://localhost:8085/crowd')
CROWD_APPLICATION = os.environ.get('CROWD_APPLICATION', 'bamboo')
CROWD_APPLICATION_PASSWORD = os.environ.get('CROWD_APPLICATION_PASSWORD', 'admin')

crowd = Crowd(
    url=CROWD_URL,
    username=CROWD_APPLICATION,
    password=CROWD_APPLICATION_PASSWORD)

user_details = crowd.user('xdfjklm')
pprint(user_details)
