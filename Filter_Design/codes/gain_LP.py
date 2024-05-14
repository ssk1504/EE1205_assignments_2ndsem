import numpy as np

# Given parameters
s1 = -0.1411 - 0.9847j
s2 = -0.3407 - 0.4079j
s3 = -0.3407 + 0.4079j
s4 = -0.1411 + 0.9847j
epsilon = 0.5
Omega_Lp = 1

# Generate the denominator polynomial
den = np.poly([s1, s2, s3, s4])
num = np.array([1])
s = 1j*1  # use Omega = 1
H = num / np.polyval(den, s)

req = 1 / np.sqrt(1 + epsilon**2)

Gain_LP = req / abs(H)
print(Gain_LP)
