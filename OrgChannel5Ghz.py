import requests
import json

print('This script will help you pull data from multiple sites at once')
print('This version of the script will give you a list of the different 5GHz channels in use across the entire org')
print('Be sure you open the source code and enter your API key into the Authorization section of the headers variable for this to function')
# define the org here
print('Please enter the Org-ID you wish to poll:')
org = input()
url1 = 'https://api.mist.com/api/v1/orgs/{}/sites'.format(org)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ENTER TOKEN HERE'
}

siteidlist = []

sitelist = requests.get(url1, headers=headers)
sitejson = json.loads(sitelist.text)

for i in range(len(sitejson)):
    siteid = sitejson[i]["id"]
    siteidlist.append(siteid)

print('Here are the different site codes that are being polled within your org')
print(siteidlist)

channels5 = []


for i in range(len(siteidlist)):
    url2 = "https://api.mist.com/api/v1/sites/{}/stats/devices".format(siteidlist[i])
    devicestats = requests.get(url2, headers=headers)
    devicestatsjson = json.loads(devicestats.text)
    if ('radio_stat' in devicestats.text):
        print("Score! Active AP hardware found at:")
        print(siteidlist[i])
        a = len(devicestatsjson)
        count = 0
        while count < a:
            if ('radio_stat' in devicestatsjson[count]):
                channel = devicestatsjson[count]["radio_stat"]["band_5"]["channel"]
                print(channel)
                channels5.append(channel)
                count = count+1
            else:
                count = count+1
    else:
        print("The site below does not have currently active hardware:")
        print(siteidlist[i])

print('Here are the 5GHz channels in use across the org')
print(channels5)
