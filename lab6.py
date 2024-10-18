import json
import math
import statistics
import markdown

with open('my_markdown.md', 'w') as f:
    # Write markdown content to the file
    f.write('# My Markdown File\n')
    f.write('## This is a heading\n')
    f.write('* This is a bullet point\n')

#with open('my_markdown', 'r') as textfile:
    #entire_contents: str = textfile.read()

f = open('datasets/counties.json')

data = json.load(f)


def find_stable_temp():
    index = 0
    variance = []
    state_dict = {}
    county_dict = {}
    point_dict = {}
    while index < len(data):
        temperatures = []
        for point in data[index]['noaa']:
            if point in ('temp-jan', 'temp-apr', 'temp-jul', 'temp-oct'):
                temperatures.append(data[index]['noaa'][point])
        county_dict[statistics.variance(temperatures)] = data[index]['name']
        state_dict[statistics.variance(temperatures)] = data[index]['state']
        variance.append(statistics.variance(temperatures))
        index += 1
    variance.sort()
    print(variance[0])
    lowest = variance[0]
    print(state_dict[lowest])
    print(county_dict[lowest])
    print(variance[-1])
    highest = variance[-1]
    print(state_dict[highest])
    print(county_dict[highest])

find_stable_temp()

def fastest_growth():
    index = 0
    fastest = 0
    state = ''
    county = ''
    while index < len(data):
        for i in data[index]['population']:
            earlier = data[index]['population']['2010']
            later = data[index]['population']['2019']
            speed = (later - earlier) / earlier * 100
            if speed > fastest:
                fastest = speed
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(fastest)
    print(state)
    print(county)
fastest_growth()
'''

with open('example.md', 'w') as mdfile:
    mdfile.write('# Lab 6: Data Scavenger Hunt\n')
    '''
