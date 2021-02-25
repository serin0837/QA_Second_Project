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
        build = 'Mages who specialize in manipulating minds, altering perceptions of friend and foe alike.'
    elif month == "4":
        build = 'Quiet killers, these types attack from the shadows against unsuspecting prey.'
    elif month == "5":
        build = 'Characters skilled in the crafting and use of powerful potions and deadly poisons.'
    elif month == "6":
        build = 'Mages who work from the shadows, using stealth to supplement their magical abilities.'
    elif month == "7:
        build = 'Brutish, aggressive fighters who prefer an overwhelming offense over a cautious defense.'
    elif month == "8":
        build = 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    elif month == "9":
        build = 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    elif month == "10":
        build = 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    elif month == "11":
        build = 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    elif month == "12":
        build = 'Tough, resiliant characters covered head to toe in nigh impenetrable heavy armor.'
    else:
        build = "Build not compatible"

    return Response(build, mimetype='text/plain')