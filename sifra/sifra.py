def character_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            
            char_frequency = {} #Create a dictionary of every letter, with a count of 0
            
            for char in text:
                if char.isalpha():  # Check if it's a letter
                    if char in char_frequency:
                        char_frequency[char] += 1  # Increment character count
                    else:
                        char_frequency[char] = 1  # Initialize count for new character
            
            # Sort characters by frequency (descending order)
            sorted_chars = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)
            
            # Extract sorted characters into a list
            sorted_char_list = [char for char, _ in sorted_chars]
            
            return sorted_char_list 
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to decrypt text using a substitution dictionary
def decrypt_with_dictionary(file_path, substitution_dict):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            encrypted_text = file.read()

            # Decrypt the text using the substitution dictionary
            decrypted_text = ''.join(substitution_dict.get(char, char) for char in encrypted_text)

            return decrypted_text
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save text to a file
def save_to_file(text, output_file_path):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
        print(f"Decrypted text saved to '{output_file_path}'.")
        return True
    
    except Exception as e:
        print(f"An error occurred while saving to file '{output_file_path}': {e}")
        return False

result_dict = {'p': 'e', 'y': 't', 'q': 'a', 'b': 'o', 'c': 'i', 'k': 'h', 'l': 'n', 't': 's', 'a': 'r', 'm': 'd', 'n': 'l', 'f': 'u', 'v': 'w', 'i': 'g','x': 'c', 'j': 'y', 'o': 'm', 'r': 'f', 'e': 'p', 'z': 'b', 'w': 'k', 'g': 'v', 'd': 'q', 'h': 'q', 'u': 'j', 's': 'z'}

encrypted_file_path = 'úkoly - py\sifra\sifrovany_text.txt'
output_file_path = 'decrypted_text.txt'

# Calculate character frequencies and create substitution dictionary
sorted_chars = character_frequency(encrypted_file_path)

# If character frequency analysis successful, decrypt and save the text
if sorted_chars is not None:
    # Create dictionary from encrypted characters and substitutions
    result_dict = dict(zip(sorted_chars, result_dict.values()))

    # Decrypt text and save to a file
    decrypted_text = decrypt_with_dictionary(encrypted_file_path, result_dict)
    save_to_file(decrypted_text, output_file_path)
else:
    print("Character frequency analysis failed.")
