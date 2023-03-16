-- create table default value 
create table IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256) NOT NULL
)
