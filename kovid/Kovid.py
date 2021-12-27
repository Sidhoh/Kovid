import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

class GetGlobalData():
    globalData = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    jprint(globalData.json())

class GetCountryData():
    countryData = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
    jprint(countryData.json())