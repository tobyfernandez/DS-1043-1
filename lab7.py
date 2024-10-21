import shutil
import string




def create_table(headers, data):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for data in data:
        # Add conditional for dictionary?
        table += "| " + " | ".join(data) + " |\n"
    return table


def view_table(header, data, max_width=(shutil.get_terminal_size()).columns, file=None):
    pass

def zipper_merge(*lists):
    indices = [0] * len(lists)
    merged = []
    while True:
        numbers = []
        for index, integers in enumerate(lists):
            if indices[index] < len(integers):
                numbers.append((integers[indices[index]], index))
        if not numbers: break

        min_integer, min_index = min(numbers)
        merged.append(min_integer)
        indices[min_index] += 1
    return merged

print(zipper_merge([1, 4, 9], [2, 5, 7], [10, 10, 10]))



def caesar_cipher(plaintext: str, rotation: int = 13) -> str:
    """Takes the plaintext and encrypts it by rotating the standard Latin alphabet by the specified amount.
    Returns the resulting encrypted string."""
    alphabet = string.ascii_lowercase # Standard lowercase alphabet
    upper = string.ascii_uppercase # Standard uppercase alphabet
    cipherbet = alphabet[rotation:] + alphabet[:rotation] # The shifted alphabet
    cipherbet_upper = upper[rotation:] + upper[:rotation] # An uppercase version of the shifted alphabet
    encryption = ''
    for character in plaintext:
        if character in alphabet or character in upper:
            if character.islower(): # Looks for lowercase letters to encrypt
                index = alphabet.index(character)
                encryption = encryption + cipherbet[index]
            else: # Looks for uppercase letters to encrypt
                index = upper.index(character)
                encryption = encryption + cipherbet_upper[index]
        else: # Preserves all non-letter characters
            encryption = encryption + character
    return encryption

print(caesar_cipher('I decided that I absolutely LOVE waffles?!',22))