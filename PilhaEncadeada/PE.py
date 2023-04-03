class Node:
    def __init__(self, dado:any):
        self.__dado = dado
        self.__prox = None
        

    # get
    # mostra qual é a carga 
    @property
    def dado (self):
        return self.__dado
    # set
    # realiza a alteração da carga
    @dado.setter
    def dado(self,novo):
        self.__dado = novo

    # get 
    # mostra qual é o próximo
    @property
    def prox(self):
        return self.__prox

    # set   
    # altera o próximo
    @prox.setter
    def prox(self,novo):
        self.__prox = novo