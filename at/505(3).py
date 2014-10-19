def func_list(list1, list2 = [1,2,3,4,5]):
    differ = tuple(x for x in list1 if x in list2)
    return differ

list1 = [99,2,11,4,5,2]
list2 = [2,4,8,9,11]
print func_list(list1)