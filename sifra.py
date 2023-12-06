def count_letters(file):
    with open(file, 'r', encoding='utf-8') as soubor:
            text = soubor.read()
            text = text.lower()
    
    frequency = {}

    for letter in text:
            # Check if the character is a letter
            if letter in frequency:
                frequency[letter] += 1  # If the letter is already in the dictionary, increment its count
            else:
                frequency[letter] = 1
    return frequency

file_name = 'algoritmy\sifrovany_text.txt'
count_letters(file_name)