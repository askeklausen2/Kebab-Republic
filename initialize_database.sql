-- Drop table if
DROP TABLE kebab;

-- Create schema for kebab data
CREATE TABLE kebab (
    name VARCHAR(50),
    address VARCHAR(100),
    price VARCHAR(50),
    rating VARCHAR(10),
    longitude VARCHAR(50),
    latitude VARCHAR(50)
);

-- Import kebab data to database
COPY kebab (name, address, price, rating, longitude, latitude) 
FROM 'web/data/init_kebab_data.csv' 
DELIMITER ','
CSV HEADER;
