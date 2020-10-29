# file can be opened for read, write, append and to do both read and write
# readline will return a single line
# readlines will return line after line
# file obeject.readable() will return a boolean value confirming that is it readable or not
employee_file =  open("employee.txt","r")
if(employee_file.readable()):
    for lines in employee_file.readlines():
        print(lines)
# file object. close will close file and it is a good practice
employee_file.close()


add = input("Do you want to say something new? ")

employee_file = open("employee.txt","a")
# using write function we can write data to a file
employee_file.write(add);
employee_file.close()
