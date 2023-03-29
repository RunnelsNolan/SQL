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
cursor.execute('exec getStudentEmail')

data = cursor.fetchall()

print('First Name          Last Name:        Personal Email:           Work Email:       ')

for row in data:
        print(row[0],'\t\t' ,row[1], '\t\t' ,row[2], '\t\t' ,row[3])