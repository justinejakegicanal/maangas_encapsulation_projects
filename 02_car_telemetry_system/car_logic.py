class Car:
    def __init__(self, year_model, make):
        self.__year_model = str(year_model)
        self.__make = str(make)
        self.__speed = 0

    def get_speed(self):
        return self.__speed