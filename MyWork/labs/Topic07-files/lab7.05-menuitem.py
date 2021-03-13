# Author David
# lab7.5.1.studentmange.py

students = []

def displayMenu():
    print("What would you like to do?")
    print("\t (a) Add new student")
    print("\t (v) View students")
    print("\t (s) Save students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/s/q):").strip()
    return choice

def doAdd(students):
    print("in adding")
def doView(students):
    print("in viewing")
def doSave(students):
    #you will put the call to save dict here
    print("in save")

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
    elif choice != 'q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()    

