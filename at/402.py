import sys, os

def main():
    usage = """
    You should pass at least 1 argument to %s
    Arguments are folders full path separed by space.
    """ % sys.argv[0]
    argv = sys.argv[1:]
    #if not arguments passed
    if not argv:
    #do some code
        print usage
        return

    output = []
    for option in argv:
        exist = "folder exist"
        #do some code here to check string is path
        if not os.path.exists(option):
            exist = "folder doesn't exist"
        elif os.path.isfile(option):
            exist = "it's file"
        output.append([option, exist])

    for i, folder_info in enumerate(output):
        print "%r.\t%s\t[%s]" % (i + 1, folder_info[0], folder_info[1])

if __name__ == '__main__':
    main()