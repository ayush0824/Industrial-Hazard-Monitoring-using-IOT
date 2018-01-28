#Temperature analysis using Raspberry-Pi and DS18B20 sensor - Ayush Dwivedi
import os
import requests
import glob
import time
import httplib
import urllib
key=’5T1VDDGI9H83QY’
os.system(’modprobe w1-gpio’)
os.system(’modprobe w1-therm’)
base_dir = ’/sys/bus/w1/devices/’
device_folder = glob.glob(base_dir + ’28*’)[0]
device_file = device_folder + ’/w1_slave’
def read_temp_raw():
    f = open(device_file, ’r’)
    lines = f.readlines()
    f.close()
    return lines
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != ’YES’:
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find(’t=’)
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        if temp_c > 55:

            res = requests.get(’https://api.simplepush.io/send/ji_4_d/
            High Temperature Alert/Temperature exceeded the safe value’)
#res2 = requests.get(’https://api.thingspeak.com/update?
            api_key=XWG85OR8_0_HU&Temperature=temp_c’)
    return temp_c
def temp_analysis():
    while True:
        temp = read_temp()
        params = urllib.urlencode({’field1’: temp, ’key’:key })
        headers = {"Content-typZZe": "application/x-www-form-urlencoded",
        "Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print ’Current temperature is ’, temp, ’(deg. Celsius)’
    print ’Status:’,response.status, ’,’,response.reason
    print(’\n’)
    data = response.read()
    conn.close()
except:
    print ("Connection failed...")
break
while True:
    temp_analysis()
    time.sleep(1)
