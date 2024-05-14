import numpy as np
import matplotlib.pyplot as plt

# Define time variable
t = np.linspace(0, 0.006, 1000)  # Time from 0 to 0.01 seconds

# Carrier signal
fc = 10**6  # Carrier frequency
Ac = 2  # Carrier amplitude
carrier_signal = Ac * np.cos(2 * np.pi * fc * t)

# Message signal
fm = 10**3  # Message frequency
Am = 4 * np.sqrt(2)  # Message amplitude
message_signal = Am * np.sin(2 * np.pi * fm * t)

# Plotting
plt.plot(t, carrier_signal, label='Carrier Signal (c(t))', color='blue')
plt.plot(t, message_signal, label='Message Signal (m(t))', color='red')
plt.title('')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()

