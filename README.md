# Kovid V1.0.0
A python api to get info on covid-19

# Installation and Usage
To install the api:

```
pip install git+git://github.com/sidhoh/Kovid.git
```

To import the api:

```python
import kovid
```
Usage:

```python
# To get global data
print(kovid.get_global_data())

# To get data from a country
print(kovid.get_country_data('USA'))

# To get global cases
print(kovid.get_global_cases())

# To get global deaths
print(kovid.get_global_deaths())

# To get global recovered
print(kovid.get_global_recovered())

# To get a country cases
print(kovid.get_country_cases('USA'))

# To get a country deaths
print(kovid.get_country_deaths('USA'))

# To get a country recovered
print(kovid.get_country_recovered('USA'))

# To get a country active
print(kovid.get_country_active('USA'))
```
