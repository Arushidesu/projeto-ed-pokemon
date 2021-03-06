from pokenode import PokeNode

class Stack:

    def __init__(self):

        self.__head = None
    
    def is_empty(self):

        '''Verifica se a pilha está vazia'''

        return self.__head == None
    
    def push(self, *item):
        
        '''Adiciona itens no índice 0'''

        current = self.__head
        temp = PokeNode(*item)

        #A pilha está vazia
        if self.is_empty():
            self.__head = temp
        else:
            temp.set_next(current)
            self.__head = temp

    def pop(self):
        
        '''Remove, se houver, o índice 0'''


    def peek(self):
    
        '''Mostra, se houver, o índice 0'''

    #Dá erro se não existem elementos na pilha

    def size(self):

        '''Diz quantos elementos a pilha possui'''

    def __str__(self):
        
        
        #Exemplo: < Bulbasauro, ... [+ 149] <

        current = self.__head
        pilha_string = "< "

        #A pilha está vazia?
        if self.is_empty():
            return pilha_string + "... <"
        #Adicionar itens da pilha
        while current != None:
            if current.get_next() == None:
                return pilha_string + "{} <".format(str(current.get_data()))
            pilha_string += "{}, ".format(str(current.get_data()))
            current = current.get_next()