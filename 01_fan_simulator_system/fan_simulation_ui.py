import os
import time

class FanSimulatorUI:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_registry_flow(self):
        self.clear_terminal()
        print("==========================================")
        print("         ELECTRIC FAN REGISTRY UI         ")
        print("==========================================")
        print(" [SYSTEM]: Initializing core motor telemetry...")
        time.sleep(1)

        print("\n>>> CONFIGURING FAN SPECIFICATIONS <<<")
        brand = input(" Enter Fan Brand: ").strip()