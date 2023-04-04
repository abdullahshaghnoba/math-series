def fibonacci (n):
    
    # Check if input is less than 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0 then it will return 0
    elif n == 0:
        return 0
    # Check if n is 1 it will return 1
    elif n == 1 :
        return 1
    # the rest of the numbers goes under this case
    else:
        return fibonacci(n-1) + fibonacci(n-2)




def lucas (n):
    # Check if input is less than 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0 then it will return 2
    if n == 0:
        return 2
    # Check if n is 1 it will return 1
    if n == 1:
        return 1
   
    # the rest of the numbers goes under this case
    return lucas(n - 1) + lucas(n - 2)




def sum_series(n, first=0, second=1):
    # if not given first and second will go with default values for them (fibonacci)
    # if given first=2 and second=1 will go with (lucas)
    # if given other values for first and second will go with new series result
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)