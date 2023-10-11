import random

seznam = [0]*11

pocet_hodu = 10000
for _ in range(pocet_hodu):
    kostka1 = random.randint(1, 6)
    kostka2 = random.randint(1, 6)
    soucet = kostka1 + kostka2
    seznam[soucet - 2] += 1

print(seznam)
