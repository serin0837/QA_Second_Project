from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/month', methods=['GET'])
def month():
    month = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    return Response(str(random.choice(month)), mimetype='text/plain')
