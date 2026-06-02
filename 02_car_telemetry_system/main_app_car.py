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

if __name__ == "__main__":
    app_engine = CarTelemetryApplication()
    app_engine.run_simulation()