class Car:
    def __init__(self, brand, model, year):
        self.__brand = str(brand)
        self.__model = str(model)
        self.__year = int(year)
        self.__current_speed = 0
        self.__is_engine_on = False

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_current_speed(self):
        return self.__current_speed

    def is_engine_on(self):
        return self.__is_engine_on

    def toggle_engine(self):
        if self.__is_engine_on:
            self.__is_engine_on = False
            self.__current_speed = 0
            return "Engine Stopped"
        else:
            self.__is_engine_on = True
            return "Engine Started"

    def accelerate(self, increment):
        if not self.__is_engine_on:
            return False
        
        self.__current_speed += int(increment)
        return True

    def brake(self, decrement):
        if not self.__is_engine_on:
            return False
            
        self.__current_speed -= int(decrement)
        if self.__current_speed < 0:
            self.__current_speed = 0
        return True