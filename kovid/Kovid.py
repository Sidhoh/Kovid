import requests
import json

def __jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_global_data():
    globalData = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    __jprint(globalData.json())

def get_countries_data():
    countries = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
    __jprint(countries.json())

def get_country_data(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    __jprint(data.json())
