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

        while True:
            try:
                max_speed = int(input(" Enter Maximum Speed (1-5): "))
                if max_speed <= 0:
                    print(" [ERROR]: Maximum speed must be greater than 0!")
                    continue
                break
            except ValueError:
                print(" [ERROR]: Please enter a valid integer for speed.")

        from fan_logic import Fan
        fan_instance = Fan(brand, max_speed)
        self.start_control_loop(fan_instance)