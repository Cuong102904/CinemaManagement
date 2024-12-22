# FILE: view.py
from tkinter import ttk
import psycopg2
from psycopg2 import sql
from customtkinter import *
from tkinter import *

def view_ticket(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT ticket_id,username, schedule_movie_date, schedule_movie_start, room_name,cinema_name, movie_title, total_money, discount_value FROM view_ticket;")
        records = cursor.fetchall()
        print("Successfully")
        return records
    except Exception as error:
        print(f"Error fetching data: {error}")
        return []

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
def fetch_movies(connection):
    try:
        # Connect to your postgres DB
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT title, overview, original_language, release_date, runtime, status, tagline FROM movie;")

        # Retrieve query results
        records = cursor.fetchall()
        print("Successfully")
        return records

    except Exception as error:
        print(f"Error fetching data: {error}")
        return []