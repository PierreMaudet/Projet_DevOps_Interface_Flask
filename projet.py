from flask import Flask
import flask
import os
from flask import render_template, make_response, request, url_for, session

app = flask.Flask(__name__)
app.config["DEBUG"]=True

@app.route('/accueil')
def accueil():
    return render_template("accueil.html")

@app.route('/comparaison/')
def comparaison():
    return render_template("comparaison.html")

@app.route('/synchronisation/')
def synchronisation():
    return render_template("synchronisation.html")


if __name__ == "__main__":
    app.run(port='5000', debug=True)