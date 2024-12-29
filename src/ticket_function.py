from functions import *

def tickets(connection, right_panel):
    clear_pannel(right_panel)

    right_panel.grid_columnconfigure(0, weight=15, uniform="proportional")
    right_panel.grid_columnconfigure(1, weight=3, uniform="proportional")
    right_panel.grid_rowconfigure(0, weight=1)  # Allow the row to stretch vertically

    table_frame = CTkFrame(right_panel)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")

    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")
    
    table = ttk.Treeview(
        table_frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11), show="headings", xscrollcommand=h_scrollbar.set
    )
    table.pack(side="left", fill="both", expand=True)
    h_scrollbar.config(command=table.xview)
    
    v_scrollbar = Scrollbar(table_frame, orient="vertical", command=table.yview)
    v_scrollbar.pack(side="right", fill="y")
    table.config(yscrollcommand=v_scrollbar.set)

    table.heading(1, text="ticket_id")
    table.heading(2, text="username")
    table.heading(3, text="schedule_movie_date")
    table.heading(4, text="schedule_movie_start")
    table.heading(5, text="room_name")
    table.heading(6, text="cinema_name")
    table.heading(7, text="movie_title")
    table.heading(8, text="ticket_price")
    table.heading(9, text="discount_value")
    table.heading(10, text="seat_detail")
    table.heading(11, text="product_detail")
    column_widths = {
        1: 30,
        2: 100,
        3: 120,
        4: 120,
        5: 100,
        6: 100,
        7: 300,
        8: 80,
        9: 80,
        10: 150,
        11: 150
    }
    for col, width in column_widths.items():
        table.column(col, width=width, anchor="nw")
    for record in view_ticket(connection):
        table.insert("", "end", values=record)
    

    button_frame = CTkFrame(right_panel)
    button_frame.grid(row=20, column=0, padx=10, pady=10, sticky="nsew")
   
    delete_button = CTkButton(
        button_frame, text="Search for ticket", fg_color="#4B9BE5",text_color="white", command=lambda: Search(connection, right_panel, table)
    )
    delete_button.grid(row=0, column=0, padx=5, pady=5)

    update_button = CTkButton(
        button_frame, text="history_transaction", fg_color="#4B9BE5",text_color="white", command=lambda: history_transaction(connection, right_panel, table_frame, table)
    )
    update_button.grid(row=0, column=1, padx=5, pady=5)

    insert_button = CTkButton(
        button_frame, text="Search by date", fg_color="#4B9BE5",text_color="white", command=lambda: search_by_date(connection, right_panel, table_frame, table)
    )
    insert_button.grid(row=0, column=2, padx=5, pady=5)
    insert_button = CTkButton(
        button_frame, text="Total ticket sold per day of each movie", fg_color="#4B9BE5",text_color="white", command=lambda: total_ticket_sold_per_movie_per_day(connection, right_panel, table_frame)
    )
    
    insert_button.grid(row=0, column=3, padx=5, pady=5)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)

    button_frame1 = CTkFrame(right_panel)
    button_frame1.grid(row=20, column=1, padx=10, pady=10, sticky="nsew")
    back_button = CTkButton(
        button_frame1, text="Back", fg_color="#4B9BE5",text_color="white", command=lambda: tickets(connection, right_panel)
    )
    back_button.grid(row=0, column=0, padx=5, pady=5)
    button_frame1.grid_columnconfigure(0, weight=1)

def Search(connection, right_panel, table, left_panel=None):
    if left_panel:
        clear_pannel(left_panel)
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = CTkLabel(input_frame, text="Input the ID of each ticket", font=("Open Sans", 10))
    label.grid(row =0, column =2, columnspan=2, padx=30, pady=5, sticky="w")
    entry = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry.grid(row=1, column=2, columnspan=2, sticky="ew")

    def submit_search():
        search_data = entry.get().strip()
        print(f"Field: {search_data}")
        for item in table.get_children():
            table.delete(item)

        for record in search_ticket(connection, search_data):
            table.insert("", "end", values=record)

    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_search,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row= 1 * 2 + 2, column=2, columnspan=2, pady=10, padx=30, sticky="w")


def history_transaction(connection, right_panel, table_frame,table, left_panel = None):
    if left_panel:
        clear_pannel(left_panel)
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    label = CTkLabel(input_frame, text="Input the username", font=("Open Sans", 15))
    label.grid(row =0, column =2, columnspan=2, padx=30, pady=10, sticky="w")
    entry_usernname = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_usernname.grid(row=1, column=2, columnspan=2, sticky="ew")
    label_gmail = CTkLabel(input_frame,text="Input the gmail", font=("Open Sans", 15))
    label_gmail.grid(row =2, column =2, columnspan=2, padx=30, pady=10, sticky="w")
    entry_gmail = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_gmail.grid(row=3, column=2, columnspan=2, sticky="ew")

    def submit_search():
        clear_pannel(table_frame)
        columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        column_widths = [80, 180, 90, 140, 60, 100, 100, 80, 80, 100, 80]
        headings = [
            "Username", "Email", "Name", "Movie", 
            "Room", "Money_Ticket", "Feedback", "Discount", 
            "Staff", "Date", "Start"
        ]
        table_frame1, table1 = create_table_frame(right_panel, columns, column_widths, headings)
        
        search_data = entry_usernname.get().strip()
        search_gmail = entry_gmail.get().strip()
        print(f"Field: {search_data}")
        for record in search_history(connection, search_data, search_gmail):
            table1.insert("", "end", values=record)
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_search,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=4, column=2, columnspan=2, pady=10, padx=30, sticky="w")


def ticket_sold(connection, right_panel, table_frame,table, left_panel = None):
    return None

def search_by_date(connection, right_panel, table_frame,table, left_panel = None):
    if left_panel:
        clear_pannel(left_panel)
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = CTkLabel(input_frame, text="Input the start date", font=("Open Sans", 10))
    label.grid(row =0, column =2, columnspan=2, padx=30, pady=5, sticky="w")
    entry_start = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_start.grid(row=1, column=2, columnspan=2, sticky="ew")
    
    label = CTkLabel(input_frame, text="Input the end date", font=("Open Sans", 10))
    label.grid(row =2, column =2, columnspan=2, padx=30, pady=5, sticky="w")
    entry_end = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_end.grid(row=3, column=2, columnspan=2, sticky="ew")
    
    def submit_search():
        start = entry_start.get().strip()
        end = entry_end.get().strip()
        print(f"Field: {start} - {end}")
        for item in table.get_children():
            table.delete(item)

        for record in search_ticket_by_date(connection, start, end):
            table.insert("", "end", values=record)
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_search,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=4, column=2, columnspan=2, pady=10, padx=30, sticky="w")

def total_ticket_sold_per_movie_per_day(connection, right_panel, table_frame, left_panel = None):
    if left_panel:
        clear_pannel(left_panel)
    
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = CTkLabel(input_frame, text="Input the start date", font=("Open Sans", 10))
    label.grid(row =0, column =2, columnspan=2, padx=30, pady=5, sticky="w")
    entry_start = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_start.grid(row=1, column=2, columnspan=2, sticky="ew")

    def submit_search():
        start = entry_start.get().strip()
        print(f"Field: {start}")
        
        clear_pannel(table_frame)
        columns = [1, 2, 3]
        column_widths = [80, 180, 90]
        headings = [
            "Date", "Total Ticket", "Movie"
        ]
        table_frame1, table1 = create_table_frame(right_panel, columns, column_widths, headings)

        for record in total_ticket_sold_per_movie_per_days(connection, start):
            table1.insert("", "end", values=record)
    
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_search,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=4, column=2, columnspan=2, pady=10, padx=30, sticky="w")

    
    

def create_table_frame(parent, columns, column_widths, headings):
    table_frame = CTkFrame(parent)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")
    
    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")
    
    table = ttk.Treeview(
        table_frame, columns=columns, show="headings", xscrollcommand=h_scrollbar.set
    )
    table.pack(side="left", fill="both", expand=True)
    h_scrollbar.config(command=table.xview)
    
    v_scrollbar = Scrollbar(table_frame, orient="vertical", command=table.yview)
    v_scrollbar.pack(side="right", fill="y")
    table.config(yscrollcommand=v_scrollbar.set)
    
    for col, width in zip(columns, column_widths):
        table.heading(col, text=headings[col - 1])
        table.column(col, width=width, anchor="nw")
    
    return table_frame, table
