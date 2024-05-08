# List Comprehension in Python Example
# x = [1,2,3,4,5]
# sqr = [y**2 for y in x]
# print(sqr)


# Iteration with List Comprehension
# lst = [chr for chr in [1,2,3]]
# print(lst)

#  In this example, we are printing the even numbers from 0 to 10 using List Comprehension.
#  lst=[1,2,3,4,5,6,7,8,9,10]
#  eve = [x for x in lst if(x%2==0)]
#  print(eve)


# list comprehnsion over for loop
# lst = [chr for chr in "Geek for Geeks"]
# print("List of characters:", lst)


# nested list comprehension

# via for loop
# mat = []
# for i in range(5):
#     mat.append([])
#     for j in range(5):
#         mat[i].append(j)
# print(mat)

# via list comp

# mat = [[j for j in range(5)]for i in range(4)]
# print("Nested list of integers:",mat)

# n = 6
# tab = [x*10 for x in range(1,n)]
# print("Tabulation character: ", tab)


# using lamda
# lst = list(map(lambda x:x*10,[i for i in range(1,11)]))
# print("Lambda expression result: ", lst)


# Python List Comprehension using If-else.
# LST = ["EVEN NUMBER" if i%2==0
#        else "odd number" for i in range(10)]
# print("Resultant List: ", LST)


# In this example, we are inserting numbers in the list which is a multiple of 10 to 100, and printing it.
# lst = [num for num in range(100) if num%5==0 and num%10==0]
# print("Multiple conditions: ", lst)


# In this example, we are inserting a square from 1 to 10 to list and printing the list.
# lst = [n**2 for n in range(11)]
# print("Square numbers between 1 & 10",lst)


# In this example, we are reversing strings in for loop and inserting them into the list, and printing the list.
# lst = ["hii my name is rehhh"]
# x = [x[::-1]for x in lst]
# print(x)


# Creating a list of Tuples from two separate Lists

# lst1= [ "hi", "rehan"]
# lst2 = [1,2]
# x = [(x,y)for x,y in zip(lst1,lst2)]
# print(x)


# Display the sum of digits of all the odd elements in a list.

# lst = [111,123,222,444]
# tt = 0
# lst2=[]
# for i in lst:
#     if i%2!=0:
#         tt = sum(int(x)for x in str(i))
#         lst2.append(tt)
# print("Sum of Odd Numbers: ",lst2)


#  filtering odd squares divisible by 5 
# import functools

# ans  = filter(lambda x:x%5==0,
# [x**2 for x in range(1,11)if x%2!=0])
# print(list(ans))



# Reversing a sublist using Slicing

# lst = [1,2,3,"hi","by"]
# lst = lst[1:5][::-2]
# print(list(lst))


# check for palindrom
# lst = [1,2,2,1]
# lst2 = lst.copy()
# lst2.reverse() 
# if lst2 == lst:
#     print("Yes")
# else:
#     print("No")


#  Filtering a Nested List Using List Comprehension
# mat=[[2,3,4], [5,6,7], [8,9,10]]
# ans = [ele for row in mat for ele in row if ele%2!=0]
# print(ans)


#check nested list using any()isinstance()
# lst = [1,2,1234]
# print("og list:",lst)
# lst2 = any(isinstance(sub, list)for sub in lst)
# print(lst2)


# Copy a Nested List Using Iteration
# lst = [[1],[2,3],[45,5]]
# lst2=[]
# for x in range(len(lst)):
#     tmp = []
#     for j in lst[x]:
#         tmp.append(j)
#     lst2.append(tmp)
# print(lst2)


# import copy
# lst = [[1],[2,3],[45,5]]
# lst2 = copy.deepcopy(lst)
# print("original list: ",lst2)


# import json

# lst = [[1],[2,3],[45,5]]
# jlst = json.dumps(lst)
# ans = json.loads(jlst)
# print(ans)



# Convert Python List into Nested List Using map(), split() and lambda

# lst = ["rehan","sayyed","heyy","wassup"]
# ans = list(map(lambda x: x.split(" , "), lst))
# print(list(ans))


# Python Split Nested List into Two Lists Using List Comprehension
# lst = [["rehan","don"],["sayyed","don"],["heyy","by"],["wassup","wassdown"]]
# ans1 = [i[1] for i in lst]
# ans2 = [i[0]for i in lst]
# print(ans1)
# print(ans2)


#  zip using list comprehension We can find sum of each column of the given nested list using zip function of python enclosing it within list comprehension. 
# lst = [[1,2,3,4],[4,5,6,6]]
# ans = [sum(i)for i in zip(*lst)]
# print(ans)  



# 1. Using List Comprehension to Flatten a List of Lists
# mat = [["rehan"],[1],["sayyed"],[2]]
# ans = sum(mat, [])
# print(ans)


# usinf flatten
# mat = [["rehan"],[1],["sayyed"],[2]]
# from pandas.core.common import flatten
# mat = [["rehan"],[1],["sayyed"],[2]]
# print(list(flatten(mat)))



# Sort Flatten list of list
# mat = [[3, 5], [7, 3, 9], [1, 12]]
# x = [ele for i in mat for ele in i]
# print(sorted(x))

