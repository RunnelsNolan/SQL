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

       

        #login = self.login_entry.get()

        #pw = self.password_entry.get()

        login = 'Nolan_runnels1'
        pw = 'MIS4322student'

 

 

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

 
        # conect to server
        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()  #creates a cursor
        #a cursor is a space in memeory that holds abunch of records

        cursor.execute('select * from School.dbo.Course') #grabbing the datavfrom that table

        data = cursor.fetchall()
        print(data)

        

        for course in data:
            courseID = course[0]
            title = course[1]
            credits = course[2]
            deptID = course[3]
            
            preList = {'CourseID': courseID, 'Title': title, 'Credits': credits, 'DeptID': deptID}
            courseList.append(preList) #creates a list of dictionaries
        
        a = int(input("Enter Course ID: " ))

        for dictionary in courseList:
            if a == dictionary['CourseID']:
                print(f'Title: {dictionary["Title"]}')
                print(f'Credits: {dictionary["Credits"]}')
                print(f'Dept ID: {dictionary["DeptID"]}')



 

myinstance = SQLLogin()

print("moving on.....")