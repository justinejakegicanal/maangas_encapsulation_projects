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

        while True:
            try:
                year = int(input(" Enter Manufacturing Year: "))
                if year <= 1885:  # Taon kung kailan naimbento ang unang kotse
                    print(" [ERROR]: Invalid year. Please enter a realistic vehicle year.")
                    continue
                break
            except ValueError:
                print(" [ERROR]: Please enter a valid integer for the year.")

        from car_logic import Car
        car_instance = Car(brand, model, year)
        self.start_control_loop(car_instance)
    
    def start_control_loop(self, car):
        while True:
            self.clear_terminal()
            print("==========================================")
            print("         VEHICLE TELEMETRY SYSTEM         ")
            print("==========================================")
            print(f" [+] Vehicle Brand: {car.get_brand()}")
            print(f" [+] Vehicle Model: {car.get_model()}")
            print(f" [+] Model Year:    {car.get_year()}")
            print(f" [+] Engine Status: {'ON' if car.is_engine_on() else 'OFF'}")
            print(f" [+] Current Speed: {car.get_current_speed()} km/h")
            print("==========================================")
            print(" [1] Toggle Engine Ignition")
            print(" [2] Step on Accelerator")
            print(" [3] Apply Service Brakes")
            print(" [4] Terminate Telemetry Session")
            
            choice = input("\n Select Action: ").strip()
            
            if choice == "1":
                status = car.toggle_engine()
                print(f" [SYSTEM]: {status}.")
                time.sleep(1.5)
            
            elif choice == "2":
                if not car.is_engine_on():
                    print(" [WARNING]: Cannot accelerate. Start the engine first!")
                    time.sleep(1.5)
                    continue
                while True:
                    try:
                        amt = int(input(" Enter acceleration increment (km/h): "))
                        if amt < 0:
                            print(" [ERROR]: Increment cannot be negative.")
                            continue
                        car.accelerate(amt)
                        print(" [SUCCESS]: Velocity increased.")
                        break
                    except ValueError:
                        print(" [ERROR]: Please enter a valid integer.")
                time.sleep(1.5)