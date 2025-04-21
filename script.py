import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light (m/s)
f = 2.0e9  # Frequency (Hz)
lambda_ = c / f  # Wavelength (m)
Gt = 1000  # Transmitter antenna gain
Gr = 1000  # Receiver antenna gain

# Transmit power range (100 mW to 1 W in 10 mW steps)
tx_power_mw = np.arange(100, 1001, 10)  # mW
tx_power_w = tx_power_mw / 1000  # Convert to W

# Distances (in km converted to m)
distances_km = [200, 400, 600, 800, 1000]
distances_m = np.array(distances_km) * 1000

# Calculate received power for each distance
received_power = []
for d in distances_m:
    Pr = tx_power_w * Gt * Gr * (lambda_ / (4 * np.pi * d))**2
    received_power.append(Pr)

# Plotting
plt.figure(figsize=(10, 6))
for i, d in enumerate(distances_km):
    plt.plot(tx_power_mw, 10 * np.log10(received_power[i]), label=f'Distance = {d} km')

# Adding labels and legend
plt.title("Received Power vs Transmit Power using Friis Transmission Equation")
plt.xlabel("Transmit Power (mW)")
plt.ylabel("Received Power (dBm)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

