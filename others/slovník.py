def words(n):
    with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as soubor:
        lines = soubor.readlines()
    
    x = lines.split()
    print(x)

    for i in range(x):
        print(i)

words(5)