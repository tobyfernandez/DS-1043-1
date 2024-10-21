def create_table(headers, rows):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    def format_row(row):
        return "| " + " | ".join(str(item).ljust(width) for item, width in zip(row, col_widths)) + " |"

    # Build the table
    table = format_row(headers) + "\n"
    table += "| " + " | ".join("-" * width for width in col_widths) + " |\n"
    for row in rows:
        table += format_row(row) + "\n"

    return table





headers1 = ["Name", "Age", "City", "Occupation"] #Switch out occupation for Employed boolean
rows1 = [
    ["Alice", "30" , "New York", "Accountant"],
    ["Bob", "25", "Los Angeles", "Cashier"],
    ["Charlie", "35", "Chicago", "Software Engineer"]
]

headers2 = ["Name", "Age"]
rows2 = [
    {"Name": "Alice", "Age": "30", "City": "New York", "Occupation": "Accountant"},
    {"Name": "Bob", "Age": "25", "City": "Los Angeles", "Occupation": "Cashier"},
    {"Name": "Charlie", "Age": "35", "City": "Chicago", "Occupation": "Software Engineer"},
]


with open('anothertest.md', 'w') as f:
    f.write(create_table(headers1, rows1))
    f.write('# Is this working?')

for i in rows2:
    print(i)