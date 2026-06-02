import os
import time
from car_logic import Car

class CarTelemetryApplication:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_simulation(self):
        self.clear_screen()
        test_car = Car(2026, "Maangas GT")

        for _ in range(5):
            test_car.accelerate()
            print(f"🚀 Accelerating... Current Velocity: {test_car.get_speed()} km/h")

        for _ in range(5):
            test_car.brake()
            print(f"🛑 Braking... Current Velocity: {test_car.get_speed()} km/h")

if __name__ == "__main__":
    app_engine = CarTelemetryApplication()
    app_engine.run_simulation()