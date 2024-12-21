# FILE: view.py
from tkinter import ttk
import psycopg2
from psycopg2 import sql
from customtkinter import *
from tkinter import *



def fetch_students(connection):
    try:
        # Connect to your postgres DB
        cursor = connection.cursor()

        # Execute a query
        cursor.execute("SELECT * FROM clazz;")

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
        cursor.execute("SELECT * FROM class_infos;")

        # Retrieve query results
        records = cursor.fetchall()
        print("Successfully")
        return records

    except Exception as error:
        print(f"Error fetching data: {error}")
        return []