# squareroot.py
# Author David

# positive floating-point number as input and 
# outputs an approximation of its square root


def squareRoot(number):
    # Assuming the sqrt of n as n only  
    x = number    
    # To count the number of iterations  
    count = 0   
    while (1) : 
        count += 1 
        # Calculate more closed x  
        root = 0.5 * (x + (number / x))  
        # Check for closeness  
        if (abs(root - x) < l) : 
            break 
        # Update root  
        x = root 
    print(root)
    ans = round(root,2)
    print(ans)
    return



# main program

l = 0.00001
number = float(input("Please enter a positive integer:"))

if number <= 0:
    print("No negativity or zeros allowed here")
elif number != 0:
    squareRoot(number)







