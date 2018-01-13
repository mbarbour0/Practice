dicts = [
        {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
    ]

def runtime(arg1):
    result = []
    for i in arg1:
        result.append(stringline.format(**i))
    return result

stringline = "Hi, my name is {name} and my favorite food is {food}"

print(runtime(dicts))