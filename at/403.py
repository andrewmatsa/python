import sys

def main():

    num = [int(arg) for arg in sys.argv[1:] if arg.isdigit()]
    num.sort()
    if len(num) == 0:
        print 'Please enter the numbers!'
        return
    print num
    print 'sum of two biggest number is: %d' %sum(num[-2:])

if __name__ == '__main__':
    main()

