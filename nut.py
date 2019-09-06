import urllib.request

import json

def printResults(data):
    theJSON=json.loads(data)

    magnitude = float (input("Enter Magniture: "))

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= magnitude :
            print ("%2.1f" % i["properties"]["mag"], i["properties"]["place"])        
    print ("--------------\n")
    

    
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
    # print out our customized results
        printResults(data)
    else:
        
        print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))


if __name__ == "__main__":
      main()
