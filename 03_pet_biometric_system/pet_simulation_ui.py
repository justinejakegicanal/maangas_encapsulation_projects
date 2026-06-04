import os
import time
from pet_logic import Pet

class PetBiometricSimulator:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_registry_flow(self):
        self.clear_terminal()
        print("==========================================")
        print("      PET BIOMETRIC REGISTRY SYSTEM       ")
        print("==========================================")
        print(" [SYSTEM]: Initializing secure biometric links...")
        time.sleep(1)