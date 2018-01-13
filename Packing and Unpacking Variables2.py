random_list = [
        {"num1": "1 + 2", "num2": 3}, 
        {"num1": "2 + 3", "num2": 5}, 
        {"num1":"5 + 7", "num2": 12}
        ]

def number_factory(arg1):
    result = []
    for i in arg1:
        result.append(factory.format(**i))
    return result

factory = "{num1} = {num2}!"

print(number_factory(random_list))