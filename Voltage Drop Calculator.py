class VoltageDropCalculator:

    def __init__(self, current, resistance):
        self.current = current
        self.resistance = resistance

    def calculate_voltage_drop(self):
        return self.current * self.resistance

    def calculate_percentage_drop(self, supply_voltage):
        voltage_drop = self.calculate_voltage_drop()
        return (voltage_drop / supply_voltage) * 100

    def display_result(self, supply_voltage):
        voltage_drop = self.calculate_voltage_drop()
        percentage = self.calculate_percentage_drop(supply_voltage)
        load_voltage = supply_voltage - voltage_drop

        print("----- Voltage Drop Calculator -----")
        print(f"Supply Voltage   : {supply_voltage:.2f} V")
        print(f"Load Current     : {self.current:.2f} A")
        print(f"Resistance       : {self.resistance:.2f} Ohm")
        print(f"Voltage Drop     : {voltage_drop:.2f} V")
        print(f"Percentage Drop  : {percentage:.2f} %")
        print(f"Load Voltage     : {load_voltage:.2f} V")


# Example values
supply_voltage = 230
current = 10
resistance = 0.5

calculator = VoltageDropCalculator(current, resistance)
calculator.display_result(supply_voltage)
