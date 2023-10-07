def maior(a):
    if a.dir!=None:maior(a.dir)
    else:print(a.raiz)