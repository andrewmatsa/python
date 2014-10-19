ans = raw_input('Would you like to calculate your procent:')
while ans.lower == "no":
    summa = "asd"
    while not summa.isdigit():
        summa = raw_input('which summa do you need kredit:')

    procent = "asd"
    while not procent.isdigit():
        procent = raw_input('Your credit is:')

    z = float(summa) * float(procent) / 100.0
    print z
    ans = raw_input('Would you like to calculate your procent:')