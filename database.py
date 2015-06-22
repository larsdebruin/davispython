#!/bin/env python
import MySQLdb
from warnings import filterwarnings

class mysql:
    def __init__(self):
        
        database = 'weather'
        host = 'tor.larsdebruin.net'
        port = 3306
        user = 'weather'
        password = 'suZ7fQUKEtbxSEZt'
    
        try:
          self.db = MySQLdb.connect(db=database,host=host,port=port,user=user,passwd=password)
          filterwarnings('ignore', category = MySQLdb.Warning)
        except MySQLdb.Error, e:
          print("Unable to connect to MySQL, Error %d: %s" % (e.args[0], e.args[1]))
    
    def insert(self,data):
      c=self.db.cursor()
      query = 'INSERT INTO archive (time,bar_trend,barometer,temp_in,hum_in,temp_out,wind_speed,\
wind_10m_avg_speed,wind_direction,hum_out,rain_rate,rain_storm,rain_day,rain_month,rain_year,forecast_icon,cloud_base,heat_index, dewpoint, rel_hum, wind_chill, forecast_rule) VALUES \
(now(),\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\'\
,\'%s\',\'%s\',\'%s\');' % (data['BarTrend'], data['Pressure'], data['TempIn'], data['HumIn'],
data['TempOut'], data['WindSpeed'], data['WindSpeed10Min'], data['WindDir'], data['HumOut'], data['RainRate'], data['RainStorm'], 
data['RainDay'], data['RainMonth'], data['RainYear'], data['ForecastIcon'], data['CloudBase'], data['HeatIndex'],data['DewPoint'],data['RelHum'],data['WindChill'],data['ForecastRuleNo'])
      try:
        c.execute(query)
        self.db.commit()
      except self.db.Error, e:
        print("Could not insert data into database error %d: %s" % (e.args[0], e.args[1]))
        
    def insert_realtime(self,data):
      c=self.db.cursor()
      query = 'REPLACE INTO realtime (time,value) VALUES (now(),\'%s\');' % (data)
      try:
        c.execute(query)
        self.db.commit()
      except self.db.Error, e:
        print("Could not insert data into database error %d: %s" % (e.args[0], e.args[1]))