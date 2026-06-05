import os
import time

class FanSimulatorUI:
    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_registry_flow(self):
        self.clear_terminal()
        print("==========================================")
        print("           FAN REGISTRY SYSTEM            ")
        print("==========================================")
        print(" [SYSTEM]: Initializing device controllers...")
        time.sleep(1)

        print("\n>>> CONFIGURING DEVICE SPECS <<<")
        brand = input(" Enter Fan Brand: ").strip()
        
        while True:
            try:
                max_speed = int(input(" Enter Maximum Speed Level: "))
                if max_speed <= 0:
                    print(" [ERROR]: Maximum speed must be greater than 0.")
                    continue
                break
            except ValueError:
                print(" [ERROR]: Please enter a valid integer for maximum speed.")

        from fan_logic import Fan
        fan_instance = Fan(brand, max_speed)
        self.start_control_loop(fan_instance)

    def start_control_loop(self, fan):
        while True:
            self.clear_terminal()
            print("==========================================")
            print("          FAN TELEMETRY SYSTEM            ")
            print("==========================================")
            print(f" [+] Fan Brand:    {fan.get_brand()}")
            print(f" [+] Power Status: {'ON' if fan.get_current_speed() > 0 else 'OFF'}")
            print(f" [+] Current Speed: {fan.get_current_speed()}")
            print("==========================================")
            print(" [1] Set Fan Speed")
            print(" [2] Terminate Fan Session")
            
            choice = input("\n Select Action: ").strip()
            
            if choice == "1":
                while True:
                    try:
                        speed = int(input(" Enter speed level (0 for OFF): "))
                        fan.set_speed(speed)
                        
                        if speed > 0:
                            frames = ['-', '\\', '|', '/']
                            for _ in range(12):
                                for frame in frames:
                                    self.clear_terminal()
                                    print("==========================================")
                                    print("          FAN TELEMETRY SYSTEM            ")
                                    print("==========================================")
                                    print(f" [+] Fan Brand:    {fan.get_brand()}")
                                    print(f" [+] Power Status: ON")
                                    print(f" [+] Current Speed: {speed}  [{frame}]")
                                    print("==========================================")
                                    time.sleep(0.05 / speed)
                        
                        print(f" [SUCCESS]: Fan speed updated to {speed}.")
                        break
                    except ValueError:
                        print(" [ERROR]: Please enter a valid integer.")
                time.sleep(1)
            elif choice == "2":
                print("\n [SYSTEM]: Disconnecting device stream...")
                time.sleep(1)
                break
            else:
                print(" [ERROR]: Invalid transmission option.")
                time.sleep(1)