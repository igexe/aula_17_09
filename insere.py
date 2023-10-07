from arvore import Tree

def insere(arvore,raiz):
    if arvore is None:
        arvore=Tree(raiz)
    else:
        if raiz< arvore.raiz:
            arvore.esq=insere(arvore.esq,raiz)
        else:
            arvore.dir=insere(arvore.dir,raiz)
    return arvore

