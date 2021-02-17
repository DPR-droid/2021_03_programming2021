# Author David
# lab.5.1.randomNumberList.py
# The program that puts 10 random numbers into aqueue(list), 
# The program should then output all the values in the queue, 
# Then take the numbers from the queue one at a time, 
# Print it and the current numbers still in the queue. 
# (the command pop(0) takes the first element out of a list


import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print("current Number is {} and the queue is {} ".format(currentNumber, queue))

print("the queue is now empty")