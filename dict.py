# Using dictionary comprehension make dictionary
# dic = {x: x**2 for x in [1,2,3,4]}
# print(dic)  


# Merging two dictionaries using update()
# dic1= {1:"rehan ", 2:"sayyed"}
# dic1.update({3:"heyy"})
# print("Dictionary 1 :",dic1)


# This method is used if we have two lists and we want to convert them into a dictionary with one being key and the other one as corresponding values.
# lst = [1,2,3,4]
# lst2 = ["rehan","suresh","ramesh"]
# ans = dict(zip(lst,lst2))
# print("Merged Dictionary :", ans)

# lst = [1,2,3,4]
# # lst2 = ["rehan","suresh","ramesh"]
# ans = dict(enumerate(lst))
# print("Merged Dictionary :", ans)


# Add values to dictionary Using the merge( | ) operator
# dic1= {1:"rehan ", 2:"sayyed"}
# dic2 = {2:"kya?", 3:"hain??"}
# dic3 = dic1 | dic2
# print("Merged Dictionary :", dic3)


#  Remove a Key from a Dictionary using the del
# dic = {1:"rehan",2:"sayyed"}
# del dic[1]
# print("After Removing key-value pair :",dic)



# Using OrderedDict.move_to_end()  
from collections import OrderedDict
lst = OrderedDict([("rehan","1"),("sayyed","2")])
lst.update({"ali":"3"})
lst.move_to_end("ali",last=False)
print("Before moving :",lst)