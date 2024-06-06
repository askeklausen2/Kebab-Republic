-- Drop table if
DROP TABLE kebab;

-- Create schema for kebab data
CREATE TABLE kebab (
    name VARCHAR(50),
    address VARCHAR(100),
    price FLOAT(50),
    rating FLOAT(10),
    longitude FLOAT(50),
    latitude FLOAT(50)
);

-- Import kebab data to database
COPY kebab (name, address, price, rating, longitude, latitude) 
FROM 'web/data/init_kebab_data.csv' 
DELIMITER ','
CSV HEADER;
