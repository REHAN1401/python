# n = int(input("enter number : "))

# def fact(n):
#     return 1 if (n==1 or n==0) else n*fact(n-1)

# num =5
# print("factorial of" , num,"is",fact(n)) 


import math 

def fact(n):
    return math.factorial(n)

n = int(input("enter number:"))
print("factorial is: ",fact(n))