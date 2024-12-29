# FILE: view.py
from tkinter import ttk
import psycopg2
from psycopg2 import sql
from customtkinter import *
from tkinter import *

def total_ticket_sold_per_movie_per_days(connection, start_date):
     try:
        cursor = connection.cursor()
        cursor.execute(
             sql.SQL(
                 """
                 SELECT start_dates, total_ticket_sold, movie_name FROM ticket_sold(%s);
                """
             ), (start_date,)
         )
        records = cursor.fetchall()
        print("Successfully")
        return records
     except Exception as error:
        print(f"Error fetching data: {error}")
        return []
     finally:
        cursor.close()

def top_spending_customers(connection, n):
    try:
        cursor = connection.cursor()
        cursor.execute(
            sql.SQL(
                """
                SELECT first_name || ' ' || last_name AS Name, email,phone,username,total_amounts, ranks FROM vip_customer(%s);
                """
            ),
            (n,)
        )
        records = cursor.fetchall()
        print("Successfully")
        return records
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()

def search_ticket_by_date(connection, start_date, end_date):
    try:
        cursor = connection.cursor()
        cursor.execute(
            sql.SQL(
                """
                SELECT ticket_id, username, schedule_movie_date, schedule_movie_start, 
                    room_name, cinema_name, movie_title, total_money, discount_value, 
                    seat_details, product_details 
                FROM view_ticket 
                WHERE schedule_movie_date >= %s AND schedule_movie_date <= %s 
                ORDER BY schedule_movie_date DESC;
                """
            ),
            (start_date, end_date) 
        )
        records = cursor.fetchall()
        print("Successfully")
        return records
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()


def search_ticket(connection, ticket_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            sql.SQL("SELECT ticket_ids ,usernames, schedule_movie_dates, schedule_movie_starts, room_names,cinema_names, movie_titles, total_moneys, discount_values,seat_detail, product_detail FROM search_ticket(%s) ;"),
            (int(ticket_id),),
        )
        record = cursor.fetchall()
        print("Successfully")
        return record
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()

def search_history(connection, username, gmail):
    try:
        cursor = connection.cursor()
        cursor.execute(
            sql.SQL("SELECT * FROM history_trans(%s, %s);"),
            (username, gmail),
        )
        record = cursor.fetchall()
        print("Successfully")
        return record
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()


def view_ticket(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ticket_id,username, schedule_movie_date, schedule_movie_start, room_name,cinema_name, movie_title, total_money, discount_value, seat_details, product_details FROM view_ticket WHERE schedule_movie_date >= '2024-11-17' ORDER BY schedule_movie_date DESC ;")
        records = cursor.fetchall()
        print("Successfully")
        return records
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()

def view_customers(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT first_name || ' ' || last_name AS Name, email,phone,address,city,username,total_amount FROM users;")
        records = cursor.fetchall()
        print("Successfully")
        return records
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()

def view_schedule(connection):
    try:
        # Connect to your postgres DB
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM view_schedule ORDER BY schedule_movie_date DESC;")

        # Retrieve query results
        records = cursor.fetchall()
        print("Successfully")
        return records

    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()


def fetch_students(connection):
    try:
        # Connect to your postgres DB
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM movie;")

        # Retrieve query results
        records = cursor.fetchall()
        print("Successfully")
        return records

    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()

def fetch_movies(connection):
    try:
        # Connect to your postgres DB
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT title, overview, original_language, release_date, runtime, status, tagline FROM movie ORDER BY release_date DESC LIMIT 100;")

        # Retrieve query results
        records = cursor.fetchall()
        print("Successfully")
        return records

    except Exception as error:
        print(f"Error fetching data: {error}")
        return []
    finally:
        cursor.close()