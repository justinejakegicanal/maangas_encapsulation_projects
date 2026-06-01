import os
import time
from fan_logic import Fan

class FanSimulatorApplication:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')