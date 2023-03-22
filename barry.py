import tkinter as t

import tkinter.messagebox

from tkinter.font import Font

import pyodbc

 

class SQLLogin:

    def __init__(self):

        self.main_window = t.Tk()

        self.main_window.geometry('300x100')

        self.main_window.title('SQL Server Login')

        #self.title_font = Font(family='Source Sans Pro Bold', size=24)

 

        # Frames

        self.login_frame = t.Frame(self.main_window)

        self.password_frame = t.Frame(self.main_window)

        self.button_frame = t.Frame(self.main_window)

      

        

 

        # LABELS

 

        # title

        self.login_label = t.Label(self.login_frame, text="Login:", anchor='w', width = 10)

        self.password_label = t.Label(self.password_frame, text="Password:", anchor='w', width = 10)

   

        # ENTRIES

 

        self.login_entry = t.Entry(self.login_frame, show=None, width=20)

       

        self.password_entry = t.Entry(self.password_frame, show="*", width=20)

       

 

        # BUTTON

 

        self.login_button = t.Button(self.button_frame, text="Login", command=self.access_database)

 

        self.login_label.pack(side="left")

        self.login_entry.pack(side="right")

 

        self.password_label.pack(side='left')

        self.password_entry.pack(side='right')

 

        self.login_button.pack()

     

        self.login_frame.pack()

        self.password_frame.pack()

        self.button_frame.pack()

 

        t.mainloop()

 

    def access_database(self):

       

        login = self.login_entry.get()

        pw = self.password_entry.get()

 

 

        self.main_window.destroy()

 

        print(login, pw)

        preList = {}

        courseList = []

        cn_str = (

            'Driver={SQL Server};' #data source driver

            'Server=MIS-SQLJB;' #server name

            'Database=School;' #database name

            'UID='+login+';' #user name

            'PWD='+pw+';' #user pass

        )

 

        cn = pyodbc.connect(cn_str)

        return

 

myinstance = SQLLogin()

print("moving on.....")