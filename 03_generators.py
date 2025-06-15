# 3. create a generator function that yields squares of numbers up to a given limit. 

def square(limit):
    for i in range(limit + 1):
        yield i ** 2

limit = int(input("Enter the limit: "))  
for sq in square(limit):
    print(sq)