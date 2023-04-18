import requests
import json
import sys, getopt, csv

def nxosAddFeature(specDict):

  with open(specDict['infile'], 'r') as csv_file:
      csvread = csv.DictReader(csv_file)
      csvDict = list(csvread)

  print(csvDict)
  for i in range(len(csvDict)):
    k = 0
    if(csvDict[i]['mgmtIP'] != ""):
      baseUrl = "http://" + csvDict[i]['mgmtIP'] + "/ins"
      headers={'content-type':'application/json'}
      print(csvDict[i]['feature'])
      print(csvDict[k]['feature'])
      for k in range(len(csvDict)):
        if(csvDict[k]['feature'] != ""):
          featureInput = "feature " + csvDict[k]['feature']
          payload={
            "ins_api": {
                "version": "1.0",
                "type": "cli_conf",
                "chunk": "0",
                "sid": "sid",
                "input": featureInput,
                "output_format": "json",
                "rollback": "stop-on-error"
            }
          }
          response = requests.post(baseUrl,data=json.dumps(payload), headers=headers,auth=(specDict['username'],specDict['password'])).json()

 