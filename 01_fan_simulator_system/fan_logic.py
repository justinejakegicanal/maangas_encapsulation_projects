class Fan:
    def __init__(self, brand, max_speed):
        self.__brand = str(brand)
        self.__max_speed = int(max_speed)
        self.__current_speed = 0

    def get_brand(self):
        return self.__brand

    def get_max_speed(self):
        return self.__max_speed

    def get_current_speed(self):
        return self.__current_speed

    def set_speed(self, speed):
        new_speed = int(speed)
        if 0 <= new_speed <= self.__max_speed:
            self.__current_speed = new_speed
            return True
        return False