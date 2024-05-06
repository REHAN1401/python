# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 
# Explanation : All the keys before all the values in list. 


dict = {'rehan':1, 'reh':2, 'reh3':3}

x = dict.values()
y = dict.keys()
print(list(y)+list(x))