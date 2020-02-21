print("Writing to the file .... ")

employee_file = open("employee_new.txt",'a')

print("Writable: "+str(employee_file.writable()))

emp_name = input("Enter Employee name : ")
emp_dept = input("Enter employee department: ")

employee_file.write("\n"+emp_name+" - "+emp_dept)

employee_file.close()

employee_file2 = open("employee.txt",'r')

for employee in employee_file2.readlines():
    print(employee)

employee_file2.close()