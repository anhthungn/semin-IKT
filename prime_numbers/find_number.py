def find_number(prvek):
    pole = [1, 2, 3, 4, 5]
    for i in pole:
        if i == prvek:
            return True
    
    return False

prvek = int(input('Zadej prvek '))

if find_number(prvek):
    print(prvek, 'je v poli')
else:
    print(prvek, 'není v poli')
