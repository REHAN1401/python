# Input: dict1 = {'a': 10, 'b': 8}
#            dict2 = {'d': 6, 'c': 4}
# Output: {'a': 10, 'b': 8, 'd': 6, 'c': 4}

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
for i in dict2.keys():
    dict1[i]=dict2[i]
print(dict1)

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
res = dict1 | dict2
print(res)