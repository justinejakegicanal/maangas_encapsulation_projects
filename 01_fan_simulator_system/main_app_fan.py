import os
import time
from fan_logic import Fan

class FanSimulatorApplication:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_simulation(self):
        self.clear_screen()
        
        fan_unit_one = Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)
        fan_unit_two = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

if __name__ == "__main__":
    app_engine = FanSimulatorApplication()
    app_engine.run_simulation()