import os
import time
from pet_logic import Pet

class PetBiometricSimulator:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')