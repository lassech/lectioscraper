#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from __future__ import print_function
import requests
import re
from bs4 import BeautifulSoup
import httplib2
import os
import base64

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.errors import HttpError


import datetime
from datetime import tzinfo, timedelta, datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

################################################################################
# Indsæt skoleid og lærerid. Kan findes i webadressen til din lectio. 		   #
# Fx her 99 og 9999999999 skoleid og lærerid 								   #
# https://www.lectio.dk/lectio/99/SkemaNy.aspx?type=laerer&laererid=9999999999 #
# Uger er hvor lang tid frem du vil høste skemaet 							   #
# c_id er din calenderId. Find den i din google kalender.					   #
################################################################################
skoleid = "99"
lærerid = "9999999999"
uger = 3
c_id = "bjuua3gdbuc@group.calendar.google.com"

weekNumber = datetime.today().isocalendar()[1]
weekNumber = "{:02}".format(weekNumber)
###############################################################################


def google_create(event, idd):
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)

	try: 
			event = service.events().insert(calendarId=c_id, body=event).execute()
	except HttpError as err:
			if err.resp.status == 409:
					event = service.events().get(calendarId=c_id, eventId=idd).execute()
					updated_event = service.events().update(calendarId=c_id, eventId=event['id'], body=event).execute()


			else:
					raise err
def getidid (ido):
	idd = str(ido)
	iddf = idd.index("=") +1
	iddl = idd.index("&")
	idd = idd[iddf:iddl]
	lidd = "lo" + lærerid
	idd = lidd + idd
	idd = idd.replace("aktivitetforside2.aspx?absid=", "")
	idd = idd.replace("/", "")
	return idd

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def getugeskema(url):
	url.status_code
	url.headers
	c = url.content
	soup = BeautifulSoup(c, "lxml")
	samples = soup.find_all("a", "s2skemabrik")


	#søger skemabrikkerne
	for link in samples:
		ido = (link.get("href"))
		link = str(link)
		if ido:  #hvis der er id
			if "Hele dagen" not in link: #sørger for at topbrikkerne topbrikkerne kommer frem
				date = re.search("\d{1,2}/\d{1,2}-\d{4} (?:Hele dagen|\d{2}:\d{2} til "
	                      		"(?:\d{1,2}/\d{1,2}-\d{4} )?\d{2}:\d{2})", link)
				dayend = date[0].index('/')
				day = str(date[0])[0:dayend]
				day = int(day)
				monthend = date[0].index('-')
				month = str(date[0])[dayend + 1:monthend]
				month = int(month)
				yearend = date[0].index(' ')
				year = str(date[0])[monthend+1:yearend]
				year = int(year)
				## startime first digits
				starttimefbegin = str(date[0]).index(":") -2
				starttimefend = str(date[0]).index(":") 
				starttimef = str(date[0])[starttimefbegin:starttimefend]
				starttimef = int(starttimef)
				# start time last digits
				starttimelbegin = str(date[0]).index(":") +1
				starttimelend = str(date[0]).index(":") +3
				starttimel = str(date[0])[starttimelbegin:starttimelend]
				starttimel = int(starttimel)
				#endtime first digits
				endtimefbegin = str(date[0]).rindex(":") -2
				endtimefend = str(date[0]).rindex(":") 
				endftime = str(date[0])[endtimefbegin:endtimefend]
				endftime = int(endftime)					
				#endtime last digits
				endtimelbegin = str(date[0]).rindex(":") +1
				endtimelend = str(date[0]).rindex(":") +3
				endltime = str(date[0])[endtimelbegin:endtimelend]
				endltime = int(endltime)
				#fjerner uvigtige dele af infoformationem
				link = link.replace(str(date[0]), "")
				link = (link.replace('"', ' ', 3))
				s='data-additionalinfo='
				linkfirst = link.rindex(s) + len(s) +1
				linklast = link.index('" ')
				lectioinfo = str(link)[linkfirst:linklast]
				lectioinfo = lectioinfo.replace("Ændret!", "")
				#inserts into lectio calendar
				#credentials = get_credentials()
				#http = credentials.authorize(httplib2.Http())
				#service = discovery.build('calendar', 'v3', http=http)
				idd =  getidid(ido)
				event = {
					 'summary': lectioinfo,
					 'id': idd,
					# 'location': 'København',
					# 'description': 'A chance to hear more about Google\'s developer products.',
					 'start': {
					   'dateTime': str(datetime(year, month, day,starttimef,starttimel).isoformat('T')),
					   'timeZone': 'Europe/Copenhagen',
					 },
					 'end': {
					   'dateTime': str(datetime(year, month, day,endftime,endltime).isoformat('T')),
					   'timeZone': 'Europe/Copenhagen',
					   'status': 'confirmed'
					 },

				}
				if "Aflyst" not in link: #eksporterer elementer som ikke er aflyst
				
					
					print ("Følgende modul er eksporteret:")
					print (event)
					print ("")			
					google_create(event, idd)
					
													
				if "Aflyst!" in link:
					idd =  getidid(ido)
					credentials = get_credentials()
					http = credentials.authorize(httplib2.Http())
					service = discovery.build('calendar', 'v3', http=http)
					try: 
						event = service.events().get(calendarId=c_id, eventId=idd).execute()
						event['status'] = 'cancelled'
						updated_event = service.events().update(calendarId=c_id, eventId=event['id'], body=event).execute()
					except HttpError as err:
							if err.resp.status == 404:
								print ("aflyst")
							else:
								raise err
				if "Ændret!" in link:
					idd =  getidid(ido)
					credentials = get_credentials()
					http = credentials.authorize(httplib2.Http())
					service = discovery.build('calendar', 'v3', http=http)
					try: 
						event = service.events().get(calendarId=c_id, eventId=idd).execute()
						event['summary'] = lectioinfo
						updated_event = service.events().update(calendarId=c_id, eventId=event['id'], body=event).execute()
					except HttpError as err:
							if err.resp.status == 404:
								print ("aflyst")
							else:
								raise err



get_credentials()
i = 0
while i < uger:
	weekNumber = int(weekNumber)+i
	weekNumber = "{:02}".format(weekNumber)
	print ("Nu hentes skemaet fra uge nr." + weekNumber)
	url = "https://www.lectio.dk/lectio/{}/SkemaNy.aspx?type=laerer&laererid={}&week={}{}".format(skoleid, lærerid, str(weekNumber), datetime.today().year)
	url = requests.get(url)
	getugeskema(url)
	i = i+1