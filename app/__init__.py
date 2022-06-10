import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from the .env file

app = Flask(__name__)  # Initializes a Flask app

# os.getenv("API_KEY")  # Obtains the value of the .env variable containing the Google Maps API key

# Route for the landing page
@app.route('/')
def index():
    """
    Serves the landing page.
    """
    return render_template('index.html', title="Team Pythonic", url=os.getenv("URL"))

# Route for the profile page
@app.route('/profile/<name>')
def profile(name):
    """
    Loads profile dynamically from the JSON file and serves profile page.
    
    If profile could not be found, redirects to the landing page.
    """
    data = load_profiles_from_json('data.json')
    if name in data:
        info = data[name]
        return render_template('profile.html', name=name, info=info, url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))
    else:
        return index()


# Route for the projects page
@app.route('/projects')
def projects():

    data = load_profiles_from_json('projects.json')
    info1 = data['portfolio']
    info2 = data['strace']
    info3 = data['qa']
    info4 = data['weather']
    return render_template('projects.html', info1=info1, info2 = info2, info3 = info3, info4= info4,url=os.getenv("URL"))

# Route for the contact page
@app.route('/contact')
def contact():

    return render_template('contact.html', url=os.getenv("URL"))

# Route for the resume page
@app.route('/resume')
def resume():

    return render_template('resume.html', url=os.getenv("URL"))

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Serves the projects page.
    """
    return render_template("index.html")


def load_profiles_from_json(filename) -> dict:
    """
    Loads profile data by parsing the JSON file provided.

    :param: The JSON file to parse
    :return: A dict containing all the JSON info parsed
    """
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)
