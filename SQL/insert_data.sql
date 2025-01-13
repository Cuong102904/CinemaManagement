COPY movie(movie_id, title, overview, original_language, release_date, runtime, status, tagline, url) FROM 'E:\DEV\db_lab\raw\clean\movie.csv' DELIMITER ',' CSV HEADER;
COPY genre(id_genre, name) FROM 'E:\DEV\db_lab\raw\clean\gernes.csv' DELIMITER ',' CSV HEADER;
COPY movie_join_genre(id_genre,movie_id) FROM 'E:\DEV\db_lab\raw\clean\genre_join_film.csv' DELIMITER ',' CSV HEADER;
COPY crew(movie_id, id_crew,department, gender,job, name) FROM 'E:\DEV\db_lab\raw\clean\crew.csv' DELIMITER ',' CSV HEADER;
COPY "cast"(id_cast, movie_id, character, gender, name,"order") FROM 'E:\DEV\db_lab\raw\clean\cast.csv' DELIMITER ',' CSV HEADER;

COPY users(user_id,first_name, last_name, address, city,phone, email, username, password) FROM 'E:\DEV\db_lab\raw\clean\customer.csv' DELIMITER ',' CSV HEADER;
COPY cinema(cinema_id,name, location) FROM 'E:\DEV\db_lab\raw\clean\cinema.csv' DELIMITER ',' CSV HEADER;
COPY room(room_id, cinema_id, name,type, price) FROM 'E:\DEV\db_lab\raw\clean\room.csv' DELIMITER ',' CSV HEADER;


COPY seat(room_id, seat_id, row, col) FROM 'E:\DEV\db_lab\raw\clean\seat.csv' DELIMITER ',' CSV HEADER;
COPY schedule(schedule_movie_date,schedule_movie_start,room_id,movie_id) FROM 'E:\DEV\db_lab\raw\clean\schedule.csv' DELIMITER ',' CSV HEADER;

COPY product(name,description,price, category) FROM 'E:\DEV\db_lab\raw\clean\product.csv' DELIMITER ',' CSV HEADER;
COPY staff(name,email,birth,role,cinema_id) FROM 'E:\DEV\db_lab\raw\clean\staff.csv' DELIMITER ',' CSV HEADER;
COPY discount(discount_id,value,date_start,date_expire) FROM 'E:\DEV\db_lab\raw\clean\discount.csv' DELIMITER ',' CSV HEADER;

COPY ticket(schedule_id,user_id, staff_id) FROM 'E:\DEV\db_lab\raw\clean\ticket1.csv' DELIMITER ',' CSV HEADER;

COPY seat_detail(ticket_id, seat_id, price) FROM 'E:\DEV\db_lab\raw\clean\seat_detail.csv' DELIMITER ',' CSV HEADER;
-- current we drop this trigger
-- DROP TRIGGER tg_on_update_seat_price ON seat_detail
--DROP TRIGGER tg_on_update_price_seat1 ON seat_detail
--DROP TRIGGER tg_on_update_price_seat ON seat_detail





-- Demo
-- INSERT INTO schedule(schedule_movie_date, schedule_movie_start, room_id, movie_id) VALUES
-- ('2024-12-28','04:20',1,559)
-- INSERT INTO users(user_id,first_name, last_name, address,city, email,phone, username, password)
-- VALUES(2000,'Hoang', 'Cuong', 'LongBien','Hanoi','hoangmanhcuongx29@gmail.com','083-565-2146','cuonghoang223','12345');


-- INSERT INTO ticket(ticket_id,user_id, schedule_id,feedback,staff_id) VALUES (544441,2000, 3501,'10diemverygood',1)
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544441,'A1_1') 
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544441,'A1_1') 
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544441,'A2_1') 
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544441,'A3_1') 

-- INSERT INTO product_detail(ticket_id, product_id, quantity) VALUES (544441, 1, 2)
-- INSERT INTO product_detail(ticket_id, product_id, quantity) VALUES (544441, 2, 2)

-- UPDATE ticket
-- SET discount_id = 'km_10_1'
-- WHERE ticket_id = 544441;
-- SELECT * FROM ticket WHERE ticket_id = 544441

-- DELETE FROM product_detail WHERE ticket_id = 544441
-- DELETE FROM ticket WHERE ticket_id = 544441

-- SELECT * FROM search_ticket(544441)
-- SELECT * FROM users WHERE user_id = 2000
-- SELECT * FROM product
-- SELECT * FROM product_detail
-- SELECT * FROM ticket WHERE ticket_id = 544441






--Demo
-- SELECT * FROM schedule ORDER BY schedule_id DESC
-- SELECT * FROM ticket WHERE ticket_id = 544442;

-- SELECT * FROM seat_detail WHERE ticket_id = 544442;

-- SELECT * FROM users WHERE user_id = 2001
-- SELECT * FROM product
-- SELECT * FROM search_ticket(544442)
-- SELECT * FROM users WHERE user_id = 2001
-- SELECT * FROM product
-- SELECT * FROM product_detail WHERE ticket_id= 544442

-- SELECT * FROM discount

-- Demo
-- INSERT INTO schedule(schedule_movie_date, schedule_movie_start, room_id, movie_id) VALUES
-- ('2024-12-30','04:20',1,559)
-- INSERT INTO users(user_id,first_name, last_name, address,city, email,phone, username, password)
-- VALUES(2001,'Nguyen', 'Dat', 'LongBien','Hanoi','dat@gmail.com','083-562-1003','dat1003','12345');

-- EXPLAIN ANALYZE SELECT * FROM schedule_in_day()
-- SELECT * FROM schedule_in_day()

-- INSERT INTO ticket(ticket_id,user_id, schedule_id,feedback,staff_id) VALUES (544442,2001, 3509,'10diemverygood',1)
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544442,'A1_1'); 
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544442,'A1_1'); 
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544442,'A2_1');
-- INSERT INTO seat_detail(ticket_id, seat_id) VALUES (544442,'A3_1'); 

-- INSERT INTO product_detail(ticket_id, product_id, quantity) VALUES (544442, 1, 2);
-- INSERT INTO product_detail(ticket_id, product_id, quantity) VALUES (544442, 2, 2);

-- DELETE FROM product_detail WHERE ticket_id = 544442
-- DELETE FROM ticket WHERE ticket_id = 544442

-- UPDATE ticket
-- SET discount_id = 'km_10_1'
-- WHERE ticket_id = 544442;
-- UpDATE  ticket SET discount_id = NULL WHERE ticket_id = 544442