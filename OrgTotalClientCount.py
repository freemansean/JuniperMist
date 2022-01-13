import requests
import json

print('This script will help you pull data from multiple sites at once')
print('This version of the script will give you a total count of wireless clients connected across your org')
print('Be sure you open the source code and enter your API key into the Authorization section of the headers variable for this to function')
# define the org here
print('Please enter the Org-ID you wish to poll:')
org = input()
url1 = 'https://api.mist.com/api/v1/orgs/{}/sites'.format(org)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'ENTER TOKEN HERE'
}

siteidlist = []

sitelist = requests.get(url1, headers=headers)
sitejson = json.loads(sitelist.text)

for i in range(len(sitejson)):
    siteid = sitejson[i]["id"]
    siteidlist.append(siteid)

print('Here are the different site codes that are being polled within your org')
print(siteidlist)

totalclients = 0

for i in range(len(siteidlist)):
    url2 = "https://api.mist.com/api/v1/sites/{}/clients/search".format(siteidlist[i])
    clients = requests.get(url2, headers=headers)
    clientsjson = json.loads(clients.text)
    sitecount = len(clientsjson)
    totalclients = (totalclients + sitecount)

print('Here are the total number of wireless clients connected across this org')
print(totalclients)
