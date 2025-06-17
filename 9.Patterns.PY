# pattern questions
# *
# * *
# * * *
# * * * * 
# * * * * *

# def half_pyramid(n):
#     for i in range(0, n + 1):
#         for j in range(0, i):
#             print("*", end=" ")
#         print()

# def half_pyramid_number_pattern(n):
#     m = 1
#     for i in range(0, n+1):
#         for j in range(0, i):
#             print(m, end=" ")
#             m = m + 1
#         print()   

# def inverted_half_pyramid(n):
#     for i in range(0, n+1):
#         for j in range(0, n-i):
#             print("*", end=" ")
#         print()

# def full_pyramid(n):
#     for i in range(0, n + 1):
#         for j in range(0, n-i):
#             print(end=" ")

#         for k in range(0, i):
#             print("*", end=" ")
#         print()

def half_pyramid(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()
    print()

def half_pyramid_number_pattern(n):
    num = 1
    for i in range(1,n+1): 
        for j in range(i):
            print(num, end=" ")
        num += 1
        print()
    print()

# Explanation in metrics format above Two funtions
# *          ← row 1, i = 1 → j = 0
# * *        ← row 2, i = 2 → j = 0, 1
# * * *      ← row 3, i = 3 → j = 0, 1, 2
# * * * *    ← row 4, i = 4 → j = 0, 1, 2, 3

def inverted_half_pyramid(n):
    # num = 1
    for i in range(1, n+1):
        for j in range(n + 1 -i):
            print("*", end=" ")
            # print(num, end=" ")
            # num += 1
        print()
    print()

# Explanation in metrics format for inverted_half_pyramid
# * * * *          ← row 1, i = 1 → j = 0, 1, 2, 3
# * * *            ← row 2, i = 2 → j = 0, 1, 2,
# * *              ← row 3, i = 3 → j = 0, 1
# *                ← row 4, i = 4 → j = 0, 1, 2, 3

def full_pyramid(n):
    for i in range(1, n+1):
        for j in range(n+1 -i):
            print(" ", end=" ")

        for j in range(i):
            print("*", end=" ")

        for j in range(i-1):
            print("*", end=" ")

        print()

    print()

def palindromic_number_pyramid(n):
    for i in range(1, n+1):
        for j in range(n+1 -i):
            print(" ", end=" ")
       
        num2 = i
        for j in range(i):
            print(num2, end=" ")
            num2 = num2 - 1
        num = 2
        for j in range(i-1):
            print(num, end=" ")
            num += 1

        print()

    print()

def optmized_full_pyramid(n):
    for i in range(1, n + 1):                  
        for j in range(n - i):                 
            print(" ", end="")

        for k in range(i):
            print("*", end=" ")                

        print()  

# def diamond_star_pattern(n):
#     for i in range(1, n+1):
#         for j in range(n -i):
#             print(" ", end=" ")
        
#         for k in range()

#  Numver Pyramid
    #    1
    #   2 3
    #  4 5 6
    # 7 8 9 10
def number_pyramid(n):
    num = 1
    for i in range(1, n + 1):                  
        for j in range(n - i):                 
            print(" ", end="")

        for k in range(i):
            print(num, end=" ")     
            num += 1       
        print()    

    print()  



def Paraelogram(n):
    for i in range(1, n+1):
        for j in range(n+1 -i):
            print(" ", end=" ")

        for j in range(n):
            print("num", end=" ")
        
        print()

    print()


n = int(input("Enter the Number: "))
# half_pyramid(n)
# half_pyramid_number_pattern(n)
# inverted_half_pyramid(n)
# full_pyramid(n)
# palindromic_number_pyramid(n)
# optmized_full_pyramid(n)
# number_pyramid(n)
# Paraelogram(n)
