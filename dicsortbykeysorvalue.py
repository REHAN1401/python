key_value={}

key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323
 
print("Task 1:-\n")
 
print("key_value", key_value)
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
for i in sorted(key_value.keys()):
    print(i, end=" ")


from collections import OrderedDict
 
dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)