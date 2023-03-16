-- create table default value 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
create table IF NOT EXISTS cities(
    id INT UNIQUE NOT NULL AUTO_INCREMENT ,
    name VARCHAR(256) NOT NULL,
    state_id INT Not NULL,
    PRIMARY KEY ( id ),
    CONSTRAINT FK_STATES_ID FOREIGN KEY (state_id) REFERENCES states(id)

)
