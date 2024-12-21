from tkinter import ttk
from customtkinter import *
from tkinter import *
from view import *
from style import *
import datetime

def clear_pannel(panel):
    """Clear all widgets from the right panel."""
    for widget in panel.winfo_children():
        widget.destroy()
    
def views(connection, right_panel): 
    clear_pannel(right_panel)
    label1 = CTkLabel(
            right_panel,
            text="Movies Table 1",

            font=("Open Sans", 20)
        )
    label1.pack(side=TOP)
    table = ttk.Treeview(right_panel, columns=(1, 2, 3, 4), show="headings")
    table.heading(1, text="clazz_id")
    table.heading(1, text="clazz_id")
    table.heading(2, text="name")
    table.heading(3, text="lecturer_id")
    table.heading(4, text="monnitor_id")
    table.pack(padx=10, pady=10, fill=BOTH, expand=True)  

    for record in fetch_students(connection):
        table.insert('', 'end', values=record)




def addmovie(connection, right_panel):
    clear_pannel(right_panel)

    right_panel.grid_columnconfigure(0, weight=3, uniform="proportional")
    right_panel.grid_columnconfigure(1, weight=1, uniform="proportional")


    table_frame = Frame(right_panel)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")

   
    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")

    table = ttk.Treeview(
        table_frame, 
        columns=(1, 2, 3, 4, 5, 6, 7), 
        show="headings", 
        xscrollcommand=h_scrollbar.set
    )
    table.pack(side='left', fill='both', expand=True)

    h_scrollbar.config(command=table.xview)

    table.heading(1, text="Title")
    table.heading(2, text="Overview")
    table.heading(3, text="Original Language")
    table.heading(4, text="Release Date")
    table.heading(5, text="Runtime")
    table.heading(6, text="Status")
    table.heading(7, text="Tagline")

    column_widths = {
        1: 200,  
        2: 300,  
        3: 100,  
        4: 100,  
        5: 50,  
        6: 50,  
        7: 200,  
    }

    for col, width in column_widths.items():
        table.column(col, width=width, anchor="center")  # Set width and alignment

    for record in fetch_movies(connection):  
        table.insert('', 'end', values=record)

# The input side of the right panel

    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


    fields = [
        "Title", "Overview", "Original Language",
        "Release Date", "Runtime", "Status",
        "Tagline"
    ]
    entries = {}

    for i, field in enumerate(fields):
        label = CTkLabel(input_frame, text=field, font=("Open Sans", 14), text_color="#D9D9D9")
        label.grid(row=i * 2, column=2, columnspan=2, padx=30, pady=5, sticky="w")

        if field == "Overview":
            entry = Text(input_frame, font=("Open Sans", 14), height=5, width=40)
        else:
            entry = Entry(input_frame, font=("Open Sans", 14), width=30)
        entry.grid(row=i * 2 + 1, column=2, columnspan=2, padx=30, pady=5, sticky="w")

        entries[field] = entry

    # File selection for URL
    def choose_file():
        """Open a file dialog to select an image file and update the 'URL' entry."""
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All Files", "*.*")]
        )
        if file_path:
            entries["URL"] = file_path_label
            file_path_label.configure(text=file_path)
            

    # Create label and "Choose File" button for URL
    url_label = CTkLabel(input_frame, text="URL (Image File)", font=("Open Sans", 14), text_color="#D9D9D9")
    url_label.grid(row=len(fields) * 2, column=2, columnspan=2, padx=30, pady=5, sticky="w")

    choose_file_button = CTkButton(
        input_frame, text="Choose File", command=choose_file, fg_color="gray", text_color="white"
    )
    choose_file_button.grid(row=len(fields) * 2 + 1, column=2, padx=30, pady=5, sticky="w")

    file_path_label = CTkLabel(input_frame, text="", font=("Open Sans", 12))
    file_path_label.grid(row=len(fields) * 2 + 1, column=2, padx=30, pady=5, sticky="w")

    def submit_movie():
     
        movie_data = {field: (entry.get() if isinstance(entry, Entry) else entry.get("1.0", "end-1c")) for field, entry in entries.items()}
        movie_data["URL"] = file_path_label.cget("text")  # Get the file path from the label
        release_date = movie_data["Release Date"]
        try:
            movie_data["Release Date"] = datetime.datetime.strptime(release_date, "%Y-%m-%d").date()
        except ValueError:
            print("Error: Release Date must be in the format YYYY-MM-DD.")
            return
        
        if not movie_data["Title"] or not movie_data["Original Language"]:
            print("Error: Title and Original Language are required fields.")
            return

        try:
        
            with connection.cursor() as cursor:
                insert_query = sql.SQL("""
                    INSERT INTO movie (title, overview, original_language, release_date, runtime, status, tagline, url)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """)
                cursor.execute(insert_query, (
                    movie_data["Title"],
                    movie_data["Overview"],
                    movie_data["Original Language"],
                    movie_data["Release Date"],
                    int(movie_data["Runtime"]) if movie_data["Runtime"].isdigit() else None,
                    movie_data["Status"],
                    movie_data["Tagline"],
                    movie_data["URL"]
                ))
                connection.commit()
                print("Movie added successfully.")
        except Exception as e:
            print(f"Error inserting data into the database: {e}")
            connection.rollback()

    # Add a submit butto
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_movie,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=len(fields) * 2 + 2, column=2, columnspan=2, pady=10, padx=30, sticky="w")

