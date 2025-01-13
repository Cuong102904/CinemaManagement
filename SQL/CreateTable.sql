CREATE TABLE movie (
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR(100),
	overview TEXT,
	original_language VARCHAR(10),
	release_date DATE,
	runtime INTEGER,
	status VARCHAR(50),
	tagline TEXT,
	revenue integer DEFAULT 0,
	url TEXT
);

CREATE TABLE genre (
	id_genre SERIAL PRIMARY KEY,
	name VARCHAR(40)
);

CREATE TABLE movie_join_genre (
	movie_id INTEGER,
	id_genre INTEGER,
	CONSTRAINT fk_id_genre FOREIGN KEY (id_genre) REFERENCES genre(id_genre) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE crew (
    id_crew VARCHAR(50) PRIMARY KEY,
    movie_id INTEGER,
    department VARCHAR(80),
    gender INTEGER,
    job VARCHAR(80),
    name VARCHAR(80),
    FOREIGN KEY (movie_id) REFERENCES movie(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "cast" (
    id_cast SERIAL PRIMARY KEY,
    movie_id INTEGER,
    character VARCHAR(1000),
    gender VARCHAR(10),
    name VARCHAR(80),
    "order" INTEGER,
    CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES movie(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	address VARCHAR(80),
	city VARCHAR(40),
	email VARCHAR(50) UNIQUE,
	phone VARCHAR(12) UNIQUE,
	username VARCHAR(30),
	password VARCHAR(30),
	total_amount int DEFAULT 0
	CONSTRAINT email_or_phone CHECK (
        NOT (email IS NULL AND phone IS NULL)
    )
);

CREATE TABLE cinema (
	cinema_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	location VARCHAR(30)
);

CREATE TABLE room (
	room_id SERIAL PRIMARY KEY,
	cinema_id INTEGER,
	name VARCHAR(10),
	type VARCHAR(10),
	price INTEGER DEFAULT 0,
	CONSTRAINT fk_cinema_id FOREIGN KEY (cinema_id) REFERENCES cinema(cinema_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE seat (
	seat_id VARCHAR(7) PRIMARY KEY,
	room_id INTEGER,
	row VARCHAR(1),
	col INTEGER,
	CONSTRAINT fk_room_id FOREIGN KEY (room_id) REFERENCES room(room_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE staff(
	staff_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	email VARCHAR(30),
	birth VARCHAR(30),
	role VARCHAR(30),
	cinema_id INTEGER,
	CONSTRAINT fk_cinema_id FOREIGN KEY (cinema_id) REFERENCES cinema(cinema_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE schedule (
	schedule_id SERIAL PRIMARY KEY,
	schedule_movie_date DATE,
	schedule_movie_start VARCHAR(10),
	room_id INTEGER,
	movie_id INTEGER,
	CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES movie(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_room_id FOREIGN KEY (room_id) REFERENCES room(room_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE product (
	product_id SERIAL PRIMARY KEY,
	name VARCHAR(30),
	description TEXT,
	price INTEGER,
	category VARCHAR(30)
);

CREATE TABLE discount (
	discount_id VARCHAR(30) PRIMARY KEY,
	value int,
	date_start date,
	date_expire date,
	customer_id int,
	CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ticket (
	ticket_id SERIAL PRIMARY KEY,
	user_id INTEGER,	
	schedule_id INTEGER,
	total_money INTEGER DEFAULT 0,
	discount_id VARCHAR(30),
	feedback text,
	staff_id INTEGER,
	CONSTRAINT fk_staff_id FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_schedule_id FOREIGN KEY (schedule_id) REFERENCES schedule(schedule_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_discount_id FOREIGN KEY (discount_id) REFERENCES discount(discount_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE product_detail(
	ticket_id INTEGER,
	product_id INTEGER,
	PRIMARY KEY (ticket_id,product_id),
	quantity INTEGER,
	unit_price INTEGER DEFAULT 0,
	CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_ticket_id FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE seat_detail (
	ticket_id INTEGER,
	seat_id varchar(7),
	PRIMARY KEY(ticket_id,seat_id),
	price INTEGER,
	CONSTRAINT fk_ticket_id FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_seat_id FOREIGN KEY (seat_id) REFERENCES seat(seat_id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- to drop all table
-- DO $$ 
-- BEGIN
--     -- Generate and execute DROP TABLE commands for all tables
--     EXECUTE (
--         SELECT STRING_AGG('DROP TABLE IF EXISTS "' || tablename || '" CASCADE;', ' ')
--         FROM pg_tables
--         WHERE schemaname = 'public'
--     );
-- END $$;


-- TRUNCATE TABLE seat_detail CASCADE
-- TRUNCATE TABLE ticket CASCADE


-- SELECT pg_get_serial_sequence('ticket', 'ticket_id')
--SELECT pg_get_serial_sequence('seat_detail', 'ticket_id')
--ALTER SEQUENCE public.ticket_ticket_id_seq RESTART WITH 1

-- DO $$
-- DECLARE
--     trigger_record RECORD;
-- BEGIN
--     FOR trigger_record IN
--         SELECT event_object_table AS table_name, trigger_name
--         FROM information_schema.triggers
--         WHERE trigger_schema = 'public'
--     LOOP
--         EXECUTE FORMAT('DROP TRIGGER IF EXISTS %I ON %I;', trigger_record.trigger_name, trigger_record.table_name);
--     END LOOP;
-- END $$;
