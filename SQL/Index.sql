CREATE INDEX idx_schedule_date_start ON schedule (schedule_movie_date);
-- DROP INDEX idx_schedule_date_start 
--explain analyze SELECT * FROM view_schedule WHERE schedule_movie_date >= CURRENT_DATE;



--DROP INDEX idx_movie_name
CREATE INDEX idx_movie_name ON movie USING HASH(title)
--CREATE INDEX idx_movie_name ON movie USING btree(title)

-- explain analyze
-- SELECT title, overview, original_language, release_date ,status,tagline,runtime
--     FROM movie
--     WHERE title = 'Avatar';

CREATE INDEX idx_total_revenue ON users (total_amount);
-- DROP INDEX idx_total_revenue
-- explain analyze SELECT * FROM users ORDER BY total_amount

CREATE INDEX idx_schedule_id ON schedule (schedule_id);

