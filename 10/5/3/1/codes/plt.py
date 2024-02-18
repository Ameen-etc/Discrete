import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat files
data_ap = np.loadtxt('ap4_data.dat', skiprows=1)  # Skip the header row
data_sum = np.loadtxt('ap4_sum.dat', skiprows=1)

# Separate the columns into n_values and y_values for AP data
n_values_ap = data_ap[:, 0]
y_values_ap = data_ap[:, 1]

# Separate the columns into n_values and y_values for sum data
n_values_sum = data_sum[:, 0]
y_values_sum = data_sum[:, 1]

# Create a subplot with stem plots
fig, axs = plt.subplots(1, 2, figsize=(8, 8))

# Plot AP data
axs[0].stem(n_values_ap, y_values_ap, linefmt='c-', markerfmt='co', basefmt='k-')
axs[0].set_xlabel('n')
axs[0].set_ylabel('x(n)')

# Plot sum data
axs[1].stem(n_values_sum, y_values_sum, linefmt='b-', markerfmt='bo', basefmt='k-')
axs[1].scatter(n_values_sum[-1], y_values_sum[-1], color='red', zorder=3)
axs[1].set_xlabel('n')
axs[1].set_ylabel('y(n)')

plt.tight_layout()
plt.show()


