'''Displays information on the next stop location of all busses 
of a given line and outputs a CSV file
Author - Vishwajeet Shelar
Input Example: 
$ python get_bus_info.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv
Assumption: User has the MTA API Key and enters correct Bus Line
'''

from __future__ import print_function
import json
import urllib2 
import os
import sys

# Checks if both MTA key and Busline is entered
if len(sys.argv)<4:
    print('''Must pass the MTA key and Bus line and name of CSV file
eg.$ python get_bus_info.py <MTA_KEY> <BUS_LINE> <FILE_NAME>.csv
    ''')
    sys.exit()

apikey = sys.argv[1]
bus = sys.argv[2]
f_name = sys.argv[3]

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
    
    f_dict = []
    vehicles = (info["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    
    #  Collect all data about latitude,longitude,stop_name, status
    for i in range(len(vehicles)):
        loc = {}
        stop_name = None
        status = None
        
        loc = vehicles[i]["MonitoredVehicleJourney"]["VehicleLocation"]
        try:
            if len(vehicles[i]['MonitoredVehicleJourney']['OnwardCalls']["OnwardCall"][0]["StopPointName"]) > 0:
                stop_name = vehicles[i]['MonitoredVehicleJourney']['OnwardCalls']["OnwardCall"][0]["StopPointName"]
        except:
            stop_name = 'N/A'
        
        try:   
            if len(vehicles[0]['MonitoredVehicleJourney']['OnwardCalls']["OnwardCall"][0]["Extensions"]\
["Distances"]["PresentableDistance"]) > 0:
                status = vehicles[0]['MonitoredVehicleJourney']['OnwardCalls']["OnwardCall"][0]["Extensions"]\
["Distances"]["PresentableDistance"]            
        except:
            status = 'N/A'

        f_dict.append((loc['Latitude'], loc['Longitude'],stop_name,status ))

#   Write the CSV file    
    doc = open(f_name,'w+')
    doc.writelines('Latitude,Longitude,Stop Name,Stop Status')
    doc.writelines('\n')
    for i in range(len(f_dict)):
        if i != 0:
            doc.writelines('\n')
        doc.writelines('{0},{1},{2},{3}'.format(f_dict[i][0], f_dict[i][1],f_dict[i][2], f_dict[i][3]))
    doc.close()
    
        
        
    