"""TPRG2131 Winter 202x RC class starter with simplistic test code."""

import math

class ResistorCapacitor:
    """Model a resistor-capacitor (RC) network that charges or discharges over time."""

    def __init__(self, resistance, capacitance, initial=0.0):
        """Initialize with resistance (Ohms), capacitance (Farads), and initial voltage (Volts)."""
        self.resistance = resistance
        self.capacitance = capacitance
        self.initial_voltage = initial
        self._voltage = initial  # The starting voltage for the RC network

    #
    # Mutator methods
    #
    def set_voltage(self, voltage):
        """Set the initial voltage."""
        self.initial_voltage = voltage
        self._voltage = voltage

    #
    # Accessor methods
    #
    def voltage(self, time):
        """Calculate the voltage at a given time during charging or discharging.
        
        Formula for charging: V(t) = V_initial * exp(-t / (R * C))
        """
        # Compute the voltage decay over time using the RC time constant.
        tau = self.resistance * self.capacitance
        return self.initial_voltage * math.exp(-time / tau)

## Test code (place at bottom of the file)
if __name__ == "__main__":
    print("Self testing...")
    rc1 = ResistorCapacitor(1000.0, 1.0e-6)
    rc1.set_voltage(5.0)
    rc2 = ResistorCapacitor(10.0e3, 22.0e-6, 12.0)

    print("rc1:")
    print(rc1.resistance, rc1.capacitance, rc1.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 0.5e-3
        print(f"Time {stime:.4f}s -> Voltage: {rc1.voltage(stime):.4f} V")

    print("rc2:")
    print(rc2.resistance, rc2.capacitance, rc2.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 150.0e-3
        print(f"Time {stime:.4f}s -> Voltage: {rc2.voltage(stime):.4f} V")
# done
