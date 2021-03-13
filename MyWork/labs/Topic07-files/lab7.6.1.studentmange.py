# Author David
# lab7.6.1.studentmange.py

import json
filename = "testdict.json"

students = []

def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)


def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (s) Save students")
    print("\t (l) Load students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/s/l/q):").strip()
    return choice

def doAdd(students):
    print("in adding")
def doView(students):
    print("in viewing")
def doSave(students):
    writeDict(students)
    print("Students saved")
def doLoad(students):
    writeDict(students)
    print(students)

#main program

choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda function
    # I am keeping this for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)  
    elif choice == 'l':
        doLoad(students)  
    elif choice != 'q':
        print("\n\nplease select either a,v,s,l or q")
    choice=displayMenu()    

