import testinglab7
from testinglab7 import pretty_print_lists

headers1 = ["Name", "Age", "City", "Employed"]
rows1 = [
    ["Daisy", 30, "New York", True],
    ["Dennis", 25, "Los Angeles", False],
    ["Drake", 35, "Chicago", True]
]

with open('testmarkdown.md', 'w') as f:
    # Write markdown content to the file
    f.write('# Markdown File\n')
    f.write('## This is a heading\n')
    f.write('* This is a bullet point\n')
    f.write('# Testing\n')

def add_stuff():
    with open('testmarkdown.md','a') as f:
        f.write(pretty_print_lists(headers1, rows1))

add_stuff()

