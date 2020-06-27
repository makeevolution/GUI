import urllib.request
import json
import time

while True:
    dataLink="https://bitbay.net/API/Public/BTC/all.json"
    data=urllib.request.urlopen(dataLink)
    data=data.read()
    data=json.loads(data)
    
    trans=data['transactions'][0]
    print(data['transactions'][0]['date'])
    
    print(data)
    time.sleep(2)
    
    