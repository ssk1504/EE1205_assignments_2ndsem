import numpy as np
import matplotlib.pyplot as plt

# Given parameters
s1 = -0.1411 - 0.9847j
s2 = -0.3407 - 0.4079j
s3 = -0.3407 + 0.4079j
s4 = -0.1411 + 0.9847j
epsilon = 0.5
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

G_LP = 0.2499
num = G_LP

Omega_p1 = 0.7673
Omega_p2 = 0.9004

Omega_s1 = 0.7366
Omega_s2 = 0.9366

# Define parameters for transformation
B = 0.1331
Omega0 = 0.8312

# Perform transformation to get s_L
s_L = (1j * w)**2 + Omega0**2
s_L = s_L / (B * (1j * w))

# Band pass gain
G_bp = 1.1187

# Substitute s = jw into H(s)
H = G_bp * (num / np.polyval(den, s_L))

# Plot magnitude response for H(s)
plt.figure()
plt.plot(w, abs(H), linewidth=1)
plt.title('Band Pass Filter')
plt.xlabel('Analog Frequency ($\Omega$)')
plt.ylabel('|H_{a,BP}($\Omega$)|')
plt.grid(True)
plt.ylim(0, 1.2)
plt.savefig("Band_Pass_Filter.png")
