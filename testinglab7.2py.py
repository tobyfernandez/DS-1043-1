import shutil
def create_table(headers, data):
    if not data:
        raise ValueError("Data should contain values for columns")

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

headers1 = ["Name", "Age", "City", "Employed", "Name", "Age", "City", "Employed", "Name", "Age", "City", "Employed"]
rows1 = [
    ["Daisy", 30, "New York", True, "Daisy", 30, "New York", True, "Daisy", 30, "New York", True,],
    ["Dennis", 25, "Los Angeles", False, "Dennis", 25, "Los Angeles", False,"Dennis", 25, "Los Angeles", False],
    ["Drake", 35, "Chicago", True, "Drake", 35, "Chicago", True, "Drake", 35, "Chicago", True]
]

headers2 = ["Name", "Age", "City", "Employed"]
rows2 = [
    {"Name": "Daisy", "Age": 30, "City": "New York", "Employed": True},
    {"Name": "Dennis", "Age": 25, "City": "Los Angeles", "Employed": False},
    {"Name": "Drake", "Age": 35, "City": "Chicago", "Employed": True},
]

def view_table(headers, data, max_width=(shutil.get_terminal_size()).columns, file=None):
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

view_table(headers1, rows1)
