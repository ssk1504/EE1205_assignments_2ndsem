import numpy as np

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

num = 0.2499

# Define parameters for transformation
B = 0.1331
Omega0 = 0.8312

# Perform transformation to get s_L
s_L = (1j * 0.7673)**2 + Omega0**2
s_L /= B * (1j * 0.7673)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
