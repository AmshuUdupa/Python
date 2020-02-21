print("Reading from a file ... ")

employee_file = open("employee.txt", "r")

#C:\Users\akoteshw\PycharmProjects\Chap01\

print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline()[0])
#print(employee_file.readlines()[1])

employee_file.readlines()

'''
for employee in employee_file.readlines():
    print(employee)
'''


employee_file.close()