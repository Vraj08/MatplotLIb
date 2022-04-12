import matplotlib.pyplot as plt

x= [1, 2, 3, 4] # x-axis values

y= [2,4,6,8] # Y-axis values

plt.plot(x,y, 'r', linewidth=4, linestyle='dashed') # first plot with X and Y data

y1 = [3, 5, 7, 9]

plt.plot(x, y1, linewidth=3, linestyle='dashdot') # second plot with x1 and y1 data

plt.xlabel("X-axis ") # Giving Title to x-axis

plt. ylabel("Y-axis ") # Giving Title to y-axis

plt.title ('Multiple Plots on same axis') # Giving Title to Graph

plt.show() # function to show the plot