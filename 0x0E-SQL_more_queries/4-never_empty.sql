-- create table default value 
create table IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
)