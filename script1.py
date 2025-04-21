import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Constants
c = 3e8  # Speed of light (m/s)
f = 2.0e9  # Frequency (Hz)
lambda_ = c / f  # Wavelength (m)
Gt = 1000  # Transmitter antenna gain
Gr = 1000  # Receiver antenna gain

# Parameters
tx_power_w = 200 / 1000  # Transmit power: 200 mW converted to Watts
distances_km = [200, 400, 600, 800, 1000]  # Distances in kilometers
distances_m = np.array(distances_km) * 1000  # Convert distances to meters
snr_db = np.arange(-2, 8, 1)  # SNR range in dB
snr_linear = 10 ** (snr_db / 10)  # Convert SNR from dB to linear scale

# BER computation
ber_results_separated_fixed = []  # Store BER arrays for each distance

# Loop through each distance to calculate and store BER
for d in distances_m:
    Pr = tx_power_w * Gt * Gr * (lambda_ / (4 * np.pi * d))**2  # Received power
    ber_distance = []  # Store BERs for this distance
    for snr in snr_linear:
        noise_power = Pr / snr  # Noise power for this SNR
        eb_n0 = Pr / noise_power  # Calculate Eb/N0
        ber = 0.5 * erfc(np.sqrt(eb_n0))  # Compute BER using Q-function
        ber_distance.append(ber)  # Append BER for this SNR
        ber_results_separated_fixed.append(ber_distance)  # Add BER array for this distance

# Plotting the BER vs SNR
plt.figure(figsize=(10, 6))
for i, d in enumerate(distances_km):
    plt.semilogy(snr_db, ber_results_separated_fixed[i], label=f'Distance = {d} km')  # label

# Adding labels, grid, and legend
plt.title("BER vs SNR for OOK Modulation")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.show()
