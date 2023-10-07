def corre(a):
    if a==None:
        return 0
    elif a.esq==None and a.dir==None:
        return 1
    else:
        return corre(a.esq)+corre(a.dir)
    
def folhas(a):
    return corre(a)