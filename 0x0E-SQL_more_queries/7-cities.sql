-- creates the database hbtn_0d_usa and the table cities(in database hbtn_0d_usa)
-- cities description: id INT unique, auto generated, can't be null and is a primary key
-- state_id INT, can't be null and must be a foreign key that references to id of the states table
-- name VARCHAR(256) can't be null

CREATE DATABASE IF NOT EXISTS hbtn-0d_usa;
CREATE TABLE IF NOT EXISTS htbtn_0d_usa.cities(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id));
