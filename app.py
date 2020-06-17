#This is the main page that will route the user to the homepage and to the result page

from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)


@app.route('/result', methods=['POST'])
def result():
    location = request.form['local'].lower()
    r = requests.get('https://api.covid19api.com/summary')
    covid_19 = r.json()
    countries = covid_19.get('Countries')
    number_of_cases = 0
    total_deaths = 0
    total_recovered = 0

    for country in countries:
        if country.get('Country').lower() == location:
            number_of_cases = country.get('TotalConfirmed')
            total_deaths = country.get('TotalDeaths')
            total_recovered = country.get('TotalRecovered')
            break


    return render_template('result.html', cases=number_of_cases, deaths=total_deaths, recovered=total_recovered, location=location)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





