from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
import requests
from application.models import Travel
from application import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    #change uri
    country_response = requests.get("http://character-gen_service2:5000/race")
    month_response = requests.get("http://character-gen_service3:5000/player_class")
    build_response = requests.post("http://character-gen_service4:5000/build", data = month_response.text)
    
    new_build = Travel(country = country_response.text, month = month_response.text, build = build_response.text)
    db.session.add(new_build)
    db.session.commit()

    return render_template('index.html', country=country.text, month=month.text, build=build_response.text)
