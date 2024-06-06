from static.functions import *
from flask import Flask, redirect, render_template, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.sql import select
import psycopg2

#before running the web app insert the needed info
username = "askeklausen"
password = "postgres"
dbname = "askeklausen"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/search/")
def search():
    name = request.form.get('name')
    rating = request.form.get('rating')
    price = request.form.get('price')
    dist = request.form.get('dist')
    lon = request.form.get('lon')
    lat = request.form.get('lat')
    
    print(name, rating, price, dist, lon, lat)
    
    engine = create_engine(f"postgresql://{username}:{password}@localhost/{dbname}")
    metadata = MetaData()

    kebab_table = Table('kebab', metadata, autoload_with=engine)

    with engine.connect() as conn:
        select_stmt = select(kebab_table)
        result = conn.execute(select_stmt)
        rows = result.fetchall()

    attributes = ['name', 'address', 'price', 'rating', 'latitude', 'longitude']
    data = []
    for row in rows:
        row_dict = {}
        for index, attribute in enumerate(attributes):
            row_dict[attribute] = row[index]
        data.append(row_dict)
    
    if name: data = search_name(name, data)
    if rating: data = search_rating(rating, data)
    if price: data = search_price(price, data)
    if dist and lat and lon: data = search_closer(lat, lon, dist, data)
    return html_from_list(data)

@app.route("/insert/")
def insert():
    name = request.form.get('name')
    rating = request.form.get('rating')
    price = request.form.get('price')
    dist = request.form.get('dist')
    lon = request.form.get('lon')
    lat = request.form.get('lat')
    
    #Connect to your database
    engine = create_engine(f"postgresql://{username}:{password}@localhost/{dbname}")
    metadata = MetaData()

    # Define the table
    kebab_table = Table('kebab', metadata,
                        Column('name', String),
                        Column('address', String),
                        Column('price', Float),
                        Column('rating', Float),
                        Column('latitude', Float),
                        Column('longitude', Float))

    # Insert values
    values = {
        'name': name,
        'address': "DO LATER",
        'price': price,
        'rating': rating,
        'latitude': lat,
        'longitude': lon
    }

    # Insert the new row and return the inserted data
    with engine.connect() as conn:
        insert_stmt = kebab_table.insert().values(values).returning(*kebab_table.columns)
        conn.execute(insert_stmt)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)