def does_something(arg):
    """This function takes different types of input, including int, float, and string.
    Entering a string returns that string 3 times.
    Entering an integer or a float returns that number * 3.
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")
