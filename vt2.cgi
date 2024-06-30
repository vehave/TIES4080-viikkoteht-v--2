#!/home/voohartu/public_html/cgi-bin/ties4080/venv/bin/python
#muuta edelliselle riville oikea polku omaan venv-ympäristöön
# -*- coding: utf-8 -*-
# suorittaa Flask-sovellukset CGI-ohjelmina users.jyu.fi-palvelimella
import sys
from wsgiref.handlers import CGIHandler
from werkzeug.debug import DebuggedApplication

try:
  from vt2 import app as application

  if __name__ == '__main__':
         handler = CGIHandler()
         application.debug = True
         handler.run(DebuggedApplication(application))

except:
  #koska tänne päädyttäessä ei werkzeug toimi täytyy itse tulostaa http-protokollan
  #edellyttämä otsake. STDOUT menee tässä tapauksessa suoraan selaimelle
  print("Content-Type: text/plain;charset=UTF-8\n")
  print("Syntaksivirhe:\n")
  for err in sys.exc_info():
        print(err)
