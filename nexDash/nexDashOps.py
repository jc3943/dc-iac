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

def nexDashAddSite(specDict, cookie):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    siteUrl = nexDashBaseUrl + "/nexus/api/sitemanagement/v4/sites"
    sitePayload = {"spec":{"host":csvDict[0]['apicIp'],"latitude":"10","name":"dCloud","password":"C1sco12345","siteType":"ACI","userName":"admin"}}


