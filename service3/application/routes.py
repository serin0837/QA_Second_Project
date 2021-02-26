from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/month', methods=['GET'])
def month():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return Response(str(random.choice(month)), mimetype='text/plain')
