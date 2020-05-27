def GeldOrdnen(cents):
    taler = [200,100,50,20,10,5,2,1]
    ergebnis = [0,0,0,0,0,0,0,0]
    i = 0
    for coin in taler:
        if cents != 0:
            ergebnis[i] = cents//coin
            i += 1
            cents = cents%coin
        else:
            return ergebnis

def Test(cents, ergebnis):
    if GeldOrdnen(cents) == ergebnis:
        print(f"{cents} cents sind {ergebnis}")
    else:
        print(f"{cents} cents war das falsche Ergebnis")
        

Test(100, [0,1,0,0,0,0,0,0])
Test(387, [1,1,1,1,1,1,1,0])
Test(200, [1,0,0,0,0,0,0,0])
Test(0, [0,0,0,0,0,0,0,0])
Test(9, [0,0,0,0,0,1,2,0])