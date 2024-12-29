from tkinter import ttk
import psycopg2
from psycopg2 import sql
from customtkinter import *
from tkinter import *


def clear_pannel(panel):
    """Clear all widgets from the right panel."""
    for widget in panel.winfo_children():
        widget.destroy()
    
def connection():
    connection = psycopg2.connect(
        dbname="Cinema_3",
        user="postgres",
        password="1029",
        host="localhost",
        port="5432"
    )
    return connection