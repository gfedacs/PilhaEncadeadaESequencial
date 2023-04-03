from PE import Node
class PilhaException(Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)



class PilhaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    # Vai retonar o valor da pilha que está na primeira posição.

    @property
    def topo(self):
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        
        return self.__topo.dado
    
    def vazia(self):
        return self.__tamanho == 0
    
    def tamanho(self):
        return self.__tamanho
    
    def inserir(self,novoDado):
        no = Node(novoDado) # Foi feito um objeto e escolheu um número
        no.prox = self.__topo # Agora o próximo vai ser igual oq ja tinha, como a lista está vazia é igual a None.
        self.__topo = no # e por fim, o topo agora será o novo valor que foi definido que é o novoDado
        self.__tamanho -= 1



    def remocao(self,):
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        self.__topo = self.__topo.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = 'Pilha: [' 
        p = self.__topo

        while p != None:
            saida += f'{p.dado}'
            p = p.prox

            if p !=None: 
                saida += ', ' 

        saida += ']'
        return saida
    
    def imprimir(self):
        print(self.__str__())

    def modificar (self, novoValor):
        if self.vazia(): #dúvida
            raise PilhaException('A pilha está vazia')
        self.__topo.dado = novoValor #dúvida

if __name__== '__main__':
     
    p=PilhaEncadeada()

    p.inserir(10)
    p.inserir(20)
    p.inserir(30)
    p.inserir(40)


print(p)
print(p)
p.remocao()
print(p)

