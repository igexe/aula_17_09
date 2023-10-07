def menor(a):
    if a.esq!=None:menor(a.esq)
    else:
        print(a.raiz)