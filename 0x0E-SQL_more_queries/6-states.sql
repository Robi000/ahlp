-- create table default value 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
create table IF NOT EXISTS states(
    id INT UNIQUE NOT NULL AUTO_INCREMENT ,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY ( id )
)
