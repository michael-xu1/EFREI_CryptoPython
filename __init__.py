from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)
app.secret_key = "une_clef_secrete_pour_la_session"  # Obligatoire pour utiliser les sessions

@app.before_request
def create_fernet_key():
    # Si pas de clé dans session, on en crée une
    if 'fernet_key' not in session:
        session['fernet_key'] = Fernet.generate_key().decode()

@app.route('/')
def accueil():
    return "Bienvenue sur l'application de chiffrement."

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    try:
        key = session.get('fernet_key')
        f = Fernet(key.encode())
        token = f.encrypt(valeur.encode())
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        key = session.get('fernet_key')
        f = Fernet(key.encode())
        token = f.decrypt(valeur.encode())
        return f"Valeur décryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
