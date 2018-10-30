from pokenode import PokeNode

#Lista modificada para aceitar apenas itens do PokeNode

class List:

    def __init__(self):

        self.__head = None

    
    def add(self, *item):

        '''Adiciona itens no índice 0 da lista'''

        temp = PokeNode(*item)
        temp.set_next(self.__head)
        self.__head = temp


    def remove(self, item):

        ''' Remove a primeira ocorrência do item na lista.'''

        current  = self.__head
        previous = None

        #A lista está vazia?
        if current == None:
            print("Não há itens nesta lista.")
        #O item removido é o primeiro da lista
        elif current.get_data() == item:
            self.__head = current.get_next()
        #Item removido não é o primeiro elemento
        else:
            #Vá até ele
            while current.get_data() != item:
                previous, current = current, current.get_next()
            previous.set_next(current.get_next())

    def size(self):

        '''Retorna a quantidade de itens presentes na lista (length)'''

        count = 0
        current = self.__head
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):

        '''Retorna True se a lista possuir o elemento'''

        current = self.__head
        while current != None:
            if current.get_data() != item:
                current = current.get_next()
            else:
                return True

        return False

    def is_empty(self):

        '''Verifica se a lista está vazia. Retorna True se verdadeiro.'''

        return self.__head == None

    def append(self, *item):

        '''Adiciona um item na última posição da lista'''

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
        

    def index(self, item):

        '''Retorna o índice do elemento na lista. Retorna -1 se a lista não possuí-lo'''

        count = 0
        current = self.__head
        try:
            while current.get_data() != item:
                current = current.get_next()
                count += 1
            return count
        except:
            return -1

    def insert(self, pos, *item):
        
        '''Adiciona um item no índice "pos"
        Se pos for >= o tamanho da lista, adiciona no fim'''

        current = self.__head
        previous = None
        temp = PokeNode(*item)
        count = 0

        #Lista vazia
        if self.is_empty():
            self.__head = temp
        #Demais casos
        else:
            try:
                #Pos 0
                if pos == 0:
                    temp.set_next(current)
                    self.__head = temp
                #Pos > 0 <= len
                else:  
                    #Verificar até o último índice da lista          
                    while count != pos:
                        previous, current = current, current.get_next()
                        count += 1
                    temp.set_next(current)
                    previous.set_next(temp)
            #Vai dar erro quando current for None, pois None.get_next(), e pos > len
            except:
                temp.set_next(current)
                previous.set_next(temp)
    
    #TODO
    # def pop(self, pos = None):
        
    #     '''Remove o último item da lista.
    #     Pode receber um índice específico.'''

    #     current = self.__head
    #     previous = None
    #     popped = None

    #     try:
    #         
    #     except:
    #         return "A lista está vazia"

    #     return popped
    
    def __str__(self):
        
        '''Printa a lista tal qual uma lista em Python, []'''

        current = self.__head
        lista_string = "[ "

        #A lista está vazia?
        if self.is_empty():
            return lista_string + "]"
        #Adicionar itens da lista
        while current != None:
            if current.get_next() == None:
                return lista_string + "{} ]".format(str(current.get_data()))
            lista_string += "{}, ".format(str(current.get_data()))
            current = current.get_next()
        