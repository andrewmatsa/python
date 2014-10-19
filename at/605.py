from convertors import time, money

def main():
    print money.convert("100 EUR")
    print time.convert(1000)

if __name__ == '__main__':
    main()