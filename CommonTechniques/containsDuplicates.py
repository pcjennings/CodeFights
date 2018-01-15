def containsDuplicates(a):
    d = set()
    for i in a:
        if i in d:
            return True
        d.add(i)

    return False
