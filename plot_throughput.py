import pandas as pd
import matplotlib.pyplot as plt

# Load extracted dataset
df = pd.read_csv('throughput_data.csv', sep=' ', names=['Time_s', 'Total_Bytes'])

# Convert Total Bytes to Megabits
df['Total_Mb'] = (df['Total_Bytes'] * 8) / 1e6

# Calculate instantaneous throughput per step (Mbps)
df['Time_Diff'] = df['Time_s'].diff()
df['Byte_Diff'] = df['Total_Bytes'].diff()
df['Instant_Mbps'] = (df['Byte_Diff'] * 8) / (df['Time_Diff'] * 1e6)

# Generate plot
plt.figure(figsize=(10, 5))
plt.plot(df['Time_s'], df['Instant_Mbps'], color='#1f77b4', linewidth=1.5, label='Instantaneous Throughput')
plt.axhline(y=15.99, color='r', linestyle='--', label='Average Throughput (~16.0 Mbps)')

plt.title('ns-3 mmWave Simulation: Receiver Throughput vs Time', fontsize=12)
plt.xlabel('Simulation Time (s)', fontsize=10)
plt.ylabel('Throughput (Mbps)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig('throughput_plot.png', dpi=300)
print("Plot successfully saved as throughput_plot.png")
