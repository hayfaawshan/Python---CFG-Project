#This is the main page that will route the user to the homepage and to the result page

from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)


@app.route('/result', methods=['POST'])
def result():
    location = request.form['local']
    r = requests.get('https://api.covid19api.com/total/country/' +location )
    json_object = r.text
    return json_object
    #return render_template('result.html')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





