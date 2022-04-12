import matplotlib.pyplot as plt

x= [8, 24, 34, 48, 88] #x-axis values

y= [44, 84, 34, 40, 80] # Y-axis values

plt.plot(x, y) # first plot with X and Y data

x1 = [24, 34, 36, 68]

y1 = [34, 54, 74, 79]

plt. plot(x1, y1) # second plot with x1 and y1 data

plt. xlabel("X-axis ") # Giving Title to x-axis

plt.ylabel("Y-axis") # Giving Title to y-axis

plt. title('Multiple Plots on same axis') # Giving Title to Graph

plt. show() # function to show the plot