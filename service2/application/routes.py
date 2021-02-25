from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/country', methods=['GET'])
def country():
    country = ["Greece", "Turkey", "Cuba", "USA", "Czech", "France", "Denmark", "Ireland","Portugal","Croatia"]
    return Response(str(random.choice(country)), mimetype='text/plain')