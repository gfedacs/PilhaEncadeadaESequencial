
class no:
    def __init__(self,carga,proximo = None):
        self.__carga = carga # Essa é a carga atual
        self.__proximo = proximo # Essa é a próxima carga
    

    @property
    def carga (self):
        return self.__carga
    @carga.setter
    def carga (self,nova_carga):
        self.__carga = nova_carga
    @property
    def proximo (self):
        return self.__proximo
    @proximo.setter
    def proximo(self,novo_proximo):
        self.__proximo = novo_proximo
    def TemProximo (self) -> bool:
        return self.__proximo == None
    def __str__(self):
        return f'{self.__carga}'
