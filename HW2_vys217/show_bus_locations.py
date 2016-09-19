'''Displays information about active vehicles for a given Bus Line
Author - Vishwajeet Shelar
Input Example: $ python show_bus_locations.py <MTA_KEY> <BUS_LINE>
Assumption: User has the MTA API Key and enters correct Bus Line
'''

from __future__ import print_function
import json
import urllib2 
import os
import sys

# Checks if both MTA key and Busline is entered
if len(sys.argv)<3:
    print('''Must pass the MTA key and Bus line
eg.$ python show_bus_locations.py <MTA_KEY> <BUS_LINE>
    ''')
    sys.exit()

apikey = sys.argv[1]
bus = sys.argv[2]

try:
    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s\
&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus)

    response = urllib2.urlopen(url)  
except urllib2.HTTPError:
    print("Incorrect MTA Key")
else:

    data = response.read().decode("utf-8")
    info = json.loads(data)
    
    if "ErrorCondition" in info["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]:
        print('Incorrect Bus Line')
        sys.exit()
        
#   Check the number of active buses
    print('Bus Line : ',bus)
    vehicles = (info["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    print ('Number of Active Buses :', str(len(vehicles)))
        
#   Print the longitude and latitude
    for i in range(len(vehicles)):
        loc = {}
        loc = vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]
        print('Bus {0} is at latititude {1} and longitude {2}'.format(i, loc['Latitude'], loc['Longitude']))

