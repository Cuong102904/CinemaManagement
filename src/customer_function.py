from functions import *
from view import *
from CTkMessagebox import CTkMessagebox
import customtkinter


def customers(connection, right_panel):
    clear_pannel(right_panel)

    right_panel.grid_columnconfigure(0, weight=5, uniform="proportional")
    right_panel.grid_columnconfigure(1, weight=1, uniform="proportional")
    right_panel.grid_rowconfigure(0, weight=1)  # Allow the row to stretch vertically

    table_frame = CTkFrame(right_panel)
    table_frame.grid(row=0, column=0, rowspan=20, padx=10, pady=10, sticky="nsew")

    h_scrollbar = Scrollbar(table_frame, orient="horizontal")
    h_scrollbar.pack(side="bottom", fill="x")
    
    table = ttk.Treeview(
        table_frame, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", xscrollcommand=h_scrollbar.set
    )
    table.pack(side="left", fill="both", expand=True)
    h_scrollbar.config(command=table.xview)
    
    v_scrollbar = Scrollbar(table_frame, orient="vertical", command=table.yview)
    v_scrollbar.pack(side="right", fill="y")
    table.config(yscrollcommand=v_scrollbar.set)

    table.heading(1, text="Name")
    table.heading(2, text="Email")
    table.heading(3, text="Phone")
    table.heading(4, text="Address")
    table.heading(5, text="City")
    table.heading(6, text="Username")
    table.heading(7, text="Total Spent")
    column_widths = {
        1: 100,
        2: 300,
        3: 100,
        4: 300,
        5: 200,
        6: 200,
        7: 80,
    }
    for col, width in column_widths.items():
        table.column(col, width=width, anchor="nw")
    for record in view_customers(connection):
        table.insert("", "end", values=record)
# The input side of the right panel
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    input_frame.grid_columnconfigure(2, weight=1)  # Allows column 2 to expand
    fields = ["First_name", "Last_name", "Address", "City", "Email", "Phone",  "Username", "Password"]
    entries = {}

    for i, field in enumerate(fields):
        label = CTkLabel(input_frame, text=field, font=("Open Sans", 14), text_color="#D9D9D9")
        label.grid(row=i * 2, column=2, columnspan=2, pady = 5, sticky="ew")
        entry = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
        entry.grid(row=i * 2 + 1, column=2, columnspan=2, sticky="ew")
        entries[field] = entry

    def add_users():
        user_data = {}
        for field, entry in entries.items():
            user_data[field] = entry.get().strip()

        try:
            with connection.cursor() as cursor:
                insert_query = sql.SQL("""
                INSERT INTO users(first_name, last_name,address,city,email,phone,username,password)
                                VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
                """)
                cursor.execute(insert_query, (user_data["First_name"], 
                                              user_data["Last_name"], 
                                              user_data["Address"], 
                                              user_data["City"], 
                                              user_data["Email"], 
                                              user_data["Phone"], 
                                              user_data["Username"], 
                                              user_data["Password"],
                ))
                connection.commit()
                print("Successfully inserted data into the database")
        except Exception as e:
            print(f"Error inserting data into the database: {e}")
            connection.rollback()
        finally:
            cursor.close()
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=add_users,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=len(fields) * 2 + 2, column=2, columnspan=2, pady=10, padx=30, sticky="w")

    button_frame = CTkFrame(right_panel)
    button_frame.grid(row=20, column=0, padx=10, pady=10, sticky="nsew")
    # Create Delete, Update, Insert buttons
    delete_button = CTkButton(
        button_frame, text="Delete", fg_color="red", text_color="white", command=lambda: delete_schedule(connection, input_frame, table)
    )
    delete_button.grid(row=0, column=0, padx=5, pady=5)

    update_button = CTkButton(
         button_frame, text="Insert", fg_color="green", text_color="white", command=lambda: customers(connection, right_panel)
    )
    update_button.grid(row=0, column=1, padx=5, pady=5)

    insert_button = CTkButton(
         button_frame, text="Top spending", fg_color="orange", text_color="white", command=lambda: top_spending(connection, input_frame, table)   
         )
    insert_button.grid(row=0, column=2, padx=5, pady=5)

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_columnconfigure(2, weight=1)
    

def delete_schedule(connection, right_panel,table):
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
        username = item_values[5]
        email = item_values[1]
        phone = item_values[2]
        print(f"Deleting user having: {username}, {email}, {phone}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM users
                    WHERE username = %s AND email = %s AND phone = %s
                    """,
                    (username, email, phone),
                )
                connection.commit()
                print(f"User deleted: {username}, {email}, {phone}")
                table.delete(selected_item)
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            cursor.close()



def top_spending(connection, right_panel, table):
    input_frame = CTkFrame(right_panel)
    input_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    Label = CTkLabel(input_frame, text="Top spending customers", font=("Open Sans", 14), text_color="#D9D9D9")
    Label.grid(row=0, column=2, columnspan=2, pady = 5, sticky="ew")
    label_input = CTkLabel(input_frame, text="Input n (Top n):", font=("Open Sans", 14), text_color="#D9D9D9")
    label_input.grid(row=1, column=2, columnspan=2, pady = 5, sticky="ew")
    entry_input = CTkEntry(input_frame, font=("Open Sans", 14), border_width=2, corner_radius=10)
    entry_input.grid(row=2, column=2, columnspan=2, sticky="ew")

    def submit_search():
        for row in table.get_children():
            table.delete(row)
        n = entry_input.get().strip()
        if n.isdigit():
            n = int(n)
            records = top_spending_customers(connection, n)
            new_columns = (1, 2, 4, 5, 6, 7)
            table["columns"] = new_columns

            # Update the headings
            table.heading(1, text="Name")
            table.heading(2, text="Email")
            table.heading(4, text="Phone")
            table.heading(5, text="Username")
            table.heading(6, text="Total Spent")
            table.heading(7, text="Ranks")

            # Update column widths
            new_column_widths = {
                1: 100,
                2: 300,
                4: 300,
                5: 200,
                6: 200,
                7: 80,
            }
            for col, width in new_column_widths.items():
                table.column(col, width=width, anchor="nw")
            for record in records:
                    table.insert("", "end", values=record)
        else:
            print("Invalid input. Please enter a number.")
    submit_button = CTkButton(
        input_frame,
        text="Submit",
        command=submit_search,
        fg_color="#4B9BE5",
        text_color="white"
    )
    submit_button.grid(row=3, column=2, columnspan=2, pady=10, padx=30, sticky="w")
