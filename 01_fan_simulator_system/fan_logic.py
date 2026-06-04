class Fan:
    def __init__(self, brand, max_speed):
        self.__brand = str(brand)
        self.__max_speed = int(max_speed)
        self.__current_speed = 0    