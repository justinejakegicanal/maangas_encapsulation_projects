class Car:
    def __init__(self, brand, model, year):
        self.__brand = str(brand)
        self.__model = str(model)
        self.__year = int(year)
        self.__current_speed = 0
        self.__is_engine_on = False