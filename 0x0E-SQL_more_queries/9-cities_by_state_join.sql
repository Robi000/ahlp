-- display all city  with their state
SELECT cities.id AS id , cities.name AS name , states.name AS name FROM  cities , states WHERE cities.state_id = states.id ORDER BY cities.id;