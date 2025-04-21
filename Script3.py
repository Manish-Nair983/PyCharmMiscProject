import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_ = 500e-9  # Wavelength (m)
w0 = 1e-3  # Beam waist (m)
z_values = np.linspace(0, 10, 500)  # Propagation distance (m)
r_values = np.linspace(0, 3 * w0, 500)  # Radial positions (m)
zR = np.pi * w0**2 / lambda_  # Rayleigh range

# Calculate beam radius w(z)
w_z = w0 * np.sqrt(1 + (z_values / zR)**2)

# Calculate intensity profile I(r, z) at a specific distance z (e.g., z = 5 m)
z_specific = 5  # Distance (m)
w_at_z = w0 * np.sqrt(1 + (z_specific / zR)**2)
I_0 = 1  # Assume normalized peak intensity
I_r = I_0 * np.exp(-2 * (r_values**2) / w_at_z**2)

# Plotting the beam radius over distance
plt.figure(figsize=(12, 6))
plt.plot(z_values, w_z * 1e3, label="Beam Radius (w(z))")
plt.axvline(zR, color="r", linestyle="--", label="Rayleigh Range")
plt.title("Beam Radius vs Propagation Distance (Gaussian Beam)")
plt.xlabel("Propagation Distance z (m)")
plt.ylabel("Beam Radius w(z) (mm)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()

# Plotting the intensity profile
plt.figure(figsize=(12, 6))
plt.plot(r_values * 1e3, I_r, label=f"Intensity Profile at z = {z_specific} m")
plt.title("Intensity Profile of Gaussian Beam")
plt.xlabel("Radial Position r (mm)")
plt.ylabel("Normalized Intensity I(r)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()
