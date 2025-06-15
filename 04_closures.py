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