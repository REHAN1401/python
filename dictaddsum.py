# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

dic = {'a':10, 'b':10, 'c':10}

lst= []
for i in dic:
    lst.append(dic[i])
print(sum(lst))