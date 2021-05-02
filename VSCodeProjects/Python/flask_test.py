from flask import Flask, render_template, jsonify
from datetime import datetime
import re
import json
import requests
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello world !"



@app.route('/dashboard')
def dashboard():
    return "Hello Dashboard !"



@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route('/api/meteo/')
def meteo():
    dictionnaire = {
        'type': 'Prévision de température',
        'valeurs': [24, 24, 25, 26, 27, 28],
        'unite': "degrés Celcius"
    }
    return jsonify(dictionnaire)


@app.route('/people/<username>')
def peoplelist(username):
    people = {
        "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": datetime.utcnow()
        },
        "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": datetime.utcnow()
        },
        "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": datetime.utcnow()
        },
        "Bkman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": datetime.utcnow()
        },
        "Brocan": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": datetime.utcnow()
        },
        "Bsdfsd": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": datetime.utcnow()
        },
        "Bkman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": datetime.utcnow()
        }
    }

    
    

    # result =  [(key, val) for key, val in people.items() if key.startswith(username)]
    # result =  [val for key, val in people.items() if key.startswith(username)]
    # result =  [key  for key, val in people.items() if key.startswith(username)]

    result = {}
    for key, value in people.items():
        if key.startswith(username):
            result[key] = value #Add slected item to the new dictionary

    list_result = [(k, v) for k, v in result.items()] 

    # return jsonify(result)
    return jsonify(list_result)
    # return result

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  requests.request.form['username']
    password = requests.request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})


if __name__ == "__main__":
    app.run(debug=True)