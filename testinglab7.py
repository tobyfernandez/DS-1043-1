


def create_table(headers, data):
    if isinstance(headers, dict):
        headers = [value for key, value in headers.items() if value in headers]
    if not all(len(row) == len(headers) for row in data):
        raise ValueError("All rows must contain values from each header")

    col_info = {header: {'max_width': len(header), 'align': 'left'} for header in headers}

    for row in data:
        for i, rv in enumerate(row): # rv stands for row value
            str_value = str(rv) if rv is not None else ""
            if isinstance(rv, str):
                col_info[headers[i]]['align'] = 'left'
            elif isinstance(rv, int) and not isinstance(rv, bool): # Necessary since bools are subtype of int
                col_info[headers[i]]['align'] = 'right'
            elif isinstance(rv, float):
                col_info[headers[i]]['align'] = 'right'
                str_value = f"{rv:.2f}"
            elif isinstance(rv, bool):
                col_info[headers[i]]['align'] = 'center'
            col_info[headers[i]]['max_width'] = max(col_info[headers[i]]['max_width'], len(str_value))

    table_list = []

    header_str = '| ' + ' | '.join(f"{header:{col_info[header]['max_width']}}" for header in headers) + ' |'
    separator_str = '| ' + ' | '.join(f"{'-' * col_info[header]['max_width']}" for header in headers) + ' |'

    table_list.append(header_str)
    table_list.append(separator_str)

    for row in data:
        row_str = '| ' + ' | '.join(
            f"{str(rv).center(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'center' \
            else str(rv).rjust(col_info[headers[i]]['max_width']) if col_info[headers[i]]['align'] == 'right' \
            else str(rv).ljust(col_info[headers[i]]['max_width'])}"
            for i, rv in enumerate(row)) + ' |'
        table_list.append(row_str)

    return '\n'.join(table_list)

headers1 = ["Name", "Age", "City", "Employed"]
rows1 = [
    ["Daisy", 30, "New York", True],
    ["Dennis", 25, "Los Angeles", False],
    ["Drake", 35, "Chicago", True]
]

headers2 = ["Name", "Age", "City", "Employed"]
rows2 = [
    {"Name": "Daisy", "Age": 30, "City": "New York", "Employed": True},
    {"Name": "Dennis", "Age": 25, "City": "Los Angeles", "Employed": False},
    {"Name": "Drake", "Age": 35, "City": "Chicago", "Employed": True},
]

print(create_table(headers1, rows1 ))