def nos(a):
    if a is None: return 0
    else: return 1+nos(a.esq)+nos(a.dir)

def conta(a):
    return(nos(a))