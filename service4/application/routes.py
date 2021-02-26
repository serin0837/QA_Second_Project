from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/build', methods=['POST'])
def build():
    month = request.data.decode('utf-8')
    # change logic here
    if month == "January":
        build = "enjoy sun"
    elif month == "February":
        build = "enjoy sun"
    elif month == "March":
        build = "enjoy flower"
    elif month == "April":
        build = "enjoy flower"
    elif month == "May":
        build = "love your partner more"
    elif month == "June":
        build = "surfing"
    elif month == "July":
        build = "camping"
    elif month == "August":
        build = "birthday party"
    elif month == "September":
        build = "read a lot"
    elif month == "October":
        build = "drink beer a lot"
    elif month == "November":
        build = "look back your year"
    elif month == "December":
        build = "enjoy your life"
    else:
        build = "Build not compatible"

    return Response(build, mimetype='text/plain')
