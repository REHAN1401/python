n = int(input("enter number:"))
r = 0 
sum = 0
tmp = n

while (n>0):
    r =n%10
    sum =sum+r*r*r
    n =n//10

if tmp == sum:
    print("its an armstrong number")

else:
    print("not an armstrong number")
