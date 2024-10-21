with open('testmarkdown.md', 'w') as f:
    # Write markdown content to the file
    f.write('# Markdown File\n')
    f.write('## This is a heading\n')
    f.write('* This is a bullet point\n')
    f.write('# Testing')

def add_line():
    with open('testmarkdown.md','a') as f:
        f.write('\n # ANOTHER LINE!')

add_line()
add_line()


def create_table(headers, rows):
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        table += "| " + " | ".join(row) + " |\n"
    return table





headers = ["Name", "Age", "City"]
rows = [
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open('anothertest.md', 'w') as w:
    w.write(create_table(headers, rows))
    w.write('# Is this working?')
