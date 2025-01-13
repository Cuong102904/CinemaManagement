-- insert
create or replace function insert_cinema(in cineID int, in nm varchar(30), in loca varchar(30)) returns void as
$$
begin
	insert into cinema(cinema_id, name, location) values (cineID, nm, loca);
end;
$$ language plpgsql;

create or replace function insert_schedule(in sheID int, in sch_date date, in sch_start varchar(10), in rmID int, in mvID int) returns void as
$$
begin
	insert into schedule(schedule_id, schedule_movie_date, schedule_movie_start, room_id, movie_id) values (sheID, sch_date, sch_start, rmID, mvID);
end;
$$ language plpgsql;

create or replace function insert_cast(in cID int, in mvID int, in cha varchar(50), in gen varchar(10), in nm varchar(50), in ord int) returns void as
$$
begin
	insert into "cast"(id_cast, movie_id, character, gender, name, "order") values (cID, mvID, cha, gen, nm, ord);
end;
$$ language plpgsql;

create or replace function insert_crew(in cID varchar(50), in mvID int, in dep varchar(30), in gen int,in jo varchar(30), in nm varchar(30)) returns void as
$$
begin
	insert into crew(id_crew, movie_id, department, gender, job, name) values (cID, mvID, dep, gen, jo, nm);
end;
$$ language plpgsql;

create or replace function insert_discount(in disID varchar(30), in vl int, in date_s date, in date_x date, in cusID int) returns void as
$$
begin
	insert into discount(discount_id, value, date_start, date_expire, customer_id) values (disID, vl, date_s, date_x, cusID);
end;
$$ language plpgsql;

create or replace function insert_genre(in genID int, in nm varchar(40)) returns void as 
$$
begin
	insert into insert_genre(id_genre, name)  values (genID, nm);
end;
$$ language plpgsql;

create or replace function insert_movie(in mvID int, in tit varchar(100), in ovv text, in lang varchar(10), in redate date, in runtime int, in sta varchar(10), in tag text, in url text, in age int) returns void as
$$
begin
	insert into movie(movie_id, title, overview, original_language, release_date, runtime, status, url, ageres) values (mvID, tit, ovv, lang, redate, runtime, sta, tag, url, age);
end;
$$ language plpgsql;

create or replace function insert_product(in prodid int, in nm varchar(30), in des varchar(300), in price int, in cate varchar(30)) returns void as
$$
begin
	insert into product(product_id, name, description, price, category) values (prodid, nm, des, price, cate);
end;
$$ language plpgsql;

create or replace function insert_room(in rmID int, in cineID int, in name varchar(10), in type varchar(10), in price int) returns void as
$$
begin
	insert into room(room_id, cinema_id, name, type, price) values (rmID, cineID, name,type, price);
end;
$$ language plpgsql;

create or replace function insert_seat(in seatid varchar(7),in roomid int, in rw varchar(1), in cl int) returns void as
$$
begin
	insert into seat(seat_id, room_id, row, col) values (seatid, roomid, rw, cl);
end;	
$$ language plpgsql;


create or replace function insert_staff(in staffid int, in name varchar(30), in email varchar(30), in birth varchar(30), in role varchar(30), in cinemaid int) returns void as
$$
begin
	insert into staff(staff_id, name, email, birth, role, cinema_id) values (staffid, name, email, birth, role, cinemaid);
end;
$$ language plpgsql;


create or replace function insert_ticket(in ticketid int, in userid int, in scheduleid int, in roomid int, in totalmoney int, in discountid varchar(30),in feedback text, in staffid int) returns void as
$$
begin
	insert into ticket(user_id, schedule_id, room_id, discount_id, feedback, staff_id) values (user_id, scheduleid, roomid, discountid, feedback, staffid);
end;
$$ language plpgsql;


create or replace function insert_users(in userid int, in firstname varchar(30), in lastname varchar(30), in address varchar(80), in city varchar(40), in email varchar(50), in phone varchar(12), in username varchar(30), in password varchar(30), in totalamount int) returns void as
$$
begin
	insert into users(user_id, first_name, last_name, address, city, email, phone, username, password, total_amount) values (userid, firstname, lastname, address, city, email, phone, username, password, totalamount);
end;
$$ language plpgsql;

create or replace function insert_movie_join_genre(in movieid int, in idgen int) returns void as
$$
begin
	insert into movie_join_genre(movie_id, id_genre) values (movieid, idgen);
end;
$$ language plpgsql;


create or replace function insert_product_detail(in ticketid int, in prodid int, in quantity int, in price int) returns void as
$$
begin
	insert into product_detail(ticket_id, product_id, quantity, unit_price) values (ticketid, prodid, quantity, price);
end;
$$ language plpgsql;

create or replace function insert_seat_detail(in ticketid int, in seatid varchar(7), in price int) returns void as
$$
begin
	insert into seat_detail(ticket_id, seat_id, price) values (ticketid, seatid, price);
end;
$$ language plpgsql;








--FUNCTION TO MANAGER RETURN TABLE
--1.Search to the movie: input the name of the movie then return back all information of that movie having this name. 
CREATE OR REPLACE FUNCTION search_movie(in names varchar)
returns table (
    Movie_name varchar,
    overviews text,
    ori_language varchar,
    release date,
    statu varchar,
    taglines text,
    length integer
) as
$$
begin 
    return query
    SELECT title, overview, original_language, release_date ,status,tagline,runtime
    FROM movie
    WHERE title = names;
END;
$$ language plpgsql;


--2. Search the indentical ticket: input the id of this ticket then it will return all the information of that ticket
CREATE OR REPLACE FUNCTION search_ticket(in ticketID integer)
RETURNS TABLE(
    ticket_ids integer,
	usernames varchar,
	schedule_movie_dates date,
	schedule_movie_starts varchar,
	room_names varchar,
	cinema_names varchar,
	movie_titles varchar,
	total_moneys int,
	feedbacks text,
	discount_values integer,
	seat_detail text,
	product_detail text
) AS
$$
BEGIN 
	RETURN QUERY
	    SELECT ticket_id, username, schedule_movie_date, schedule_movie_start, room_name, cinema_name, movie_title, total_money, feedback, discount_value, seat_details, product_details
        FROM view_ticket
        WHERE ticket_id = ticketID
        ORDER BY schedule_movie_date, schedule_movie_start;
END;
$$ language plpgsql;


--3. Search the history transaction of 1 Users: Input the username and gmail (or input the users id ) will return detail all transaction (include ticket, name , movie, date, start, ...)
CREATE OR REPLACE FUNCTION history_trans(usersds VARCHAR(30), gmail VARCHAR(50))
RETURNS TABLE(
    usernames VARCHAR,
    email VARCHAR,
    name TEXT,
    movie VARCHAR,
    room VARCHAR,
    total_money INTEGER,
    feedback TEXT,
    discount_id VARCHAR,
    staff_name VARCHAR,
    schedule_movie_date DATE,
    schedule_movie_start VARCHAR
) AS 
$$
BEGIN 
    RETURN QUERY
    SELECT 
        u.username AS usernames,
        u.email,
        (u.first_name || ' ' || u.last_name) AS name, -- Explicit cast to VARCHAR
        m.title AS movie,
        r.name AS room, -- Use the correct room name
        t.total_money,
        t.feedback,
        t.discount_id,
        s.name AS staff_name,
        sc.schedule_movie_date,
        sc.schedule_movie_start
    FROM ticket t
    JOIN schedule sc ON t.schedule_id = sc.schedule_id
    JOIN movie m ON sc.movie_id = m.movie_id
    JOIN users u ON t.user_id = u.user_id
    JOIN staff s ON t.staff_id = s.staff_id
    JOIN room r ON sc.room_id = r.room_id -- Add a JOIN for the room name
    WHERE u.username = usersds AND u.email = gmail;
END;
$$ LANGUAGE plpgsql;
-- tesst: SELECT * FROM history_trans('tslad0','rebbecca.didio@didio.com.au')

-- 4. Search: at that time how many seat in 1 room having booked. 
--Input (name room, date, and the start) => return the number seat which had been booked.
CREATE OR REPLACE FUNCTION search_booked_seat(in scheduleid int)
RETURNS TABLE(
	room_name int,
	date date,
	start varchar,
	number_booked bigint
) AS
$$
BEGIN 
	RETURN QUERY
	SELECT s.room_id, scc.schedule_movie_date, scc.schedule_movie_start , COUNT(DISTINCT sd.seat_id) as number_booked_seat
	FROM seat_detail sd
	JOIN seat s ON sd.seat_id = s.seat_id
	JOIN schedule scc ON s.room_id = scc.room_id
	WHERE scc.schedule_id = scheduleid
	GROUP  BY s.room_id,  scc.schedule_movie_date, scc.schedule_movie_start;
END;
$$ language plpgsql;

-- 5. Display the revenue of 2 period of time: Input (date_start, date_end) output is the revenue
CREATE OR REPLACE FUNCTION revenue_period(in date_start date, in date_end date)
RETURNS TABLE(
	total_revenue bigint ,
	date_starts date,
	date_ends date
) AS 
$$
BEGIN 
	RETURN QUERY
	SELECT SUM(t.total_money), date_start, date_end
	FROM ticket t
	JOIN schedule s ON t.schedule_id = s.schedule_id
	WHERE s.schedule_movie_date >= date_start AND s.schedule_movie_date <= date_end;
END;
$$ language plpgsql;

--6. Display how many ticket having sold in 1 day for each movie: Input: start_date, return how many ticket for each movie that sold in that day
CREATE OR REPLACE FUNCTION ticket_sold(in start_date date)
RETURNS TABLE(
	Start_dates date,
	total_ticket_sold bigint,
	movie_name varchar
) AS
$$ 
BEGIN 
	RETURN QUERY 
	SELECT s.schedule_movie_date, COUNT(t.ticket_id), m.title
	FROM ticket t
	JOIN schedule s ON t.schedule_id = s.schedule_id
	JOIN movie m ON s.movie_id = m.movie_id
	WHERE s.schedule_movie_date = start_date
	GROUP BY s.schedule_movie_date, m.title;
END;
$$ language plpgsql;

--7.  Search by genre: Input: name of this genre, then ouput: list of the movie having this type of genre and order by the release date.
CREATE OR REPLACE FUNCTION search_genre(in genre_name varchar)
RETURNS TABLE(
	movie_title varchar,
	released_date date,
	genres varchar
) AS
$$
BEGIN 
	RETURN QUERY
	SELECT m.title, m.release_date, g.name AS genres
	FROM movie m
	JOIN movie_join_genre mjg ON m.movie_id = mjg.movie_id
	JOIN genre g ON mjg.id_genre = g.id_genre
	WHERE g.name = genre_name
	ORDER BY m.release_date DESC;
END;
$$ language plpgsql;
--8. Search crew by movie: Input the name of the movie then return all the crew of that movie
CREATE OR REPLACE FUNCTION search_crew(in movie_name varchar)
RETURNS TABLE(
	crew_name varchar,
	department varchar,
	gender integer,
	job varchar,
	movie_title varchar
) AS
$$
BEGIN 
	RETURN QUERY
	SELECT c.name, c.department, c.gender, c.job, m.title
	FROM crew c
	JOIN movie m ON c.movie_id = m.movie_id
	WHERE m.title = movie_name;
END;
$$ language plpgsql;

--9. Search cast by movie: Input the name of the movie then return all the cast of that movie
CREATE OR REPLACE FUNCTION search_cast(in movie_name varchar)
RETURNS TABLE(
	cast_name varchar,
	gender varchar,
	VaiDien varchar,
	orders integer,
	movie_title varchar
) AS
$$
BEGIN 
	RETURN QUERY
	SELECT c.name, c.gender, c.character, c.order, m.title
	FROM "cast" c
	JOIN movie m ON c.movie_id = m.movie_id
	WHERE m.title = movie_name;
END;
$$ language plpgsql;

--10.  Display the quantity of each product having been sold in 2 period:
CREATE OR REPLACE FUNCTION product_sold(in date_start date, in date_end date)
RETURNS TABLE(
	product_name varchar,
	quantity_sold bigint
) AS
$$
BEGIN 
	RETURN QUERY
	SELECT p.name, SUM(pd.quantity)
	FROM product_detail pd
	JOIN product p ON pd.product_id = p.product_id
	JOIN ticket t ON pd.ticket_id = t.ticket_id
	JOIN schedule s ON t.schedule_id = s.schedule_id
	WHERE s.schedule_movie_date >= date_start AND  s.schedule_movie_date <= date_end
	GROUP BY p.name;
END;
$$ language plpgsql;




---- FUNCTION to staff

--Function return lịch chiếu trong ngày
create or replace function schedule_in_day() 
returns table (
	title varchar(100),
	overview text,
	schedule_movie_date date,
	schedule_movie_start varchar(10)
) as
$$
begin
	return query
	select m.title, m.overview, s.schedule_movie_date, s.schedule_movie_start
	from schedule s
	join movie m using (movie_id) 
	where s.schedule_movie_date >= current_date;
end;
$$ language plpgsql;

--return những khách hàng tiêu tiền nhiều nhất

-- create or replace function vip_customer(in num int)
-- returns table (
-- 	user_id int,
-- 	first_name varchar(30),
-- 	last_name varchar(30),
-- 	email varchar(50),
-- 	phone varchar(12),
-- 	username varchar(30),
-- 	total_amount int
-- ) as
-- $$
-- begin
-- 	return query
-- 	select u.user_id, u.first_name, u.last_name, u.email, u.phone, u.username, u.total_amount
-- 	from users u
-- 	order by u.total_amount desc
-- 	limit num;
-- end;
-- $$ language plpgsql;
CREATE OR REPLACE FUNCTION vip_customer(IN num INT)
RETURNS TABLE (
    user_id INT,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(50),
    phone VARCHAR(12),
    username VARCHAR(30),
    total_amounts INT,
    ranks bigint
) AS
$$
BEGIN
    RETURN QUERY
    WITH ranked_users AS (
        SELECT 
            u.user_id, 
            u.first_name, 
            u.last_name, 
            u.email, 
            u.phone, 
            u.username, 
            u.total_amount,
            DENSE_RANK() OVER (ORDER BY u.total_amount DESC) AS rank
        FROM users u
    )
    SELECT 
        r.user_id, 
        r.first_name, 
        r.last_name, 
        r.email, 
        r.phone, 
        r.username, 
        r.total_amount,
        r.rank
    FROM ranked_users r
    WHERE r.total_amount >= (
        SELECT MIN(total_amount)
        FROM ranked_users
        WHERE rank = num
    )
    ORDER BY r.rank;
END;
$$ LANGUAGE plpgsql;



-- function tính tổng doanh thu của một bộ phim và update revenue
--alter table movie add column revenue int;

create or replace function total_revenue_movie(in movieid int)
returns bigint as 
$$
declare total_rev bigint;
begin
select sum(seat_detail.price) into total_rev
	from ticket t
	join seat_detail using (ticket_id)
	join schedule using (schedule_id)
	join movie using (movie_id)
	where schedule.movie_id = movieid;

	update movie
	set revenue = total_rev
where movie_id = movieid;
return total_rev;
end;
$$ language plpgsql;

--Function in ra top doanh thu phim đã update tính đến hiện tại

create or replace function top_revenue_movie(in num int) 
returns table (
	movie_id int,
	title varchar(30),
	revenue int
) as
$$
begin
	return query
	select m.movie_id, m.title, m.revenue
	from movie m
	order by revenue desc
	limit num;
end;
$$ language plpgsql;

-- Function xóa hết các discount mà hết hạn
create or replace function tf_on_delete_discount()
returns void as
$$
begin
	delete from discount where date_expire < current_date;
end;
$$ language plpgsql;