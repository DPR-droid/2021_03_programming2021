########################################################################
### plottask.py
### This displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
### in the range (0, 4) on the one set of axes.
### Author David
### https://numpy.org/doc/stable/reference/generated/numpy.power.html
########################################################################

########################################################################
### import modules and renaming using the as function
########################################################################
import numpy as np
import matplotlib.pyplot as plt

########################################################################
### creating range using lab8.5.plot.py as reference.
########################################################################
xaxis = np.array([0,1,2,3,4])

########################################################################
### https://www.w3resource.com/graphics/matplotlib/basic/matplotlib-basic-exercise-5.php
########################################################################
### line 1 points
f = np.power(xaxis, 1)
### Testing print cubed range
print(f)
### plotting the line 1 points 
plt.plot(xaxis, f, label = "f(x)=x")
########################################################################

########################################################################
### line 2 points
g = np.power(xaxis, 2)
### Testing print squared range
print(g)
### plotting the line 2 points 
plt.plot(xaxis, g, label = "g(x)=x2")
########################################################################

########################################################################
### line 3 points
h = np.power(xaxis, 3)
### Testing print cubed range
print(h)
### plotting the line 3 points 
plt.plot(xaxis, h, label = "h(x)=x3")
########################################################################

#######################################################################
### Settings for plot
### Set the y axis label of the current axis.
plt.xlabel('x - axis')
### Set the y axis label of the current axis.
plt.ylabel('y - axis')
### Set a title of the current axes.
plt.title('Displays Plot for f(x)=x, g(x)=x2 and h(x)=x3')
### show a legend on the plot
plt.legend()
### Display a figure.
plt.show()

#######################################################################

