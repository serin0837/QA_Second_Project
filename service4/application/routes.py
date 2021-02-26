from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/build', methods=['POST'])
def build():
    month = request.data.decode('utf-8')
    # change logic here
    if month == "1":
        build = "You need sun. WHy don't you go somewhere hot and shiny?"
    elif month == "2":
        build = "You need sun. WHy don't you go somewhere hot and shiny?"
    elif month == "3":
        build = 'Drink cocktail.'
    elif month == "4":
        build = 'Enjoy Flower'
    elif month == "5":
        build = 'Enjoy sun.'
    elif month == "6":
        build = 'Enjoy sun'
    elif month == "7":
        build = 'Enjoy beach.'
    elif month == "8":
        build = 'Swimming.'
    elif month == "9":
        build = 'Autumn.'
    elif month == "10":
        build = 'Autumn.'
    elif month == "11":
        build = 'November'
    elif month == "12":
        build = 'December'
    else:
        build = "Build not compatible"

    return Response(build, mimetype='text/plain')
