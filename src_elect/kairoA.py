from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("LED Circuit")
circuit.V("1", "n001", circuit.gnd, 3 @ u_V)
circuit.R("2", "n006", circuit.gnd, 2.4 @ u_kΩ)
circuit.R("1", "n001", "n006", 5.1 @ u_kΩ)
circuit.SinusoidalVoltageSource(
    "2",
    "n005",
    circuit.gnd,
    amplitude=0.93 @ u_V,
    offset=100 @ u_mV,
    frequency=1 @ u_kHz,
)

# Assuming that 'XU1' is an operational amplifier
circuit.SubCircuitFactory("XU1", "n006", "n002", "n001", circuit.gnd, "n003", "level2")
circuit.model(
    name="XU1",
    modele_type="OpAmp",
    Avol=1 @ u_Meg,
    GBW=10 @ u_Meg,
    slew=10 @ u_Meg,
    ilimit=25 @ u_mV,
    rail=0 @ u_V,
    Vos=0 @ u_V,
    En=0 @ u_V,
    Enk=0 @ u_V,
    In=0 @ u_V,
    Ink=0 @ u_V,
    Rin=500 @ u_Meg,
)

circuit.R("3", "n002", "n005", 22 @ u_kΩ)
circuit.R("4", "n003", "n002", 220 @ u_kΩ)
circuit.R("6", "n008", circuit.gnd, 5 @ u_kΩ)
circuit.R("5", "n001", "n008", 3 @ u_kΩ)
circuit.R("7", "n007", "n004", 100 @ u_Ω)
circuit.D("2", "n001", "n004", model="D")
circuit.BehavioralSource(
    "1",
    "n007",
    circuit.gnd,
    "V",
    expression="table(i(V(n008,n003), (0,0), (1n,3)))",
)
circuit.model("D", "D")

# Setting up the simulation
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=10 @ u_mV, end_time=960 @ u_mV)

# Plotting the result
import matplotlib.pyplot as plt

plt.figure()
plt.plot(analysis["n004"])
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("LED Voltage")
plt.show()
