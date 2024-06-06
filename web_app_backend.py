from static.functions import *
from flask import Flask, redirect, render_template, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, insert
from sqlalchemy.sql import select

#before running the web app insert the needed info
username = "askeklausen"
password = "postgres"
dbname = "askeklausen"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/search/", methods=['GET', 'POST'])
def search():
    name = request.form.get('name')
    rating = request.form.get('rating')
    price = request.form.get('price')
    dist = request.form.get('dist')
    address = request.form.get('address')
    lon = request.form.get('latitude')
    lat = request.form.get('longitude')
    
    engine = create_engine(f"postgresql://{username}:{password}@localhost/{dbname}")
    metadata = MetaData()
    
    if request.form.get('checkbox'):
        values = {
            'name': name,
            'address': address,
            'price': float(price),
            'rating': float(rating),
            'latitude': float(lat),
            'longitude': float(lon)
        }
        
        kebab_table = Table('kebab', metadata,
                            Column('name', String),
                            Column('address', String),
                            Column('price', Float),
                            Column('rating', Float),
                            Column('latitude', Float),
                            Column('longitude', Float))
        
        insert_stmt = insert(kebab_table).values(values)
        
        with engine.connect() as conn:
            conn.execute(insert_stmt)
            conn.commit()
        return redirect('/')
    
    else:
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

if __name__ == '__main__':
    app.run(debug=True)