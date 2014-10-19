list = [5,3,9,7,1]
for y in list:
    for x in range(len(list) - 1):
        if (list[x] > list[x + 1]):
            list[x], list[x + 1] = list[x + 1], list[x]
print list
