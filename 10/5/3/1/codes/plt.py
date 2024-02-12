import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat file
data = np.loadtxt('ap_data.dat', skiprows=1)  # Skip the header row

# Separate the columns into n_values and y_values
n_values = data[:, 0]
y_values = data[:, 1]

# Plot the data as a stem plot
plt.stem(n_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.show()

