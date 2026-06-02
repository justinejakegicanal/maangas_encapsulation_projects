import os
import time
from car_logic import Car

class CarTelemetryApplication:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')