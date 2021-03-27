# myFunctions.py
# Author David

# Turn off logging 
# import logging
# logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number < 0:
        raise ValueError('number must be > 0')
    if number == 0:
        return []
    a = 0
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already do number - 1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a, b = b, a + b
    # logging.debug("%d: %s", number, fibonacciSequence)
    
    return fibonacciSequence




if __name__ == '__main__':
    # test will go here
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 7'
    assert fibonacci(0) == [], 'incorrect return for 7'
    assert fibonacci(1) == [0], 'incorrect return for 7'

    try:
        fibonacci(-1)
    except ValueError:
        # we want this exception to be thrown
        # so this is an example where we want to do nothing
        pass
    else:
        # if the exception was not trown we should throw
        # assertion error
        assert False, 'fibonaccci missing ValueError'
        # or 
        # raise AssertionError("fibonacci no ValueError") 
    print("all good")
