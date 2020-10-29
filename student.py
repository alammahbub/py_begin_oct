# class starts with class keyword
class Student:
    # constructor name as __init__(self)
    def __init__(self,name="No name",major="No Subject", gpa=0.0, is_on_probation=False):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    # Every class function should have self as parameter
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
# inheritance
class Topper(Student):
    def title(self):
        return "I'm a topper"
    # overriding
    def on_honor_roll(self):
        if self.gpa >= 3.8:
            return True
        else:
            return False