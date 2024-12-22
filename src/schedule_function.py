from functions import *
from tkinter import ttk
from customtkinter import *
from tkinter import *
from view import *
from style import *
import datetime

import pandas as pd
import csv

import pandas as pd

def add_schedule(file_path, connection):
    # Ensure file_path is a string if wrapped in an object
    if hasattr(file_path, 'get'):
        file_path = file_path.get()
    
    print("Adding schedule...")
    cursor = connection.cursor()

    try:
        csv_reader = pd.read_csv(file_path)

        for index, row in csv_reader.iterrows():
            schedule_date = row["Date"]
            start_time = row["Start Time"]
            room = row["Room"]
            movie = row["Movie"].strip()

            cursor.execute("SELECT movie_id FROM movie WHERE title = %s", (movie,))
            movie_id = cursor.fetchone()
            if not movie_id:
                print(f"Movie '{movie}' not found in the database. Skipping...")
                continue
            movie_id = movie_id[0]

            cursor.execute("SELECT room_id FROM room WHERE name = %s", (room,))
            room_id = cursor.fetchone()
            if not room_id:
                print(f"Room '{room}' not found in the database. Skipping...")
                continue
            room_id = room_id[0]

            cursor.execute(
                """
                INSERT INTO schedule (schedule_movie_date, schedule_movie_start, room_id, movie_id)
                VALUES (%s, %s, %s, %s)
                """,
                (schedule_date, start_time, room_id, movie_id),
            )
            print(f"Added schedule: {schedule_date}, {start_time}, {room}, {movie}")

        connection.commit()
        print("All schedules added successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()


def schedule(connection, right_panel):
    clear_pannel(right_panel)

    right_panel.grid_columnconfigure(0, weight=5, uniform="proportional")
    right_panel.grid_columnconfigure(1, weight=1, uniform="proportional")
    right_panel.grid_rowconfigure(0, weight=1)  # Allow the row to stretch vertically
    table_frame = CTkFrame(right_panel)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")

    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")
    
    table = ttk.Treeview(
        table_frame, columns=(1, 2, 3, 4, 5), show="headings", xscrollcommand=h_scrollbar.set
    )
    table.pack(side="left", fill="both", expand=True)
    h_scrollbar.config(command=table.xview)
    
    v_scrollbar = Scrollbar(table_frame, orient="vertical", command=table.yview)
    v_scrollbar.pack(side="right", fill="y")
    table.config(yscrollcommand=v_scrollbar.set)

 
    table.heading(1, text="Date")
    table.heading(2, text="Start Time")
    table.heading(3, text="Room")
    table.heading(4, text="Cinema")
    table.heading(5, text="Movie")

    column_widths = {
        1: 200,
        2: 100,
        3: 100,
        4: 100,
        5: 400,
    }
    for col, width in column_widths.items():
        table.column(col, width=width, anchor="w")


    for record in view_schedule(connection):
        table.insert("", "end", values=record)

    ## The input side of the right panel
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = CTkLabel(input_frame, text="Input", font=("Open Sans", 20))
    label.grid(row =0, column =2, columnspan=2, padx=30, pady=5, sticky="w")

    file_path = StringVar() 
    def UploadAction(event=None):
        path_choose = filedialog.askopenfilename()
        file_path.set(path_choose)
        print('Selected:', path_choose)
    
    Button = CTkButton(input_frame, text="Upload", command=UploadAction)
    Button.grid(row=1, column=2, columnspan=2, padx=30, pady=5, sticky="w")

    Submit = CTkButton(input_frame, text="Submit", command=lambda: add_schedule(file_path, connection))
    Submit.grid(row=2, column=2, columnspan=2, padx=30, pady=5, sticky="w")


    button_frame = CTkFrame(right_panel)
    button_frame.grid(row=20, column=0, padx=10, pady=10, sticky="nsew")
    # Create Delete, Update, Insert buttons
    delete_button = CTkButton(
        button_frame, text="Delete", fg_color="red", text_color="white", command=lambda: delete_schedule(connection, input_frame, table)
    )
    delete_button.grid(row=0, column=0, padx=5, pady=5)

    update_button = CTkButton(
        button_frame, text="Update", fg_color="orange", text_color="white"
    )
    update_button.grid(row=0, column=1, padx=5, pady=5)

    insert_button = CTkButton(
        button_frame, text="Insert", fg_color="green", text_color="white", command=lambda: schedule(connection, right_panel)
    )
    insert_button.grid(row=0, column=2, padx=5, pady=5)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)


def delete_schedule(connection, right_panel, table):
    clear_pannel(right_panel)
    # get yes/no answers
    msg = CTkMessagebox(title="Delete?", message="Are you sure babi?",
                        icon="question", option_1="Cancel",option_2="Yes")
    response = msg.get()
    
    if response=="Yes":    
        selected_item = table.selection()
        if not selected_item:
            print("Error: No schedule selected.")
            return
        print(selected_item)
        item_values = table.item(selected_item, "values")
        schedule_date = item_values[0]
        start_time = item_values[1]
        room = item_values[2]
        movie = item_values[4]

        print(f"Deleting schedule: {schedule_date}, {start_time}, {room}, {movie}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM schedule
                    WHERE schedule_movie_date = %s AND schedule_movie_start = %s
                    AND room_id = (SELECT room_id FROM room WHERE name = %s)
                    AND movie_id = (SELECT movie_id FROM movie WHERE title = %s)
                    """,
                    (schedule_date, start_time,room, movie),
                )
                connection.commit()
                print(f"Schedule deleted: {schedule_date}, {start_time}, {room}, {movie}")
                table.delete(selected_item)
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()

