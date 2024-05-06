# The list printed sorting by age: 
# [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

# The list printed sorting by age and name: 
# [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]

# The list printed sorting by age in descending order: 
# [{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]

# done via lamda method


# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print("sort by age")
print(sorted(list,key= lambda i :i['age']))

print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))


print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: (i['age'], i['name']),reverse=True))