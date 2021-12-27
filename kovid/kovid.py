import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_global_data():
    globalData = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    jprint(globalData.json())

def get_countries_data():
    countries = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
    jprint(countries.json())
