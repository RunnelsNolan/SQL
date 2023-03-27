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



'''
1)
Calculate the new budget for each department. Every department will be getting a 10% increase in their budget except for 
the Information Systems (IS) and Computer Science (CS) departments. The IS department gets a 20% increase and the 
CS department gets a 15 % increase. Create a well formatted report that shows each department name, their 
current budget, their new budget and the amount increased.



Dept Name				Original Budget		New Budget		Increse in Budget
Engineering				$350,000.00			$385,000.00		$35,000.00
English					$120,000.00			$132,000.00		$12,000.00
Economics				$200,000.00			$220,000.00		$20,000.00
Mathematics				$250,000.00			$275,000.00		$25,000.00
Information Systems		$375,000.00			$450,000.00		$75,000.00
Computer Science		$310,500.00			$357,075.00		$46,575.00

'''
cursor.execute('select name, budget from school.dbo.Department')
data1 = cursor.fetchall()

print(format('Dept Name', '<20'), format('Original Budget','<15'), format('New Budget', '<15'),format('Increase in Budget','<15') )
for row in data1:
    dept = row[0]
    budget = float(row[1])
    if dept == 'Information Systems':
        new_budget = budget + (budget*.20)
    elif dept == 'Computer Science':
        new_budget = budget + (budget*.15)
    else:
        new_budget = budget + (budget*.10)
    
    difference = new_budget - budget


    print(format(dept,'<20'), '$' ,format(budget, '<15,.2f'),  '$' ,format(new_budget, '<15,.2f'),  '$' ,format(difference, ',.2f'),sep = "")





'''
2)
Display First Name, Last Name and corresponding personal and work email
for STUDENTS ONLY using Person and Contact_Info tables as shown below (only first row shown):


firstname	lastname	Personal Email					Work Email
Gytis		Barzdukas	josephine_darakjy@darakjy.org	ezekiel@chui.com
Peggy		Justice		art@venere.org					wkusko@yahoo.com
Yan			Li			lpaprocki@hotmail.com			bfigeroa@aol.com
Laura		Norman		donette.foller@cox.net			ammie@corrio.com
Nino		Olivotto	simona@morasca.com				francine_vocelka@vocelka.com

'''
cursor.execute('select First_Name, Last_Name, ci1.Email, ci2.Email from school.dbo.Person inner join school.dbo.contact_info as ci1 on Person.PersonID = ci1.PersonID and ci1.Email_Type = "Personal" inner join school.dbo.contact_info as ci2 on Person.PersonID = ci2.PersonID and ci2.Email_Type = "Work" ')
data2 = cursor.fetchall()
print(data2)

""" for row in data2:
    hire_date = row[3]
    first_name = row[2]
    last_name = row[1]
    personal_email = row[10]
    work_email = row[]
 """
#print(data2)







'''
3)
Display First Name, Last Name and corresponding home,cell and work phone numbers
for instructors only using Person and Contact_Info tables as shown below (only first 2 rows shown):

FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone
Kim			Abercrombie		(504) 621-8927	(410) 621-8927	(313) 621-8927
Fadi		Fakhouri		(810) 292-9388	(215) 292-9388	(815) 292-9388

'''



