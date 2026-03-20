dic = {
    "piece": 'portion of the object or of the material, produced by cutting',
    'patch': 'a piece of cloth used to mend or strengthen a weak point',
    'area': 'a region or a part of a town, a country, or the world',
    'visit': 'go to see and spend time with someone',
    'with': 'having',
    'small': 'less than normal'
}

values = list(dic.values())

# lengths of meanings
lengths = [len(v) for v in values]

# find max and min
max_len = max(lengths)
min_len = min(lengths)

# get index
max_index = lengths.index(max_len)
min_index = lengths.index(min_len)

# get actual values
longest = values[max_index]
shortest = values[min_index]

print("Longest meaning:", longest)
print("Shortest meaning:", shortest)