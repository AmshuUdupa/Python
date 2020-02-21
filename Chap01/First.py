
def get_file_ext(filename):
    try:
        return filename[filename.index(".")+1:]

    except ValueError as err:
        print(err)

filename = "Employee.txt"

print(filename[0:])
print(get_file_ext(input("enter the file name: ")))