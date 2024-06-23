#Toteuta sovellus tähän tiedostoon
# -*- coding: utf-8 -*-
from flask import Flask, request, Response
import os
app = Flask(__name__)

# @app.route määrää mille osoitteille tämä funktio suoritetaan
@app.route('/')
def hello_world():
    return Response("Hello World", content_type="text/plain; charset=UTF-8")

@app.route('/vt2')
def vt1():
    return render_template('pohja.xhtml')

@app.route('/luo', methods = ['POST', 'GET'])
def luo():
    koko = int(request.form["x"])
    p1 = request.form["pelaaja1"]
    p2 = request.form["pelaaja2"]

    return render_template("pohja.xhtml", x=koko, pelaaja1=p1, pelaaja2=p2)
    
    

