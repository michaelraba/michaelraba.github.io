#!/usr/bin/env python3.10

import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the CSV data
file_path = "/home/mi/onedrive/multiChamberMuffler/M3dat.csv"
df = pd.read_csv(file_path, skiprows=10)
df.columns = ["Frequency (Hz)", "Transmission Loss (dB)"]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df["Frequency (Hz)"], df["Transmission Loss (dB)"], marker="o")
plt.title("Transmission Loss vs Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Transmission Loss (dB)")
plt.grid(True)
plt.tight_layout()
plt.savefig("muffler_TL_20degC.svg")
