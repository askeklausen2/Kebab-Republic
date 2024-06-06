from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.sql import insert, select

# Connect to your database
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
    'name': 'Example Kebab',
    'address': '123 Kebab St',
    'price': 10.99,
    'rating': 4.5,
    'latitude': 40.7128,
    'longitude': -74.0060
}

# Insert the new row and return the inserted data
with engine.connect() as conn:
    insert_stmt = kebab_table.insert().values(values).returning(*kebab_table.columns)
    result = conn.execute(insert_stmt)
    new_row = result.fetchone()

print(new_row)

# RETRIEVE DATA

from sqlalchemy import create_engine, MetaData, Table, select

# Connect to your database
engine = create_engine('postgresql+psycopg2://username:password@localhost/dbname')
metadata = MetaData(bind=engine)

# Define the table
kebab_table = Table('kebab', metadata, autoload_with=engine)

# Select all rows
with engine.connect() as conn:
    select_stmt = select([kebab_table])
    result = conn.execute(select_stmt)
    rows = result.fetchall()

for row in rows:
    print(row)
