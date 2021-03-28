# lab10.5.employee.py
# Author David

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first 
        self.last = last 

    def __str__(self):
            return self.first + ' ' +  self.last
