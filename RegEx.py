# import re
# lst = "rehan is my name okay?"
# x = re.search("rehan",lst)
# print('start index:',x.start())
# print('end index :', x.end())


# In this code, you’re using regular expressions to find all the characters in the string that fall within the range of ‘a’ to ‘m’. The re.findall() function returns a list of all such characters. In the given string, the characters that match this pattern are: ‘c’, ‘k’, ‘b’, ‘f’, ‘j’, ‘e’, ‘h’, ‘l’, ‘d’, ‘g’.
# import re
# str = "rehann bol na?"
# patt = "[a-r]"
# x = re.findall(patt,str)
# print(x)



# 3. ^ – Caret
# Caret (^) symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. For example –  

# ^g will check if the string starts with g such as geeks, globe, girl, g, etc.
# ^ge will check if the string starts with ge such as geeks, geeksforgeeks, etc.
# import re
# str = ["rehan hai name"]
# fin = r'^rehan'
# for x in str:
#     if re.match(fin, x):
#         print(f"matched:{str}")
#     else:
#         print(f"not matched:{str}")



# $ – Dollar
# Dollar($) symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not. For example-

# s$ will check for the string that ends with a such as geeks, ends, s, etc.
# ks$ will check for the string that ends with ks such as geeks, geeksforgeeks, ks, etc.
import re
str= "rehan is who"
patt = r"who$"
match = re.search(patt,str)
if match:
    print("Match found")
else:
    print("No Match Found")