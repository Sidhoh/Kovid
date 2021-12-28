import requests
import json

globalData = requests.get("https://coronavirus-19-api.herokuapp.com/all")

def get_global_data():
    return globalData.json()

def country_data(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    return data.json()

def get_global_cases():
    return globalData.json()['cases']

def get_global_deaths():
    return globalData.json()['deaths']

def get_global_recovered():
    return globalData.json()['recovered']

def get_country_cases(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    return data.json()['cases']

def get_country_deaths(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    return data.json()['deaths']

def get_country_recovered(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    return data.json()['recovered']

def get_country_active(country):
    data = requests.get("https://coronavirus-19-api.herokuapp.com/countries/" + country)
    return data.json()['active']
