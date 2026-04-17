def christmas_tree():
    a = int(input("AMout of tres"))
    b = []
    z_length = len(b)
    for x in range(a):
        c = int(input("How tall are the trees?"))
        b.append(c)
    d = []
    for e in b:
        for f in b:
            if e > f:
                d.append(e)
                d.append(f)
    print(d)
    for h in d:
        for i in d:
            if h == d:
                d.remove(h)
    print(d)

        
christmas_tree()