# Author: Mayank Kumar Pokhriyal
# Date: 27th Feb 2025
# Description: This program generates and plots random hourly temperatures for three cities (Delhi, Mumbai, Bangalore)
#              over a 12-hour period.

import matplotlib.pyplot as plt
import random

# Create the time list for x-axis
time = list(range(1, 13))

# Define the city names
cities = ['Delhi', 'Mumbai', 'Bangalore']

# Generate and plot temperature data for each city
for city in cities:
    temperatures = [random.randint(10, 30) for _ in range(12)]
    plt.plot(time, temperatures)

# Add graph title and labels
plt.title("Hourly Temperatures in Three Cities")
plt.xlabel("Hours")
plt.ylabel("Temperature (°C)")

# Add legend with city names in the order plotted
plt.legend(cities)

# Display the graph
plt.show()