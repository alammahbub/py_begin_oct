# if try block produce an error then except block will catch that error and response as required

try:
    value = 5/0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print("Input number other than zero: "+str(err))
except ValueError:
    print("Invalid Input")