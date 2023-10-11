def head(n):
    with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as soubor:
        lines = soubor.readlines()
        
        for i in range(n):
            print(lines[i])

head(10)

def tail(n):
    with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as soubor:
        lines = soubor.readlines()
        
        length = len(lines)
        print(lines)

        for i in range(n):
            print(lines[length +-1 - i])

tail(5)