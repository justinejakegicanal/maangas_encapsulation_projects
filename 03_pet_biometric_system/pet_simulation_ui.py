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

        pet_record = Pet(name, animal_type, age)
        self.display_biometric_profile(pet_record)

    def display_biometric_profile(self, pet_obj):
        print("\n==========================================")
        print("       SECURE BIOMETRIC PROFILE LOG       ")
        print("==========================================")
        time.sleep(0.6)
        print(f" [+] Registry Name:  {pet_obj.get_name().upper()}")
        time.sleep(0.4)
        print(f" [+] Species Type:   {pet_obj.get_animal_type().title()}")
        time.sleep(0.4)
        print(f" [+] Calculated Age: {pet_obj.get_age()} year(s) old")
        print("==========================================")
        time.sleep(0.6)
        print(" [SUCCESS]: Biometric signature saved cleanly!\n")