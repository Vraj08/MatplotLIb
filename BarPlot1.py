# importing matplotlib module

from matplotlib import pyplot as plt

plt.title ("Bar graph") # Giving Title to Graph

plt.xlabel('X-axis') # Giving Title to x-axis

plt. ylabel('Y-axis') # Giving Title to y-axis

x = [8, 24, 34, 48, 88] # x-axis values

y= [44, 84, 34, 40, 80] # Y-axis values

plt.bar(x, y) # Function to plot

plt. show() # function to show the plot