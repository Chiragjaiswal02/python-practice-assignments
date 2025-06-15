# 2. Implement a simple iterator that iterates over a list of numbers.

numbers = iter([1,2,3,4,5,6,7,8,9])

while True:
    try:
        nex = next(numbers)
        print(nex)
    except:
        break