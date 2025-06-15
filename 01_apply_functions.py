# 1. Write a function that takes two functions and a value as arguments. 
# The function should apply the two functions to the value and return a tuple with the results. 
def square(num):
    return num**2

def cube(num):
    return num**3

def Result_func(square, cube, value):
    result = (square(value), cube(value))
    return result

print(Result_func(square, cube, 2))   