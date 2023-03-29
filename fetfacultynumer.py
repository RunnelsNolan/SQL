import pyodbc

login = 'Nolan_runnels1'
pw = 'MIS4322student'

cn_str = (

            'Driver={SQL Server};' #data source driver

            'Server=MIS-SQLJB;' #server name

            'Database=School;' #database name

            'UID='+login+';' #user name

            'PWD='+pw+';' #user pass

)
# conect to server
cn = pyodbc.connect(cn_str)
cursor = cn.cursor()
cursor.execute('exec getFacultyPhone')

data = cursor.fetchall()

print('FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone')

for row in data:
    print(row[0],'\t\t' ,row[1], '\t\t' ,row[2], '\t\t' ,row[3], '\t\t' ,row[4])