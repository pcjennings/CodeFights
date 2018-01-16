def removeKFromList(l, k):
    r = []
    while l is not None:
        v = l.value
        if v != k:
            r.append(v)
        l = l.next

    return r
