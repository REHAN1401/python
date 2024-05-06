# Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]} 
# Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]} 

testdict= {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}


print("The original dictionary is : " , testdict)
res= dict()
for i in testdict:
    res[i] = sorted(testdict[i])

print(res)