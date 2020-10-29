# if can execute an instruction if condition meet
# if requirements not full-filled then else will come into play
def check(num):
    if(num%2==0):
        return "even number"
    else:
        return "odd number"

# int() can convert an string to integer
num = input("input a number: ")
print(num+" is an "+check(int (num)))