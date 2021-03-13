# Author David
# lab7.5.1.studentmange.py

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
def dosave(students):
    #youwill put the call to save dict here
    print("in save")


#the dict that maps a letter to function
choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing
}

#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice in choiceMap:
        #run function
        choiceMap[choice](students)
    else: #use did not enter something valid
        print("\n\nplease select either a,v or q")

    choice=displayMenu()    

