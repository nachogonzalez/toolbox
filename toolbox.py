import json
import os
import logging
import datetime
import requests

# Hardcoded variables (to be extracted into other dedicated module)
LOG_FILE = "logs/WeatherMan.log" #Init this variable with the project specifications.
API_KEY = "33374ad19b134b3003cb38b0851e2094"

# ****** Log configuration and initialization ******

def loggingInitialization():
	file = open(LOG_FILE, "w")
	timestamp = datetime.datetime.now()
	file.close()
	logging.basicConfig(
		filename = LOG_FILE, 
		encoding = 'utf-8', 
		level = logging.INFO, 
		format='%(asctime)s %(levelname)-8s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S')
	logging.info("Logging system initialized \n")
	
# ****** JSON parsing ******

def loadJSONfile(jsonfile):
	# We use the “latin-1” encoding to map byte values directly to the first 256 Unicode code points
	with open('data/city.list.json', encoding='latin-1') as f:
		data = json.load(f)
	f.close()
	return data
