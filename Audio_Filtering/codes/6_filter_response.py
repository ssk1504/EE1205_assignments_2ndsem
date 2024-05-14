import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Step 1: Read the audio file
fs, data = wav.read("keyboard.wav")

# Step 2: Compute the one-sided Fourier transform
n = len(data)
frequencies = np.fft.fftfreq(n, d=1/fs)
spectrum = np.fft.fft(data)
spectrum_magnitude = np.abs(spectrum)
positive_frequencies = frequencies[:n//2]  # Take only the positive frequencies
positive_spectrum_magnitude = spectrum_magnitude[:n//2]  # Corresponding spectrum magnitude

# Step 3: Plot the frequency response
plt.plot(positive_frequencies, positive_spectrum_magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('|H(exp(jω))|')
plt.title('Frequency Response of "keyboard.wav"')
plt.grid(True)
plt.show()

