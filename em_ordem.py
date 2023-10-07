def em(a):
    if a!=None:
        em(a.esq)
        print(a.raiz)
        em(a.dir)