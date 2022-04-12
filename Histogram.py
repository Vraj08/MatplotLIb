import matplotlib.pyplot as plt # importing matplotlib module
import numpy as np # importing numpy module
x = np.random.normal(170, 10, 250)#Draw random samples from a normal (Gaussian) distribution.
plt.hist(x)# Function to plot
plt.title ("HISTOGRAM") # Giving Title to Graph
plt.xlabel('X-axis') # Giving Title to x-axis
plt.ylabel('Y-axis')# Giving Title to y-axi
plt.show()  # function to show the plot