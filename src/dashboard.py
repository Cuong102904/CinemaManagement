from tkinter import ttk
from customtkinter import *
from tkinter import *
from view import *
from style import *

from functions import *
from schedule_function import *
from customer_function import *
from ticket_function import *
class Dashboard(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.right_panel = None  # Placeholder for the right panel
        self.style = style_table() # Apply the custom style to the Treeview
        # UI for the Dashboard
        self.label = CTkLabel(self, text="Dashboard", text_color='red',font=("Open Sans", 30))
        self.label.pack(side=TOP, pady=20, padx=20)

        # Buttons
        self.view_button = CTkButton(self, text="View", command=self.handle_views)
        self.view_button.pack(padx=20, pady=20, fill=Y)

        self.movie_button = CTkButton(self, text="Movie", command=self.handle_movies)
        self.movie_button.pack(padx=20, pady=20, fill=Y)

        self.customer_button = CTkButton(self, text="Customer", command=self.handle_customers)
        self.customer_button.pack(padx=20, pady=20, fill=Y)

        self.ticket_button = CTkButton(self, text="Ticket", command=self.handle_ticket)
        self.ticket_button.pack(padx=20, pady=20, fill=Y)

        self.ticket_button = CTkButton(self, text="Schedule", command=self.handle_schedule)
        self.ticket_button.pack(padx=20, pady=20, fill=Y)  

        self.connection = psycopg2.connect(
            dbname="CinemaManagement",
            user="postgres",
            password="1029",
            host="localhost",
            port="5432"
        )
    def set_right_panel(self, panel):
        """Set the right panel for dynamic content."""
        self.right_panel = panel


    def handle_views(self):
        """Handle the 'View' button click."""
        if self.right_panel:
            views(self.connection, self.right_panel)
    def handle_movies(self):
        if self.right_panel:
            addmovie(self.connection, self.right_panel)        
    def handle_schedule(self):
        if self.right_panel:
            schedule(self.connection, self.right_panel)
    def handle_customers(self):
        if self.right_panel:
            customers(self.connection, self.right_panel)
    def handle_ticket(self):
        if self.right_panel:
            tickets(self.connection, self.right_panel)    
