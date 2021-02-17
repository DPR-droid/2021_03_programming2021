# Author David
# Quiz.py


numberOfQuestions = 5
averageAge = 23.5
debugMode = True
name = "joe"
age = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [12, 'Fred', False, {}]
someone = dict(firstname = 'joe')
me = {
    "firstName" : "Andrew",
    "teaching"  : [{
        "courseName" : "programming",
        "semester"   : 1
    },{
      "courseName" : "Data Representation",
      "semester"   : 2  
    }
    ]
}

print("Variable type of a.", type(numberOfQuestions))
print("Variable type of b.", type(averageAge))
print("Variable type of c.", type(debugMode))
print("Variable type of d.", type(name))
print("Variable type of e.", type(age))
print("Variable type of f.", type(months))
print("Variable type of g.", type(months[1]))
print("Variable type of h.", type(book))
print("Variable type of i.", type(stuff))
print("Variable type of j.", type(stuff))
print("Variable type of k.", type(someone))
print("Variable type of l.", type(someone["firstname"]))
print("Variable type of m.", type(me))
print("Variable type of n.", type(me["teaching"]))
print("Variable type of o.", type(me["teaching"][0]["semester"]))
print("Variable type of p.", type(me["teaching"][0]["coursename"]))
