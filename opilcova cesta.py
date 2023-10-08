import random

def opilec(vzdalenost, pocet_kroku):
    pozice = vzdalenost // 2
    domov = 0
    pub = vzdalenost

    for krok in range (pocet_kroku):
        krok = [-1, 1] #krok doleva (-1) krok doprava (+1)
        krok_opilce = random.choice(krok)
        pozice += krok_opilce

        print("home", "." * pozice + "*" + "." * (vzdalenost - pozice), "pub")

        if pozice == domov:
            print("Ended up at home!")
        elif pozice == pub:
            print("Ended up in the pub again!")
        
    else:
        print("Simulace skončila po vyčerpání kroků")
        if pozice < vzdalenost // 2:
            print("Ended up at home!")
        else:
            print("Ended up in the pub again!")

opilec(12, 10)