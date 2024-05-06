# {'gfg': [5, 6, 7, 8],
#              'is': [10, 11, 7, 5],
#              'best': [6, 12, 10, 8],
#              'for': [1, 2, 5]}

# [1, 2, 5, 6, 7, 8, 10, 11, 12]

def finuni(dic):
    uni = list(sorted({ele for val in dic.values()for ele in val}))
    return uni 



dic = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
# print(finuni(dic))


dic = {'gfg' : [5, 6, 7, 8],
            'is' : [10, 11, 7, 5],
            'best' : [6, 12, 10, 8],
            'for' : [1, 2, 5]}
x= list(dic.values())
y = []
res= []
for i in x:
    y.extend(i)
for i in y:
    if i not in res:
        res.append(i)
res.sort()
print(res)


