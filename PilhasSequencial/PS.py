# Inserção e remoção na mesma ponta do vetor
# LIFO - Last in First Out - O ultimo que entrou na pilha(o cara que tá em cima) é o primeiro que sai.
# e consequentemente, o primeiro que entra é o último que sair.
class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)




class PilhaSequencial:
    def __init__(self):
        self.__dados=[]

    def vazio(self):
        return len(self.__dados)==0
    
    def tamanho(self):
        return len(self.__dados)
    
    def topo(self):
        if self.vazia():
            raise PilhaException('A pilha está empaty')
        return self.__dados[0]
    
    # Controla a inserção
    def inserir(self,dado):
        self.__dados.insert(0,dado)
    # Controla a remoção
    def remover(self):
        if self.vazio():
            raise PilhaException('A pilha está vazio')
        return self.__dados.pop()
    
    def __str__(self) -> str:
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())


if __name__ == '__main__':
    p=PilhaSequencial()

    for i in range(1,6):
        p.inserir(i*10)

    print(p)
    try:
        p.remover()
        p.remover()
        p.remover()
        p.remover()
        p.remover()
        p.remover()
        print(p)
    except PilhaException as pe:
         print(pe)


