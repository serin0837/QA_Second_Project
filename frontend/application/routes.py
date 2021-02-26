from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
import requests
from application.models import Travel
from application import app, db

db.create_all()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    #change uri
    country_response = requests.get("http://35.197.49.49:5001/country")
    month_response = requests.get("http://35.197.49.49:5002/month")
    build_response = requests.post("http://35.197.49.49:5003/build", data = month_response.text)
    
    new_build = Travel(country = country_response.text, month = month_response.text, build = build_response.text)
    db.session.add(new_build)
    db.session.commit()

    return render_template('index.html', country=country_response.text, month=month_response.text, build=build_response.text)
