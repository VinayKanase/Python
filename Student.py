
# This is Student Class
# Used in 21_classesObject.py
# It is used for learning classes and object in python

class Student:

    # Here, name, branch, gpa are parameters that will be entered while calling Student
    # __init__ is similar to constructor in javascript
    def __init__(self, name, branch, gpa):
        self.name = name
        self.gpa = gpa
        self.branch = branch
        # The parameters passed while creating object out of this class needs to be added to object
        # self is similar to this keyword in javascript
    # Class functions used in 22_classFunctions.py

    def isFirstClassStudent(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
