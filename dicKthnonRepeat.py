# Input : str = geeksforgeeks, k = 3
# Output : r
# First non-repeating character is f,
# second is o and third is r.

# Input : str = geeksforgeeks, k = 2
# Output : o

# Input : str = geeksforgeeks, k = 4
# Output : Less than k non-repeating
#          characters in input

from collections import OrderedDict


def fun(inp,n):
    dict = OrderedDict.fromkeys(inp,0)
    for ch in dict:
        dict[ch]+=1

    nonRep = [key for (key,value) in dict.items()if value == 1]

    if len(nonRep)< n:
        return "Less than k non-repeating characters in input"
    else:
        return nonRep[n-1]

x = 'rehan sayyed ali'
n = int(input("enter Nth term: "))

print(fun(x,n))