import urllib.request
from flask import Flask, jsonify
import json

def printResults(magnitude):

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
    # print out our customized results

    theJSON=json.loads(data)

  #  magnitude = float (input("Enter Magniture: "))
    disaster = []
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= magnitude:
            value = ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            disaster.append(value) 
    # length = len(disaster)
    # for x in range(length): 
    #     print (disaster[x])

    # #print (*disaster)
    return disaster


# if __name__ == "__main__":
#       printResults()     

    

    

