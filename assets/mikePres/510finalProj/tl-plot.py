#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

# Load CSV data
df = pd.read_csv('./imag/510-muffler-TL-20degC.csv')

# Extract frequency and TL columns
frequencies = df.iloc[:, 0]
transmission_loss = df.iloc[:, 1]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies, transmission_loss, color='darkblue', linewidth=2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Transmission Loss (dB) at 20°C')
plt.title('Muffler Transmission Loss vs Frequency at 20°C')
plt.grid(True)
plt.tight_layout()
#plt.show()
plt.savefig('muffler_TL_20degC.png', dpi=300)
