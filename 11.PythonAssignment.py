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

# 2. Implement a simple iterator that iterates over a list of numbers.
numbers = iter([1,2,3,4,5,6,7,8,9])

while True:
    try:
        nex = next(numbers)
        print(nex)
    except:
        break

# 3. create a generator function that yields squares of numbers up to a given limit. 
def square(limit):
    for i in range(limit + 1):
        yield i ** 2

limit = int(input("Enter the limit: "))  
for sq in square(limit):
    print(sq)

# 4. Create a closure function that generates a series of numbers starting from a given base.

def number_series(base):
    def generator():
        nonlocal base
        base += 1
        return base
    return generator

gen = number_series(999)
for i in range(1,11):
    print(gen())  

