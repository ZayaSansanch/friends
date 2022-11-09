import json
from flask import Flask, redirect, render_template, request
import requests


app = Flask(__name__)


friends_path = "./json/friends.jspn"
peples_path = "./json/peples.json"
site_data_path = "./json/site_data.json"


def get_json(path):
    with open(path, "r") as infile:
        return json.load(infile)
def set_json(path):
    with open(path, "w") as outfile:
        outfile.write(json.dumps(path, indent=4))

@app.route('/', methods=['GET', 'POST'])
def index():
    site_data = get_json(site_data_path)

    if request.method == 'POST':
        is_button_home = False if request.form.get('button_home') is None else True
        is_button_friends = False if request.form.get('button_friends') is None else True
        is_button_finding = False if request.form.get('button_finding') is None else True

        if is_button_home:
            return redirect("http://www.google.com", code=302)
        if is_button_friends:
            return redirect("/friends", code=302)
        if is_button_finding:
            return redirect("http://www.google.com", code=302)

    return render_template('index.html', data=site_data.get("home"))

@app.route('/friends', methods=['GET', 'POST'])
def friends():
    site_data = get_json(site_data_path)

    return render_template('friends.html', data=site_data.get("friends"))