def altura(a):
    print(mede(a))

def mede(a):
    if a==None:
        return 0
    else:
        esq=mede(a.esq)
        dir=mede(a.dir)
        return max(esq,dir)+1