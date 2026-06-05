import os
import time

class PetBiometricSimulator:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_registry_flow(self):
        self.clear_terminal()
        print("==========================================")
        print("           PET REGISTRY SYSTEM            ")
        print("==========================================")
        print(" [SYSTEM]: Initializing biometric scanners...")
        time.sleep(1)

        print("\n>>> CONFIGURING PET BIOMETRICS <<<")
        name = input(" Enter Pet Name: ").strip()
        animal_type = input(" Enter Animal Type: ").strip()

        while True:
            try:
                age = int(input(" Enter Pet Age: "))
                if age < 0:
                    print(" [ERROR]: Age cannot be negative.")
                    continue
                break
            except ValueError:
                print(" [ERROR]: Please enter a valid integer for age.")

        from pet_logic import Pet
        pet_instance = Pet(name, animal_type, age)
        self.start_control_loop(pet_instance)

    def start_control_loop(self, pet):
        while True:
            self.clear_terminal()
            print("==========================================")
            print("         PET BIOMETRIC DASHBOARD          ")
            print("==========================================")
            print(f" [+] Pet Name:    {pet.get_name()}")
            print(f" [+] Animal Type: {pet.get_animal_type()}")
            print(f" [+] Pet Age:     {pet.get_age()} years old")
            
            pulse_frames = ['_v_v_v_', 'v_v_v_v', '_v_v_v_', '_______']
            for frame in pulse_frames:
                self.clear_terminal()
                print("==========================================")
                print("         PET BIOMETRIC DASHBOARD          ")
                print("==========================================")
                print(f" [+] Pet Name:    {pet.get_name()}")
                print(f" [+] Animal Type: {pet.get_animal_type()}")
                print(f" [+] Pet Age:     {pet.get_age()} years old")
                print(f" [+] Vital Pulse: [ {frame} ] Active Monitoring")
                print("==========================================")
                time.sleep(0.15)

            print(" [1] Update Pet Age")
            print(" [2] Terminate Biometric Session")
            
            choice = input("\n Select Action: ").strip()
            
            if choice == "1":
                while True:
                    try:
                        new_age = int(input(" Enter new age: "))
                        if new_age < 0:
                            print(" [ERROR]: Age cannot be negative.")
                            continue
                        
                        pet.set_age(new_age)
                        print(f" [SUCCESS]: Age updated to {pet.get_age()}.")
                        break
                    except ValueError:
                        print(" [ERROR]: Please enter a valid integer.")
                time.sleep(1.5)
            elif choice == "2":
                print("\n [SYSTEM]: Disconnecting biometric stream...")
                time.sleep(1)
                break
            else:
                print(" [ERROR]: Invalid transmission option.")
                time.sleep(1)