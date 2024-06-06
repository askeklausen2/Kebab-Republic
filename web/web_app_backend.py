import os
from readCSV import readCSV
from querry import *
from visualize import *
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-coordinates', methods=['POST'])
def submit_coordinates():
    return None

@app.route("/search/lon=<lon>/lat=<lat>/search_key=<search_key>/min_rating=<min_rating>/max_price=<max_price>/max_dist=<max_dist>/")
def search(lon: int = None, lat: int = None, search_key: str = None, min_rating: int = None, max_price: int = None, max_dist: int = None):
    data = 
    if search_key: data = search_name(search_key, data)
    if min_rating: data = search_rating(min_rating, data)
    if max_price: data = search_price(max_price, data)
    if max_dist and lat and lon: data = search_closer(lat, lon, max_dist, data)
    return html_from_list(data)

@app.route("/insert_kebab")
def insert():
    
    return 4

if __name__ == '__main__':
    app.run(debug=True)
