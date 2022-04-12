import matplotlib.pyplot as plt

StudentName = ['Vraj','Vishwa',"Vansh",'Siya'] # x-axis values

TotalMarks = [200,300,500,400] #Y-axis values

plt. bar (StudentName, TotalMarks, color='b',width=[0.8,0.6,0.5,0.7])

## Plotting graph with same color but diff widths by giving the width

#sequence as list in the arqument

plt. xlabel("StudentName") # Giving Title to x-axis

plt. ylabel("TotalMarks") # Giving Title to y-axis

plt. title ('Bar Plot With Same Color But Different Widths') # Giving Title to Graph

plt. show() # function to show the plot