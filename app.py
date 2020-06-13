#This is the main page that will route the user to the homepage and to the result page

from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)


@app.route('/result', methods=['POST'])
def result():
    information_mapper = {
        "new deaths": "NewDeaths",
        "total confirmed": "TotalConfirmed",
        "total recovered": "TotalRecovered"
    }
    location = request.form['local'].lower()
    question = request.form['question'].lower()
    r = requests.get('https://api.covid19api.com/summary')
    covid_19 = r.json()
    countries = covid_19.get('Countries')
    country_info = None
    for country in countries:
        if country.get('Country').lower() == location:
            info_key = information_mapper.get(question)
            country_info = country.get(info_key)
            break
    #0 Look at Covid1.py file
    #1 convert response to json
    #2 get countries list from json
    #3 create empty variable for storing country information
    #4 Loop through each country in country list - For loop
    #5 Compare country to country selection (location variable) - If statement
    #6 If 5 is true, set variable created in 3 to country
    #7 Break loop
    #8 come back to me

    return '{question}: {answer}'.format(question=question.title(), answer=country_info)
    #return render_template('result.html')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





