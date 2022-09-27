from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#--------------------------------------

employee_hired_early_2022 = ['David Mustermann', 98738]
employee_hired_late_2022 = ['Jakob Mustermann', 24512]

f = open('employee_list.txt', 'w')
f.write("""
------------------------
        Name, ID
------------------------
\n""")
f.write(str(employee_hired_early_2022) + '\n')
f.write(str(employee_hired_late_2022) + '\n')
f.write("""
*** 
Time when this text file was opened: 
""" + current_time +
"\n***")
f.close()




