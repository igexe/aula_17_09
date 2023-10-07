def busc(a,v):
    if a!=None:
        if a.raiz==v:
            print('\n'+str(v)+' foi encontrado nessa arvore\n')

        elif v<a.raiz:
            busc(a.esq,v)

        elif v>a.raiz:
            busc(a.dir,v)
    
    else:
        print('\n'+str(v)+' não existe nessa arvore\n')