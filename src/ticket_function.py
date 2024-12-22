from functions import *

def tickets(connection, right_panel):
    clear_pannel(right_panel)

    right_panel.grid_columnconfigure(0, weight=20, uniform="proportional")
    right_panel.grid_columnconfigure(1, weight=1, uniform="proportional")
    right_panel.grid_rowconfigure(0, weight=1)  # Allow the row to stretch vertically

    table_frame = CTkFrame(right_panel)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")

    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")
    
    table = ttk.Treeview(
        table_frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9), show="headings", xscrollcommand=h_scrollbar.set
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
    column_widths = {
        1: 30,
        2: 100,
        3: 100,
        4: 100,
        5: 100,
        6: 800,
        7: 200,
        8: 80,
        9: 80,
    }
    for col, width in column_widths.items():
        table.column(col, width=width, anchor="nw")
    for record in view_ticket(connection):
        table.insert("", "end", values=record)