def soft_compare(list1, list2):
    '''
    comparing two lists
    '''
    list1 = _create_nested_list(list1)
    list2 = _create_nested_list(list2, ";")
    list1 = _fix_format(list1)
    list2 = _fix_format(list2)
    return list1 == list2

def _create_nested_list(list, delimeter=";"):
    """
    create nested list splitted by delimeter
	"""
    return [[j.strip() for j in i.split(delimeter)] for i in list]

def _fix_format(list):
    """
	fix format before comparing
	"""
    to_return = []
    for (x,c,v) in list:
        if "," in v:
            v = v[:v.find(",")]
        to_return.append([x,c,v])
    return to_return

def pretty_print(list):
    print "\nprinting data"
    for item in list:
        print item
