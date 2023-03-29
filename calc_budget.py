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
cursor.execute('Slect Name, Budget from School.dbo.Department')

for row in data:
    name = row[0]
    old