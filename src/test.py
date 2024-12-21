import tkinter as tk
from tkinter import ttk

import customtkinter as ctk
from customtkinter import *
import tkinter.messagebox as tkmb 

class LowerPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightgray")
        label = tk.Label(self, text="Lower Panel", bg="lightgray")
        label.pack(expand=True, fill=tk.BOTH)
        self.label1 = CTkLabel(self, text='LOGIN')
        self.label1.pack(pady=12,padx=10)


class UpperPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightblue")
        label = tk.Label(self, text="Upper Panel", bg="lightblue")
        label.pack(expand=True, fill=tk.BOTH)


class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Screen")
        self.geometry("1200x900")

        # Create Upper and Lower Panels
        upper_pane = UpperPanel(self)
        lower_pane = LowerPanel(self)

        # Create a PanedWindow (split pane)
        split_pane = tk.PanedWindow(self, orient=tk.VERTICAL, sashrelief=tk.RAISED)
        split_pane.pack(fill=tk.BOTH, expand=True)

        # Add panels to the split pane
        split_pane.add(upper_pane)
        split_pane.add(lower_pane)

        # Set initial proportions (similar to setResizeWeight)
        self.update_idletasks()  # Ensure sizes are calculated before resizing
        split_pane.paneconfig(upper_pane, minsize=600)
        split_pane.paneconfig(lower_pane, minsize=300)


# Run the application
if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()
