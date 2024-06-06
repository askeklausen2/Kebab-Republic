-- Insert data into database and returns the newly inserted data
INSERT INTO kebab (name, address, price, rating, latitude, longitude)
VALUES ({value_1}, {value_2}, {value_3}, {value_4}, {value_5}, {value_6})
RETURNING *;