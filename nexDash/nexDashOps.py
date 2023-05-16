import urllib.request
import urllib3
import sys, time, os
import getopt
import requests
import csv, json, pprint
import random
from random import seed

nexDashBaseUrl = "https://198.18.133.100"

def nexDashGetToken(specDict):
    tokenUrl = nexDashBaseUrl + "/login"
    tokenHeader = {"content-type": "application/json"}
    tokenPayload = {"userName":specDict['username'],"userPasswd":specDict['password'],"domain":"DefaultAuth"}
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    tokenResponse = requests.post(tokenUrl, headers=tokenHeader, json=tokenPayload, verify=False)
    tokenJson = tokenResponse.json()
    token = tokenJson["token"]

    return token

