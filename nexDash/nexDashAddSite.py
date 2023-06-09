# Jeff Comer
# script to add apic's to Nexus Dashboard
# Example input file is vars/<branch>/aci/switch-inventory.csv

import sys, getopt, csv
import requests, json
import urllib3
from nexDashOps import nexDashGetToken, nexDashAddSite


def main(argv):
    """
    Main execution routine

    :return: None
    """

    username = ""
    password = ""
    userArg = ""
    pwArg = ""

    argDict = {"username":"","password":"","infile":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:",["username","password","infile="])
    except getopt.GetoptError:
      print('imcDns.py -u <username> -p <password> -i <inputcsv>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('imcDns.py -u <username> -p <password> -i <inputcsv>')
         sys.exit()
      elif opt in ("-u", "--username"):
         userArg = arg
         argDict["username"] = userArg
      elif opt in ("-p", "--password"):
         pwArg = arg
         argDict["password"] = pwArg
      elif opt in ("-i", "--infile"):
         infileArg = arg
         argDict["infile"] = infileArg
    return argDict

if __name__ == '__main__':
    nexDashData = main(sys.argv[1:])
    newCookie = nexDashGetToken(nexDashData)
    nexDashAddSiteResult = nexDashAddSite(nexDashData, newCookie)