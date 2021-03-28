# lab10.6.employee.py
# Author David

class Employee:
    timesheets = []

    def __init__(self, first, last):
        self.first = first 
        self.last = last 

    def __str__(self):
            return self.first + ' ' +  self.last


if __name__ == '__main__':
    test = Employee('some', 'one')
    print (test)
    assert ( 'some one' == str(test))
