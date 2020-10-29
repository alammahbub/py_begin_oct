from student import *

student1 = Student("Jim","Business",3.1,False)
print(student1.name)

print(student1.on_honor_roll())

student2 = Topper()
print(student2.title()+" my major is "+student2.major+" and my topper status is "+str(student2.on_honor_roll()))