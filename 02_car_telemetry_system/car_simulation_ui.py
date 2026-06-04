import os
import time

class CarSimulatorUI:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_registry_flow(self):
        self.clear_terminal()
        print("==========================================")
        print("         VEHICLE REGISTRY SYSTEM          ")
        print("==========================================")
        print(" [SYSTEM]: Establishing terminal downlink...")
        time.sleep(1)

        print("\n>>> CONFIGURING VEHICLE SPECS <<<")
        brand = input(" Enter Car Brand: ").strip()
        model = input(" Enter Car Model: ").strip()