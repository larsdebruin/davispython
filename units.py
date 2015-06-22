import re
from math import pow, sqrt, exp

def FToC(value): 
    return (((value * 1.0) - 32.0) * 5.0) / 9.0 if value != None else None

def CtoFT(value):
    return  ((value * 9.0) / 5.0) + 32.0 if value != None else None

def InHgToHPa(value):
    return value / 0.02953 if value != None else None

def HPaToInHg(value):
    return value * 0.02953 if value != None else None

def HPaToMmHg(value):
    return value * 0.750062 if value != None else None

def MmHgToHPa(value):
    return value / 0.750062 if value != None else None

def InToMm(value): 
    return value * 25.4 if value != None else None

def MmToIn(value): 
    return value / 25.4 if value != None else None

def MpsToKt(value):
    return value / 0.514 if value != None else None

def KtToMps(value):
    return value * 0.514 if value != None else None

def MpsToKmh(value):
    return value * 3.6 if value != None else None

def KmhToMps(value):
    return value / 3.6 if value != None else None

def MphToMps(value): 
    return value / 2.2445 if value != None else None
    
def KmhToMph(value):
    return value * 0.62137119223733 if value != None else None
    
def MphToKmh(value): 
    return value * 1.609344 if value != None else None

def MpsToMph(value): 
    return value * 2.2445 if value != None else None
    
def MpsToBft(value):
    return pow((pow((value*3.6),2))/9, 1.0/3.0) if value != None else None

def BftToMps(value):
    return sqrt(pow(value, 3)*9)/3.6 if value != None else None
    
def calc_windchill(temperature,windspeed):
    # http://metlex.met.no/calc/kalk_windchill.htm
    # http://www.drammenweb.net/vindkjoling.htm
    # windspeed needs to be in km/h
    if ( ( windspeed > 5 ) and ( windspeed < 360 ) and ( temperature > -50 ) and ( temperature < 5) ):
      return round((13.12 + 0.6215 * temperature -11.37 * pow(windspeed,0.16) + 0.3965 * temperature * pow(windspeed,0.16)),2)
    else:
      return temperature
      
def calc_dewpoint(temperature,humidity):
    # http://pydoc.net/Python/weather/0.9.1/weather.units.temp/
    x = 1 - 0.01 * humidity;
    dewpoint = (14.55 + 0.114 * temperature) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * temperature) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * temperature) * x ** 14;
    dewpoint = temperature - dewpoint;
    return round(dewpoint,2)

def calc_cloudbase(temperature,dewpoint):
    # http://www.flightsim.no/ubbthreads/ubbthreads.php?ubb=showflat&Number=515190
    return round( ((temperature - dewpoint) * 100) / 0.8 + 100 ) 

def calc_heat_index(temperature,humidity):
    #
    #calculates the heat index based upon temperature (in F) and humidity.
    #http://www.srh.noaa.gov/bmx/tables/heat_index.html
    #returns the heat index in degrees F.
    #'''   
    if (temperature < 80):
        return temperature
    else:
        return -42.379 + 2.04901523 * temperature + 10.14333127 * humidity - 0.22475541 * \
               temperature * humidity - 6.83783 * (10 ** -3) * (temperature ** 2) - 5.481717 * \
               (10 ** -2) * (humidity ** 2) + 1.22874 * (10 ** -3) * (temperature ** 2) * \
               humidity + 8.5282 * (10 ** -4) * temperature * (humidity ** 2) - 1.99 * \
               (10 ** -6) * (temperature ** 2) * (humidity ** 2);

def rel_humidity(temperature,dewpoint):
    num = 112 - (0.1 * temperature) + dewpoint
    denom = 112 + (0.9 * temperature)
    rh = pow((num / denom), 8)
    return int(rh * 100)
    
