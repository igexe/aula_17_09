from insere import insere
from arvore import Tree
from pre_ordem import pre
from em_ordem import em
from pos_ordem import pos
from busca import busc
from menor import menor
from maior import maior
from soma import soma
from conta_no import conta
from conta_folha import folhas
from media import media
from altura import altura

arbore=Tree(20)

insere(arbore,10)

insere(arbore,7)

insere(arbore,6)

insere(arbore,15)

insere(arbore,30)

insere(arbore,90)

print('\npre ordem\n')
pre(arbore)

print('\nem ordem\n')
em(arbore)

print('\npos ordem\n')
pos(arbore)

busc(arbore,10)

print('\nmaior número da arvore\n')
maior(arbore)

print('\nmenor número da arvore\n')
menor(arbore)

print('\na soma dos nós é:\n')
print(soma(arbore))

print('\na quantidade de nós na arvore é:\n')
print(conta(arbore))

print('\na quantidade de folhas na arvore é:\n')
print(folhas(arbore))

print('\na media dos valores da arvore é:\n')
media(arbore)

print('\na altura da arvore binaria é:\n')
altura(arbore)