dict1 = {
        'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 
        'Kenneth Love': ['Python Basics', 'Python Collections']
        }

def num_teachers(arg1):
    count = 0
    for i in arg1:
        count += 1
    return count

def num_courses(arg1):
    result = []
    for i in arg1.values():
        result += i
    return len(result)

print(num_courses(dict1))

def stats(arg1):
    result = []
    for teacher, course in arg1.items():
        result += [[teacher, len(course)]]
    return result

print(stats(dict1))