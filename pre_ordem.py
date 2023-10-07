def pre(a):
    if a!=None:
        print(a.raiz)
        pre(a.esq)
        pre(a.dir)