from node import Node
from pokenode import PokeNode

class Queue:

    def __init__(self):
        self.__head = None

    def is_empty(self):

        '''Verificar se a fila esta vazia'''

        return self.__head == None


    def enqueue(self, *item):

        current = self.__head
        temp = PokeNode(*item)
        #A lista está vazia
        if current == None:
            self.__head = temp
        #A lista não está vazia
        else:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(temp)


    def dequeue(self):
        
        '''Retirar item na posição 0'''

        current = self.__head
        dq = current.get_data()
        self.__head = current.get_next()

        return dq


    def size(self):

        '''Retorna a quantidade de itens presentes na fila'''
    
    count = 0
    current = self.__head
    while current != None:
        count += 1
        current = current.get_next()

    return count

    def __str__(self):

