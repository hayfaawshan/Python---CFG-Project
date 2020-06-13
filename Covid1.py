import requests
import json
from pprint import pprint
#Country = input("Press enter for Global COVID-19 statistics ")
url = 'https://api.covid19api.com/summary'
response = requests.get(url)
#print(response)
covid_19 = response.json()
#pprint(covid_19)

# Find a country's cases of new deaths
countries = covid_19.get('Countries')
country_selection = input ('How many new cases of deaths? (type in a country) ')
new_deaths = None
for country in countries:
    if country.get('Country').lower() == country_selection.lower():
        new_deaths = country.get('NewDeaths')
        break

#print (new_deaths)
print(f'There are {new_deaths} new cases of deaths')

#
my_list = []
for country in countries:
    new_deaths1 = country['NewDeaths']
#    print(new_deaths)
# to add each value of the new death to my list so I have a series of intergers to work from and do math calculations.
    my_list.append(new_deaths1)
# make sure average is indenet otherwise the average calculation will be repeated in the loop and would give long list of averages
average = (sum(my_list) / len(my_list))
#print(average) - just to make sure I have the correct value

if new_deaths > average:
    print('This is  higher than the global average')

elif new_deaths < 200:
    print('This is lower than the global average')

else new_deaths = 200:
    print('This is the the global average')

# Find a country's cases of recovery
#country_selection1 = input ('How many new confirmed cases? (type  in a country) ')
#confirmed_cases = None
#for country in countries:
#    if country.get('Country').lower() == country_selection1.lower():
#        confirmed_cases = country.get('NewConfirmed"')

#print(confirmed_cases)
#print(f'There are {confirmed_cases} new confirmed cases')