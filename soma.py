def percorre(a):
    if a==None:
        return 0
    else:
        return a.raiz+percorre(a.esq)+percorre(a.dir)
    
def soma(a):
    return percorre(a)