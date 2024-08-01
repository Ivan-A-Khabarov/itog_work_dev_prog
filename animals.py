# animals.py

class Animals:
    def __init__(self, name, commands, birth_date):
        self.__name = name
        self.__commands = commands
        self.__birth_date = birth_date
    
    def get_name(self):
        return self.__name
    
    def get_commands(self):
        return self.__commands
    
    def get_birth_date(self):
        return self.__birth_date
    
    def set_commands(self, commands):
        self.__commands = commands

class DomesticAnimals(Animals):
    pass

class Dogs(DomesticAnimals):
    pass

class Cats(DomesticAnimals):
    pass

class Hamsters(DomesticAnimals):
    pass

class PackAnimals(Animals):
    pass

class Horses(PackAnimals):
    pass

class Donkeys(PackAnimals):
    pass


