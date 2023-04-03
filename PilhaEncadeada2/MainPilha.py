from PilhaEncadeada import Pilha, PilhaException

p = Pilha()

for i in range (1,11):
    p.empilha(i*10)

print(p)
print(len(p))
try:
    while(True):
        print('desempilha: ', p.desempilha())
except PilhaException as pe:
    print(pe)
print(p)
print(len(p))