def pos(a):
    if a!=None:
        pos(a.esq)
        pos(a.dir)
        print(a.raiz)