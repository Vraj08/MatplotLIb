import matplotlib.pyplot as plt

StudentName = ['Vraj', 'Vishwa', 'Vansh', 'Siya'] #x-axis values

TotalMarks = [200,300,500,400] #Y-axis values

plt. barh (StudentName, TotalMarks, color=['r','b','g','orange'])

# Plotting graph with same width but diff colors by qiving the color

#sequence as list in the argument

plt. xlabel ("StudentName") # Giving Title to x-axis

plt. ylabel ("TotalMarks") # Givina Title to u-axis

plt. title('Horizontal Bar Plot') # Giving Title to Graph

plt.show() # function to show the olot