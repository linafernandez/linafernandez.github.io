'''
Project: 3.2.7
Partners: Tyler Batistic, Lina Fernandez
Purpose: Create a histogram of bans from the game Counter-Strike: Global Offensive, to see how players' anti-cheating methods caused spikes in the amounts of bans.
'''
#Import Libraries
import os.path
import matplotlib.pyplot as plt

# Get the date/ban data from CSV
#Data comes from vac-ban.com/#chart
directory = os.path.dirname(os.path.abspath(__file__))
datafile = open(directory + '\\Ban_Data.csv','r')
data = datafile.readlines()

#Create empty lists for dates and bans
bans=[]
dates = []
day = 0

#Loop to add ban number and day number to lists to be plotted
for line in data[1:]:
    date, ban = line.split(',')
    bans.append(int(ban))
    day += 1
    dates.append(day)

#Plot a graph with date as the x and amount of bansbans as the y
fig, ax = plt.subplots(1, 1)
ax.set_title('CS:GO Bans In 2016')
ax.plot(dates, bans, color='#7a42f5')
ax.set_xlabel('Days')
ax.set_ylabel('Amount of Bans')
ax.set_axis_bgcolor('#a5a5a5')
fig.show()