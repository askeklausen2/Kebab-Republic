from functions import *
from flask import Flask, redirect, url_for, render_template, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.sql import insert, select

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit-coordinates', methods=['POST'])
def submit_coordinates():
    return None

@app.route("/search/name=<name>/rating=<rating>/price=<price>/dist=<dist>/lon=<lon>/lat=<lat>/")
def search(name: str = None, rating: int = None, price: int = None, dist: int = None, lon: int = None, lat: int = None):
    engine = create_engine('postgresql+psycopg2://username:password@localhost/dbname')
    metadata = MetaData(bind=engine)

    # Define the table
    kebab_table = Table('kebab', metadata, autoload_with=engine)

    # Select all rows
    with engine.connect() as conn:
        select_stmt = select([kebab_table])
        result = conn.execute(select_stmt)
        rows = result.fetchall()

    attributes = ['id', 'name', 'address', 'price', 'rating', 'latitude', 'longitude']
    data = []
    for row in rows:
        row_dict = {}
        for attribute, index in enumerate(attributes):
            row_dict[attribute] = row[index]
        data.append[row_dict]
    
    if name: data = search_name(name, data)
    if rating: data = search_rating(rating, data)
    if price: data = search_price(price, data)
    if dist and lat and lon: data = search_closer(lat, lon, dist, data)
    return html_from_list(data)

@app.route("/insert/name=<name>/rating=<rating>/price=<price>/dist=<dist>/lon=<lon>/lat=<lat>/")
def insert(name: str = None, rating: int = None, price: int = None, dist: int = None, lon: int = None, lat: int = None):
    #Connect to your database
    engine = create_engine('postgresql+psycopg2://username:password@localhost/dbname')
    metadata = MetaData(bind=engine)

    # Define the table
    kebab_table = Table('kebab', metadata,
                        Column('id', Integer, primary_key=True),
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
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)