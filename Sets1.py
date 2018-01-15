COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(arg1):
    result = []
    for key, value in COURSES.items():
        if value & arg1:
            result.append(key)
    return result
    
def covers_all(arg1):
    result = []
    for key, value in COURSES.items():
        if (arg1 & value) == arg1:
            result.append(key)
    return result

print(covers_all({"input", "functions"}))