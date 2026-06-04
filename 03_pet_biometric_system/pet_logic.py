class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = str(name)
        self.__animal_type = str(animal_type)
        self.__age = int(age)

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age