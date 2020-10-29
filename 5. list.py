# list in python start with square brackets
# list can hold any kind of data
friends = ["asib","rony","sajia"]
print(friends)
# accessing list item with there index
print(friends[2]+" has index 2")
# accessing list from back or, as negative index
print(friends[-1]+" has index -1")
# Asigning new item in list by using index
friends[2] = "Borhan"
print(friends[0:2])


# list function

lucky_number = [4,8,9,32,23]
friends = ["Asib","Rony","Sajia","Borhan","Rakib"]
print(friends)
# extend function combine one list with another
friends.extend(lucky_number)
print(friends)
# append add new item at the end
friends.append("Maksud")
print(friends)

# insert can insert data item into any choosen location
friends.insert(4,"Sumon")
print(friends)
# remove delete data item as there index
friends.remove(4)
print(friends)
# pop remove a single item from back or index -1
friends.pop()
print(friends)
# index of an item can be accessed by index function
print(friends.index(9))
friends.append("Borhan")
print(friends.count("Borhan"))

# sort function will sort data in ascending order if there is only same type of data
lucky_number.sort()
print(lucky_number)
# Reverse function rearrenge data item as index 0 = index -1
lucky_number.reverse()
print(lucky_number)
#copy function of a list return all data to a new list
friends2 = friends.copy()
print(friends2)