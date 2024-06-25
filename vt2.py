#Toteuta sovellus tähän tiedostoon
# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import os
import jinja2
app = Flask(__name__)

# @app.route määrää mille osoitteille tämä funktio suoritetaan

@app.route('/')
def vt1():
    return render_template('pohja.xhtml')

@app.route('/luo', methods = ['POST', 'GET'])
def luo():
    viesti = ""
    try:
        koko = int(request.form["x"])
    except:
        return render_template("pohja.xhtml", virheviesti="Anna kokonaisluku 8-16")
    if koko<8 or koko>16:
        return render_template("pohja.xhtml", virheviesti="Anna kokonaisluku 8-16")
    p1 = request.form["pelaaja1"]
    p2 = request.form["pelaaja2"]

    try:
        return render_template("pohja.xhtml", x=koko, pelaaja1=p1, pelaaja2=p2, virheviesti=viesti)
    except:
        # Virhetilanteessa palauta virhekoodi ja viesti
        return Response("Virhetilanne 400", mimetype="text/plain"), 400

    
    
    

