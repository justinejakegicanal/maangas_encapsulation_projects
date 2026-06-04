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

    def start_control_loop(self, fan):
        while True:
            self.clear_terminal()
            print("==========================================")
            print("          FAN TELEMETRY MONITOR          ")
            print("==========================================")
            print(f" [+] Fan Brand:    {fan.get_brand()}")
            print(f" [+] Max Speed:    {fan.get_max_speed()}")
            print(f" [+] Current Speed: {fan.get_current_speed()}")
            print("==========================================")
            print(" [1] Change Speed Setting")
            print(" [2] Shutdown / Terminate Simulation")
            
            choice = input("\n Select Action: ").strip()
            
            if choice == "1":
                while True:
                    try:
                        new_speed = int(input(f" Enter speed level (0-{fan.get_max_speed()}): "))
                        if fan.set_speed(new_speed):
                            print(" [SUCCESS]: Motor rotation velocity updated.")
                        else:
                            print(" [ERROR]: Invalid speed adjustment setting!")
                        break
                    except ValueError:
                        print(" [ERROR]: Please enter a valid integer for speed level.")
                time.sleep(1.5)
            elif choice == "2":
                print("\n [SYSTEM]: Powering down magnetic core coils...")
                time.sleep(1)
                break
            else:
                print(" [ERROR]: Invalid selection option.")
                time.sleep(1)