from customtkinter import *
from tkinter import *
from dashboard import Dashboard

class MainScreen(CTk):
    def __init__(self):
        super().__init__()
        # Set the window to full-screen mode
        width= self.winfo_screenwidth()               
        height= self.winfo_screenheight()               
        self.geometry("%dx%d" % (width, height))
        self.title("Main Screen")
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        lbltitle = Label(self, bd=20, relief=RIDGE, text="Cinema Management System",
                         fg="red", bg="white", font=('Arial', 20, "bold"))
        
        lbltitle.pack(side=TOP, fill=X)
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side=LEFT, fill=Y, padx=0)
        self.right_panel = CTkFrame(self, corner_radius=0)
        self.right_panel.pack(side=RIGHT, fill=BOTH, expand=True)
        self.dashboard.set_right_panel(self.right_panel)

if __name__ == "__main__":
    root = MainScreen()
    root.mainloop()
