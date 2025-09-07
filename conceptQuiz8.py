def hashList(L, n):
    for i in L:
        print(hash(i) % n)


L = [6,9,21,15]
hashList(L, 5)