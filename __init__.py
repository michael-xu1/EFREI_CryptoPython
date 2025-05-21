from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
#test                                                                                                                         
app = Flask(__name__)
app.secret_key = "une_clé_secrète_pour_la_session"  # Obligatoire pour les sessions


@app.before_request
def set_session_key():
    # Générer une clé uniquement si elle n’existe pas déjà dans la session
    if 'fernet_key' not in session:
        session['fernet_key'] = Fernet.generate_key().decode()  
      
@app.route('/')
def hello_world():
    return render_template('hello.html')
  

@app.route('/encrypt/<string:valeur>')
def encryptage(key,valeur):
    key = session.get('fernet_key')
    if not key:
        return "Erreur : clé de session introuvable."  
    f = Fernet(key.encode())
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:valeur>')
def decryptage(key,valeur):
    key = session.get('fernet_key')
    if not key:
        return "Erreur : clé de session introuvable."
    f = Fernet(key.encode())
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.decrypt(valeur_bytes)  # Dencrypt la valeur
    return f"Valeur décryptée : {token.decode()}"  # Retourne le token en str
  
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
