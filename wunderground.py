#!/bin/env python

import urllib
import urllib2
import datetime
import units

def ToUnderground(data):
    stationid = 'INORDTRO5'
    password = 'Xtrdp6'
    url = 'http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php'
    
    getPars = {}
    getPars['action'] = 'updateraw'
    getPars['ID'] = stationid
    getPars['PASSWORD'] = password
    getPars['dateutc'] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    getPars['winddir'] = data['WindDir']
    getPars['tempf'] = data['TempOutF']
    getPars['windspeedmph'] = round(units.KmhToMph(data['WindSpeed']))
    getPars['humidity'] = data['HumOut']
    getPars['rainin'] = units.MmToIn(data['RainRate'])
    getPars['dailyrainin'] = units.MmToIn(data['RainDay'])
    getPars['baromin'] = units.HPaToInHg(data['Pressure'])
    getPars['dewptf'] = units.CtoFT(data['DewPoint'])
    getPars['softwaretype'] = 'Custom'
    
    
    
    full_url = url + '?' + urllib.urlencode(getPars)
    wudata = urllib2.urlopen(full_url)
    moreinfo = str.rstrip(wudata.read())
    
    if moreinfo != "success":
        print ("Could not upload data to Wunderground: %s") % moreinfo