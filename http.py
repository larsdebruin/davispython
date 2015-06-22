#!/bin/env python
import urllib

class httppost:
   def post(self,data):
      #location = 'asen'
      #stationtype = 'davisvp2'
      siteid = 1
      params = urllib.urlencode({'BarTrend': data['BarTrend'], 'Pressure': data['Pressure'], 'TempIn': data['TempIn'], 'HumIn': data['HumIn'], 'TempOut': data['TempOut'], 
'WindSpeed': data['WindSpeed'], 'WindSpeed10Min': data['WindSpeed10Min'], 'WindDir': data['WindDir'], 'HumOut': data['HumOut'], 'RainRate': data['RainRate'], 
'RainStorm': data['RainStorm'], 'RainDay': data['RainDay'], 'RainMonth': data['RainMonth'], 'RainYear': data['RainYear'], 'ForecastIcon': data['ForecastIcon'], 
'CloudBase': data['CloudBase'], 'HeatIndex': data['HeatIndex'], 'DewPoint': data['DewPoint'], 'RelHum': data['RelHum'], 'WindChill': data['WindChill'], 
'ForecastRuleNo': data['ForecastRuleNo'], 'siteid': siteid })
      f = urllib.urlopen("http://www.larsdebruin.net/index.php/upload/weather/", params)
      #print params
      #print f.read()

