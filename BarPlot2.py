import matplotlib.pyplot as plt

StudentName = ['Vraj',"Vishwa","Vansh",'Siya'] # x-axis values

TotalMarks = [200,300,500,400] # Y-axis values

plt. bar (StudentName, TotalMarks, color=['r', 'b', 'g', 'orange' ])

# Plotting graph with same width but diff colors by giving the color

#sequence as list in the arqument

plt. xlabel ("StudentName") # Giving Title to x-axis

plt. ylabel("TotalMarks") # Giving Title to y-axis

plt. title ('Bar Plot With Same Width But Different Colors') # Giving Title to Graph

plt. show() # function to show the plot