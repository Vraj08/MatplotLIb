import matplotlib.pyplot as plt

x= [1, 2, 3, 4] # x-axis values

y= [2,4,6,8] # Y-axis values

plt.plot(x, y) # first plot with X and Y data

y1 = [3, 5, 7, 9]

plt.plot(x, y1) # second plot with x1 and u1 data

plt.fill_between(x, y, y1, color='black')

plt.xlabel("X-axis ") # Giving Title to x-axis

plt.ylabel("Y-axis ") # Giving Title to y-axis

plt.title ('Multiple Plots on same axis') # Giving Title to Graph

plt. show() # function to show the plot