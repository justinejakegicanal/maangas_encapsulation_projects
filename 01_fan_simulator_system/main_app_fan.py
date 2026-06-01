import os
import time
from fan_logic import Fan

class FanSimulatorApplication:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_simulation(self):
        self.clear_screen()
        print("╔════════════════════════════════════════╗")
        print("║   MAANGAS PRO FAN DIAGNOSTIC SYSTEM    ║")
        print("╚════════════════════════════════════════╝\n")

        start_time = time.perf_counter()

        fan_unit_one = Fan(speed=Fan.FAST, radius=10.0, color="yellow", on=True)
        fan_unit_two = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", on=False)

        units_registry = {
            "Diagnostic Profile Unit Alpha": fan_unit_one, 
            "Diagnostic Profile Unit Beta": fan_unit_two
        }

        for identifier, unit in units_registry.items():
            print(f"📡 Analyzing Status Engine Metrics for: [ {identifier} ]")
            print(f" ├── Operational Power Status : {'ON (RUNNING)' if unit.get_on() else 'OFF (STANDBY)'}")
            print(f" ├── Kinetic Rotation Velocity: Speed Level {unit.get_speed()}")
            print(f" ├── Physical Blade Radius    : {unit.get_radius()} units")
            print(f" └── Shell Chromatic Aesthetic: {unit.get_color().upper()}")
            print("-" * 50)

        end_time = time.perf_counter()
        print(f"⏱️ Telemetry metrics computed in: {(end_time - start_time) * 1000:.4f} ms")
        print("\nThank you!")

if __name__ == "__main__":
    app_engine = FanSimulatorApplication()
    app_engine.run_simulation()