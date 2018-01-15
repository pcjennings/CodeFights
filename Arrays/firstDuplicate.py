def firstDuplicate(a):
    aset = set()
    for i in a:
        if i in aset:
            return(i)
        aset.add(i)

    return -1
