--Q4
CREATE OR REPLACE VIEW view_schedule AS
    SELECT S.schedule_id, S.schedule_movie_date, s.schedule_movie_start, r.name AS room_Name, c.name AS cinema_name, m.title AS movie_title
    FROM schedule S
    JOIN room R ON S.room_id = R.room_id            
    JOIN cinema C ON R.cinema_id = C.cinema_id
    JOIN movie M ON S.movie_id = M.movie_id
    ORDER BY S.schedule_movie_date, s.schedule_movie_start;

--SELECT * FROM view_schedule WHERE schedule_movie_date >= CURRENT_DATE;
-- SELECT * FROM view_schedule WHERE schedule_movie_date = CURRENT_DATE; //schedule for staff who sell ticket directly


--Q5
CREATE OR REPLACE VIEW view_ticket AS
SELECT  t.ticket_id,
        u.username, 
        u.email, 
        s.schedule_movie_date, 
        s.schedule_movie_start, 
        r.name AS room_name, 
        c.name AS cinema_name, 
        m.title AS movie_title, 
        t.total_money, 
        t.feedback, 
        d.value AS discount_value,
        STRING_AGG(DISTINCT sd.seat_id || ' (' || sd.price || ')', ', ') AS seat_details,
        STRING_AGG(
           DISTINCT prd.name || ' (' || p.unit_price || ' x ' || p.quantity || ')', 
            ', '
        ) AS product_details
    FROM ticket t
    JOIN users u ON t.user_id = u.user_id
    JOIN schedule s ON t.schedule_id = s.schedule_id
    JOIN room r ON s.room_id = r.room_id
    JOIN cinema c ON r.cinema_id = c.cinema_id
    JOIN movie m ON s.movie_id = m.movie_id
    LEFT JOIN discount d ON t.discount_id = d.discount_id
    LEFT JOIN seat_detail sd ON t.ticket_id = sd.ticket_id
    LEFT JOIN product_detail p ON t.ticket_id = p.ticket_id
    LEFT JOIN product prd ON p.product_id = prd.product_id
    GROUP BY 
        t.ticket_id, u.username, u.email, s.schedule_movie_date, 
        s.schedule_movie_start, r.name, c.name, m.title, 
        t.total_money, t.feedback, d.value
    ORDER BY 
        s.schedule_movie_date, s.schedule_movie_start

--SELECT * FROM view_ticket WHERE user_id = '';
--Q7
CREATE VIEW StaffSummaryView AS
SELECT 
    c.name AS cinema_name,
    st.staff_id,
    st.name AS staff_name,
    st.email,
    st.role
FROM cinema c
JOIN staff st ON c.cinema_id = st.cinema_id
ORDER BY c.name;
--SELECT * FROM StaffSummaryView WHERE cinema_name = 'cinema_1';

--Q1: tổng doanh thu theo từng ngày
CREATE OR REPLACE VIEW RevenuePerDay AS
    SELECT 
        s.schedule_movie_date,
        r.cinema_id,
        SUM(t.total_money) AS total_revenue
    FROM ticket t
    JOIN schedule s ON t.schedule_id = s.schedule_id
    JOIN room r ON s.room_id = r.room_id
    GROUP BY s.schedule_movie_date, r.cinema_id
    ORDER BY s.schedule_movie_date;

--Q2
CREATE OR REPLACE VIEW crew_details AS
    SELECT name AS "Name", department, gender, job , movie.title AS movie_title, movie.release_date
    FROM crew
    JOIN movie ON crew.movie_id = movie.movie_id;
    

--Q3
CREATE OR REPLACE VIEW cast_details AS 
    SELECT c.name AS Name, c.gender, c.character, c.order, movie.title AS movie_title, movie.release_date
    FROM "cast" c
    JOIN movie ON c.movie_id = movie.movie_id;

--Q8
CREATE OR REPLACE VIEW user_summary AS
    SELECT first_name || ' ' || last_name AS full_name, email, phone, total_amount
    FROM users
    ORDER BY total_amount DESC;
    
    
--Product Sales Reports: Combines products, tickets, and quantities sold per product.
CREATE OR REPLACE VIEW ProductSalesView AS
SELECT 
    p.product_id,
    p.name AS product_name,
    SUM(pd.quantity) AS total_quantity_sold,
    SUM(pd.unit_price) AS total_revenue
FROM product p
JOIN product_detail pd ON p.product_id = pd.product_id
GROUP BY p.product_id, p.name;