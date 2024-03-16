import urllib.request
import json


def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print("counts:", count)

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-------------------------/n")

    for i in theJSON["features"]:
        if(i["properties"]["mag"] > 4.0):
            print(i["properties"]["place"])

def url():
    website = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(website)
    get_code= weburl.getcode()
    print(get_code)
    if (get_code == 200):
        data = weburl.read()
        printResults(data)
    else:
        print("bad url", weburl.getcode())

if __name__ == "__main__":
    url()
