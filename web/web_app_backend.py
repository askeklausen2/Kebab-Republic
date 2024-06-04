from readCSV import readCSV
from querry import *
from visualize import *
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return html_from_list(readCSV("web\data\init_kebab_data.csv"))
    #return render_template("home.html")

@app.route("/search/key=<key>/min_rating=<min_rating>/max_price=<max_price>/max_dist=<max_dist>/")
def search(key, min_rating, max_price, max_dist):
    key
    return redirect(url_for("login"))

@app.route("/insert_kebab")
def insert():
    request
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
