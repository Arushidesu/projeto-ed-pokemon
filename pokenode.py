cclass PokeNode:

    def __init__(self, numero, name, type1,	type2, total, HP, attack, defense, sp_atk,	sp_def, speed, generation, legendary):

        #
        self.__next = None
        self.__data = name
        #
        self.__numero = numero
        self.__type1 = type1
        self.__type2 = type2


    def get_data(self):

        return self.__data

    def get_next(self):

        return self.__next
    
    def set_data(self, new_data):

        self.__data = new_data
    
    def set_next(self, new_next):

        self.__next = new_next