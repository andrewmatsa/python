a = [1,2,"3",4,5]
def isstring(x):
    return isinstance(x, basestring)
b = filter(isstring, a)
print  b

