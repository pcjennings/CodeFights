def sumOfTwo(a, b, v):
    a = set(a)
    b = set(b)

    return any(v - x in a for x in b)
