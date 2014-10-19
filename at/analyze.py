def is_good_list(*args):
    new = filter(lambda x: x % 3 == 0, args)
    if len(new) == len(args):
        return True
    else:
        return False

def output_list(in_list):
    if is_good_list(*in_list):
        print in_list, "is good list"
    else:
        print in_list, "is bad list"