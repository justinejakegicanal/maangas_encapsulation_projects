class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_on(self):
        return self.__on
    
    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            raise ValueError("Invalid fan speed level index.")

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = float(radius)
        else:
            raise ValueError("Fan blade radius must be a positive scalar attribute.")

    def set_color(self, color):
        if color.strip():
            self.__color = str(color)
        else:
            raise ValueError("Fan aesthetic color property cannot be empty.")

    def set_on(self, on_status):
        self.__on = bool(on_status)

    