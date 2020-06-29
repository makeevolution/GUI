import urllib.request
import json
import numpy as np
import pandas as pd
import time

while True:
    #dataLink="https://bitbay.net/API/Public/BTC/trades.json"
    dataLink="https://api.coindesk.com/v1/bpi/historical/close.json"
    data=urllib.request.urlopen(dataLink)
    data=data.read()
    data=json.loads(data)
    data=pd.DataFrame(data) #pandas DataFrame will convert
                            #the keys into heading of a table and
                            #the values of each key as the rows
    #data['time']=np.array(data['time']).astype("datetime64[s]")


#     buys=data[data['type']=="buy"]
#     buys['date']=np.array(buys['date']).astype("datetime64[s]")
#     buyDates=(buys['date']).tolist()
#     
#     sells=data[data['type']=="buy"]
#     sells['date']=np.array(buys['date']).astype("datetime64[s]")
#     sellDates=(sells['date']).tolist()

    print(data['time'])
    
    time.sleep(2)
    
    