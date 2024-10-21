def create_table(headers, rows):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        table += "| " + " | ".join(row) + " |\n"
    return table





headers1 = ["Name", "Age", "City", "Occupation"]
rows1 = [
    ["Alice", "30", "New York", "Accountant"],
    ["Bob", "25", "Los Angeles", "Cashier"],
    ["Charlie", "35", "Chicago", "Software Engineer"]
]

headers2 = ["Name", "Age"]
rows2 = {'Alice': 30, 'Bob': 25, 'Charlie': 35}


with open('anothertest.md', 'w') as f:
    f.write(create_table(headers1, rows1))
    f.write('# Is this working?')
