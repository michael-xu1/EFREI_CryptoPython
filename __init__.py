from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
#test                                                                                                                         
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')
  
@app.route('/key')
def generate_key():
    key = Fernet.generate_key().decode()
    return f"Voici votre clé : {key}"

@app.route('/encrypt/<key>/<string:valeur>')
def encryptage(key,valeur):
    f = Fernet(key.encode())
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<key>/<string:valeur>')
def decryptage(key,valeur):
    f = Fernet(key.encode())
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.decrypt(valeur_bytes)  # Dencrypt la valeur
    return f"Valeur décryptée : {token.decode()}"  # Retourne le token en str
  
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
