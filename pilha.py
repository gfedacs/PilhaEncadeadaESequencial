from no import no
class PilhaException (Exception):
    def __init__(self,mensagem):
        super().__init__(mensagem)

#Importante saber: Inserir, remover, observar o topo da pilha, vazia
class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
    def vazia(self):
        return self.__tamanho == 0
    def inserir(self,nova_carga):
        # Inseri o elemento no topo 
        no1 = no(nova_carga)  # Foi criado um objeto e escolheu um número pra ser inserido na pilha
        no1.proximo = self.__topo # Agora o próximo vai ser igual oq ja tinha, como a lista está vazia é igual a None.
        self.__topo = no1 # e por fim, o topo agora será o novo valor que foi definido que é o novoDado
        self.__tamanho += 1 
        
    def remover (self):
        # Remove um elemento dentro da pilha, que necessariamente precisa ser o último.
        if self.vazia():
            raise PilhaException(f'Não é possível ver qual é o topo, pois está vazia')
        self.__topo = self.__topo.proximo

    def __str__(self):
        saida = 'Pilha: [' 
        p = self.__topo

        while p != None:
            saida += f'{p.carga}'
            p = p.proximo

            if p !=None: 
                saida += ', ' 

        saida += ']'
        return saida
    def imprimir(self):
        print(self.__str__())

    def modificar(self,novoValor):
        if self.vazia():
            raise PilhaException(f'Não é possível ver qual é o topo, pois está vazia')
        self.__topo.carga=novoValor
    @property
    def observar(self):
        if self.vazia():
            raise PilhaException(f'Não é possível ver qual é o topo, pois está vazia')
        return self.__topo.carga
    def tamanho (self):
        return self.__tamanho


if __name__ == '__main__':

  p = Pilha()

  p.inserir(10)
  p.inserir(20)
  p.inserir(10)
  p.inserir(10)
  print(p)
  p.remover()
  print(p)
  p.remover()
  print(p)  





