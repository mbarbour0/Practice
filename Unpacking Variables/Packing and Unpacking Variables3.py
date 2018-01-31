list1 = [
        {"Item1": "Laser Sword", "Item2": "Wooden Shield"},
        {"Item1": "Long Hammer", "Item2": "Royal Shield"},
        {"Item1": "Gun", "Item2": None}
        ]

def inventory(arg1):
    result = []
    for i in arg1:
        result.append(stringline.format(**i))
    return result

stringline = "You were spawned with a {Item1} for your offensive item and a {Item2} for your defensive item. Please proceed to the next room for instructions"

print(inventory(list1))