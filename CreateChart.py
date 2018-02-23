import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()


# Open and read the csv file
reader = csv.DictReader(open('MR18_UTS_data.csv'))

dict_list = []
rowcount = 0

# Add to dictionary list
for line in reader:
        dict_list.append(line)
        rowcount += 1

# Retrieve required data


# Get 4 best average test
# Add to temporary dictionary

# Insert Data to plot: radio type = (forth person, third person, second person, first person)

radio1data = (0, 8, 0, 18)
radio2data = (0, 0, 11, 0)
radio3data = (0, 0, 0, 18)
radio4data = (8, 0, 11, 0)

# Create plot
fig, ax = plt.subplots()
index = np.arange(4)
bar_width = 0.15
opacity = 0.8

# Bar setup(radios)
radio1 = plt.barh(index + bar_width*0, radio1data, bar_width, alpha=opacity, color='r', label='Aragon(arm)')
radio2 = plt.barh(index + bar_width*1, radio2data, bar_width, alpha=opacity, color='g', label='Aragon(dsp)')
radio3 = plt.barh(index + bar_width*2, radio3data, bar_width, alpha=opacity, color='b', label='Frodo(arm)')
radio4 = plt.barh(index + bar_width*3, radio4data, bar_width, alpha=opacity, color='y', label='Frodo(dsp)')

# Labels
plt.xlabel('Number of Test Cases')
plt.ylabel('Person')
plt.title('Test Case Ranking')

# Insert ID and name here
plt.yticks(index + bar_width, ('Kartigesan Chandran', 'See Wen Xing', 'Ooi Song Qiang', 'Chong Woon Jiet'))
plt.legend()

plt.tight_layout()
plt.show()