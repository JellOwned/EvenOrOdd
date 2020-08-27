def isEven(number):
    if not isinstance(number, (int, str)) or isinstance(number, bool):
        raise ValueError("Expected an integer or a string")

    elif isinstance(int(number), ValueError):
        raise ValueError("String must contain only a number")

    return (abs(int(number)) % 2 == 0)

def isOdd(number):
    if not isinstance(number, (int, str)) or isinstance(number, bool):
        raise ValueError("Expected an integer or a string")

    elif isinstance(int(number), ValueError):
        raise ValueError("String must contain only a number")
    
    return (abs(int(number)) % 2 == 1)