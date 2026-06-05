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
        frames = ['/', '-', '\\', '|']
        for i in range(5):
            symbol = frames[i % 4]
            print(f" Connecting to ECU Core Node... {symbol}", end="\r")
            time.sleep(0.3)
        print(" [OK]: ECU Satellite Core Connected.         ")
        time.sleep(0.5)

        print("\n>>> CONFIGURING VEHICLE SPECS <<<")
        brand = input(" Enter Car Brand: ").strip()
        model = input(" Enter Car Model: ").strip()

        while True:
            try:
                year = int(input(" Enter Manufacturing Year: "))
                if year <= 1885:
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
            
            speed = car.get_current_speed()
            gauge_bar = "█" * (speed // 10)
            print(f" [+] Current Speed: {speed} km/h [{gauge_bar:<15}]")
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
            elif choice == "3":
                if not car.is_engine_on():
                    print(" [WARNING]: Engine is off. Brakes are locked.")
                    time.sleep(1.5)
                    continue
                while True:
                    try:
                        amt = int(input(" Enter braking decrement (km/h): "))
                        if amt < 0:
                            print(" [ERROR]: Decrement cannot be negative.")
                            continue
                        car.brake(amt)
                        print(" [SUCCESS]: Velocity decreased.")
                        break
                    except ValueError:
                        print(" [ERROR]: Please enter a valid integer.")
                time.sleep(1.5)
            elif choice == "4":
                print("\n [SYSTEM]: Disconnecting telemetry stream...")
                time.sleep(1)
                break
            else:
                print(" [ERROR]: Invalid transmission option.")
                time.sleep(1)