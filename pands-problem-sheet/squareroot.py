# squareroot.py
# Author David

# positive floating-point number as input and 
# outputs an approximation of its square root
# Function from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/


def squareRoot(val):
    # Assuming the sqrt of n as n only  
    x = val    
    # To count the number of iterations  
    count = 0   
    while (1) : 
        count += 1 
        # Calculate more closed x  
        root = 0.5 * (x + (val / x))  
        # Check for closeness  
        if (abs(root - x) < l) : 
            break 
        # Update root  
        x = root 
    # Test output
    # print(root)
    # Round to the nearest 2 decimal point.
    ans = round(root,1)
    print("The square root of {} is approx. {}. ".format(val, ans))
    return


# https://pynative.com/python-check-user-input-is-number-or-string/
# Create a function to test users input is a positive floating-point number

def check_user_input(input):
    try:
        # Convert it into integer 
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print(val)
            # Check that the float is positive
            if val <= 0:
                print("No negative floats allowed")
            # Go to newtons method function squareRoot()    
            else:
                squareRoot(val)
            # Test output            
            # print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a float. It's a string")


# main program
l = 0.00001
# number = 14.5
# Request user input
input1 = input("Please enter a positive floating-point number: ")

#This calls the function
check_user_input(input1)







