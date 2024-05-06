# The list printed sorting by age: 
# [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

# The list printed sorting by age and name: 
# [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]

# The list printed sorting by age in descending order: 
# [{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]

# done via itemgetter metod

from operator import itemgetter


list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print("sorting  by age")
print (sorted(list,key= itemgetter('age')))


print("sort by age and name")
print(sorted(list,key=itemgetter("age","name")))


print ("The list printed sorting by age in descending order: ")
print (sorted(list, key=itemgetter('age'), reverse=True))