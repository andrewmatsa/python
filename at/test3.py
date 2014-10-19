a = {"a":[1,2,3,4], "b":[5,6,7,8]}
new_dict = {}
for key in a:
    new_list = []
    for i in a[key]:
        new_list.append(i*2)
    new_dict[key+"-changed"] = new_list

print a
print new_dict