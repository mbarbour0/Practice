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

def string_factory(dicts):
    array = []
    for item in dicts:                
        array.append(template.format(**item))
    return array

template = "Hi, I'm {name} and I love to eat {food}!"

print(string_factory(dicts))