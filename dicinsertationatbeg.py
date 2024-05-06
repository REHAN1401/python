# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

# Output:  {'c':3, 'a':1, 'b':2}

from collections import OrderedDict

dic = OrderedDict([('akshat', '1'), ('nikhil', '2')])

dic.update({'rehan':'20'})

dic.move_to_end('rehan',last=False)
print(dic)