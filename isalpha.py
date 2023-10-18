def analyza():
    with open('alice_in_wonderland.txt', 'r', encoding='utf-8') as soubor:
        text = soubor.read()

        slovnik = {}
        for pismeno in text:
            if text.isalpha():
                if pismeno in text:
                    slovnik[pismeno] +=1
                else:
                    slovnik[pismeno] =1

analyza()