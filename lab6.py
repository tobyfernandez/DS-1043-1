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

def slowest_growth():
    index = 0
    slowest = 0
    state = ''
    county = ''
    while index < len(data):
        for i in data[index]['population']:
            earlier = data[index]['population']['2010']
            later = data[index]['population']['2019']
            speed = (later - earlier) / earlier * 100
            if speed < slowest:
                slowest = speed
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(slowest)
    print(state)
    print(county)

slowest_growth()

def deadliest():
    index = 0
    deaths = 0
    county = ''
    state = ''
    while index < len(data):
        S = 0
        FS = 0
        H = 0
        V = 0
        for i in data[index]['deaths']:
            if type(data[index]['deaths']['suicides']) == float: S = data[index]['deaths']['suicides']
            if type(data[index]['deaths']['firearm suicides']) == float: FS = data[index]['deaths']['firearm suicides']
            if type(data[index]['deaths']['homicides']) == float: H = data[index]['deaths']['homicides']
            if type(data[index]['deaths']['vehicle']) == float: V = data[index]['deaths']['vehicle']
            deathcount = S + FS + H + V
            if deathcount > deaths:
                deaths = deathcount
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(deaths)
    print(state)
    print(county)
deadliest()

def least_deadly():
    index = 0
    deaths = 3000
    county = ''
    state = ''
    while index < len(data):
        S = 0
        FS = 0
        H = 0
        V = 0
        for i in data[index]['deaths']:
            if type(data[index]['deaths']['suicides']) == float: S = data[index]['deaths']['suicides']
            if type(data[index]['deaths']['firearm suicides']) == float: FS = data[index]['deaths']['firearm suicides']
            if type(data[index]['deaths']['homicides']) == float: H = data[index]['deaths']['homicides']
            if type(data[index]['deaths']['vehicle']) == float: V = data[index]['deaths']['vehicle']
            deathcount = S + FS + H + V
            if deathcount < deaths:
                deaths = deathcount
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(deaths)
    print(state)
    print(county)
least_deadly()

def most_educated():
    county = ''
    state = ''
    index = 0
    educated = 0
    while index < len(data):
        graduates = 0
        for i in data[index]['edu']:
            if type(data[index]['edu']['bachelors+']) == float: graduates = data[index]['edu']['bachelors+']
            if graduates > educated:
                educated = graduates
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(educated)
    print(county)
    print(state)

most_educated()

def least_educated():
    county = ''
    state = ''
    index = 0
    educated = 100
    while index < len(data):
        graduates = 0
        for i in data[index]['edu']:
            if type(data[index]['edu']['bachelors+']) == float: graduates = data[index]['edu']['bachelors+']
            if graduates < educated:
                educated = graduates
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(educated)
    print(county)
    print(state)

least_educated()

def skewed_female():
    index = 0
    state = ''
    county = ''
    ratio = 0
    while index < len(data):
        for i in data[index]:
            amount = data[index]['female'] / data[index]['male']
            if amount > ratio:
                ratio = amount
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(ratio)
    print(state)
    print(county)

skewed_female()

def skewed_male():
    index = 0
    state = ''
    county = ''
    ratio = 0
    while index < len(data):
        for i in data[index]:
            amount = data[index]['male'] / data[index]['female']
            if amount > ratio:
                ratio = amount
                state = data[index]['state']
                county = data[index]['name']
        index += 1
    print(ratio)
    print(state)
    print(county)

skewed_male()
'''

with open('example.md', 'w') as mdfile:
    mdfile.write('# Lab 6: Data Scavenger Hunt\n')
    '''
