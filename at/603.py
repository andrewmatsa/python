from csv2sql import soft_compare, pretty_print

def main():
    a = ("10000;201001;1586",
         "10000;800000;23",
         "10000;8000000 ;0")
	
    b = (" 10000; 201001  ;1588,1135",
         " 10000; 800000  ;23,0000",
         " 10000; 8000000 ;0,0001")
	
    pretty_print(a)
    pretty_print(b)

    print "\nIs two lists are identical? " + str(soft_compare(a,b))
	
if __name__ == '__main__':
    main()