import shutil
import string

def create_table(headers, data):
    """Creates a list of strings that make up a table of values and their corresponding headers
    where data is either a list of lists or a list of dictionaries"""
    if all(isinstance(row, list) for row in data):
        data_type = 'list'
    elif all(isinstance(row, dict) for row in data):
        data_type = 'dict'
    else:
        raise ValueError("Data must be list of lists or list of dicts")

    col_info = {header: {'max_width': len(header), 'align': 'left'} for header in headers}

    if data_type == 'list':
        for row in data:
            for i, value in enumerate(row):
                str_value = str(value) if value is not None else "" # For determining length
                if isinstance(value, str):
                    col_info[headers[i]]['align'] = 'left'
                elif isinstance(value, int) and not isinstance(value, bool): # Necessary since bool is subtype of int
                    col_info[headers[i]]['align'] = 'right'
                elif isinstance(value, float):
                    col_info[headers[i]]['align'] = 'right'
                    str_value = f"{value:.2f}"
                elif isinstance(value, bool):
                    col_info[headers[i]]['align'] = 'center'
                col_info[headers[i]]['max_width'] = max(col_info[headers[i]]['max_width'], len(str_value))
    elif data_type == 'dict':
        for row in data:
            for key, value in row.items():
                str_value = str(value) if value is not None else "" # For determining length
                if isinstance(value, str):
                    col_info[key]['align'] = 'left'
                elif isinstance(value, int) and not isinstance(value, bool): # Necessary since bool is subtype of int
                    col_info[key]['align'] = 'right'
                elif isinstance(value, float):
                    col_info[key]['align'] = 'right'
                    str_value = f"{value:.2f}"
                elif isinstance(value, bool):
                    col_info[key]['align'] = 'center'
                col_info[key]['max_width'] = max(col_info[key]['max_width'], len(str_value))

    table_list = []

    header_str = '| ' + ' | '.join(
        f"{header.center(col_info[header]['max_width']) if col_info[header]['align'] == 'center' \
        else header.rjust(col_info[header]['max_width']) if col_info[header]['align'] == 'right' \
        else header.ljust(col_info[header]['max_width'])}"
        for header in headers) + ' |'
    separator_str = '| ' + ' | '.join(f"{'-' * col_info[header]['max_width']}" for header in headers) + ' |'

    table_list.append(header_str)
    table_list.append(separator_str)

    if data_type == 'list':
        for row in data:
            row_str = '| ' + ' | '.join(
                f"{str(value).center(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'center' \
                else str(value).rjust(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'right' \
                else str(value).ljust(col_info[headers[i]]['max_width'])}"
                for i, value in enumerate(row)) + ' |'
            table_list.append(row_str)
    elif data_type == 'dict':
        for row in data:
            row_str = '| ' + ' | '.join(
                f"{str(row.get(header, '')).center(col_info[header]['max_width']) if col_info[header]['align'] == 'center' \
                else str(row.get(header, '')).rjust(col_info[header]['max_width']) if col_info[header]['align'] == 'right' \
                else str(row.get(header, '')).ljust(col_info[header]['max_width'])}"
                for header in headers) + ' |'
            table_list.append(row_str)

    return '\n'.join(table_list)

def view_table(headers, data, max_width=(shutil.get_terminal_size()).columns, file=None):
    """Calls the create_table function and prints the resulting table to the screen, using ellipses if necessary to
    indicate that the table is too large to display in its entirety"""
    table = create_table(headers, data)
    lines = table.split('\n')
    display = []

    for line in lines:
        if len(line) > max_width:
            display.append(line[:max_width - 1] + '…')
        else:
            display.append(line)

    output = '\n'.join(display)
    print(output)

def zipper_merge(*lists):
    """Takes any number of lists containing integers and combines them into one sorted list of integers"""
    indices = [0] * len(lists) # Initializes a list of indices (one for each list of ints) starting at 0
    merged_list = []
    while True:
        numbers = [] # A temporary list to hold the next set of integers to compare
        for index, l in enumerate(lists):
            if indices[index] < len(l): # Checks to make sure we do not get IndexError
                numbers.append((l[indices[index]], index))
        if not numbers: break # Stops the loop when every integer has been compared and added to merged_list

        min_integer, min_index = min(numbers) # Finds the smallest integer in numbers along with its index
        merged_list.append(min_integer)
        indices[min_index] += 1 # Allows for the next number in the list to be checked during next loop
    return merged_list

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


