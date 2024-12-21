import customtkinter as ctk
from customtkinter import *
import tkinter.messagebox as tkmb 
import tkinter
from main_screen import MainScreen

class Login(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x480")
        self.title("Login")
        ctk.set_appearance_mode("dark")
        #ctk.set_default_color_theme("green")
        self.weight()

    def weight(self):
        
        self.label = CTkLabel(self,text="Cinema management system",font=('Arial',30,'bold'))
        self.label.pack(pady=20,padx=10)

        self.frame = CTkFrame(self)
        self.frame.pack(pady=20,padx=40,fill='both',expand=True)

        self.label1 = CTkLabel(self.frame, text='LOGIN', font=('Arial',50,'bold'))
        self.label1.pack(pady=20,padx=10)

        self.user_entry = CTkEntry(self.frame,placeholder_text="Username",text_color='green',height=40,width=220, corner_radius=20,font=("Helvetica", 18))
        self.user_entry.pack(pady=12,padx=10)

        self.user_pass = CTkEntry(self.frame,placeholder_text="Password",show="*",height=40,width=220,corner_radius=20,font=("Helvetica", 18))
        self.user_pass.pack(pady=12,padx=10)
        self.button = CTkButton(self.frame,text='Login',command=self.login,border_color='black',text_color='#EEEEEE',fg_color='#99CCCC',height=40,width=180,font=("Helvetica", 18))
        
        self.button.pack(pady=20,padx=10)

        self.checkbox = CTkCheckBox(self.frame,text='Remember Me')
        self.checkbox.pack(pady=12,padx=10)

    def login(self):
        username = "cuonghoang"
        password = '1234'
        if self.user_entry.get() == username and self.user_pass.get() == password:
            #tkmb.showinfo("Login Success")
            self.destroy()
            dashboard = MainScreen()   
            dashboard.mainloop()
            
        else:
            tkmb.showwarning(title='Wrong password or username',message='Please check your password or username') 
app = Login()
app.mainloop()