import matplotlib.pyplot as plt

IT= [12,4,8,7]

CE = [14,8,10,8]

CSE=[13,3,9,6]

xaxis=[i for i in range(len(IT))]

xaxis1=[i+ 0.25 for i in range(len(xaxis))]

xaxis2=[i+ 0.50 for i in range(len(xaxis1))]

plt. bar(xaxis, IT, color='b' ,width = 0.25, label="IT")

plt. bar (xaxis1, CE, color='r' ,width = 0.25, label="CE")

plt. bar(xaxis2, CSE, color='g', width = 0.25, label="CSE")

plt. ylabel("NO. of Students") # Giving Title to x-axis

plt.xlabel("Year") # Giving Title to y-axis

plt. title(' Multiple Bar Plots With Legends') # Giving Title to Graph

plt. legend (loc='upper right')

#you can also store line 8 9 10 as bar1=, bar2=, bar3=

#and then use below mentioned method for legend

#plt.legend( (bar1, bar2, bar3), ('IT', 'CE', 'CSE') )

plt. xticks(xaxis, [2019,2020, 2021, 2022])

plt. show() # function to show the plot