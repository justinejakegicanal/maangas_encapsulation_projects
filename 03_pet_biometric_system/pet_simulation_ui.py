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

        print("\n>>> ENTER PET BIOMETRIC DETAILS <<<")
        name = input(" Enter Pet Name: ").strip()
        animal_type = input(" Enter Animal Type (e.g., Dog, Cat): ").strip()
        
        while True:
            try:
                age = int(input(" Enter Pet Age (years): "))
                if age < 0:
                    print(" [ERROR]: Age cannot be negative!")
                    continue
                break
            except ValueError:
                print(" [ERROR]: Please enter a valid number for age.")