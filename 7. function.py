# By using def keyword we can define a function that can have none or one to many parameter
# We can use default parameter if there is no parameter supplied it will be used
def sayHi(name="user"):
    print("Hello "+name)

# function will be executed when it is called not before or after
print("Top")
sayHi("mahbub")
print("Bottom")
sayHi()

# return keyword can change execution path and send feadback to the function calling position
def cube(num):
    return num*num*num


print(cube(3))