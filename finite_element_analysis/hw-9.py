"""
David Luby
ME 786
HW 9 - python
12-1-2022
"""

import numpy as np
import matplotlib.pyplot as plt

# stress at node c (left to right as divisions increase)
xx = np.array([[471, 476, 510, 585],
                [156, 181, 188, 0],
                [95.0, 111, 116, 0]], dtype=object)

# populating x bins for bar graph
trials = []
for x in range(3):
    trials.append(np.arange(len(xx[x])))

"""
plotting point c data
"""

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# Set position of bar on X axis
br1 = np.arange(len(xx[0]))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

# Make the plot
plt.bar(br1, xx[0], color ='r', width = barWidth,
        edgecolor ='grey', label ='40 cm')
plt.bar(br2, xx[1], color ='g', width = barWidth,
        edgecolor ='grey', label ='60 cm')
plt.bar(br3, xx[2], color ='b', width = barWidth,
        edgecolor ='grey', label ='80 cm')
 
# Adding Xticks
plt.xlabel('Mesh Division Setting', fontweight ='bold', fontsize = 15)
plt.ylabel('Stress (MPa)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(xx[0]))],
        ['10/10','12/12','14/14','20/20'])
plt.title('Horizontal Stress at Point C Against Number of Mesh Divisions for Varied Side Lengths')
plt.legend()
plt.show()

# stress at each node along line ab (left to right/a to b for 10, 12, 14, 20)
yy40 = np.array([[729, 340, 124, -142],
                [734, 329, 106, -157],
                [769, 407, 211, 40.0, -181],
                [844, 593, 434, 296, 170, 51.8, -64.9, -219]], dtype=object)

yy60 = np.array([[365, 195, 139, 97.9, 42.9],
                [394, 244, 185, 144, 112, 80.6, 35.6],
                [403, 258, 199, 159, 128, 99.9, 72.0, 31.7]], dtype=object)

yy80 = np.array([[287, 161, 131, 113, 96.7, 74.0],
                [309, 189, 152, 131, 116, 103, 90.4, 71.1],
                [314, 194, 157, 136, 121, 109, 98.3, 86.6, 69.1]], dtype=object)

x40 = []
x60 = []
x80 = []

# x distance assuming linspace condition
for x in range(4):
    x40.append(np.linspace(12,20,len(yy40[x])))
for x in range(3):
    x60.append(np.linspace(12,30,len(yy60[x])))
    x80.append(np.linspace(12,40,len(yy80[x])))

plt.plot(x40[0], yy40[0], x40[1], yy40[1], x40[1], yy40[1], x40[2], yy40[2], x40[3], yy40[3])
plt.title('Vertical Stress Distribution Along Line AB for Varied Mesh Resolution with 40 cm Side Length')
plt.xlabel('Location on Line AB (cm)\n(Approximate, assuming equally-spaced nodes)')
plt.ylabel('Stress (MPa)')
plt.legend(['10/10','12/12','14/14','20/20'])
plt.show()

plt.plot(x60[0], yy60[0], x60[1], yy60[1], x60[1], yy60[1], x60[2], yy60[2])
plt.title('Vertical Stress Distribution Along Line AB for Varied Mesh Resolution with 60 cm Side Length')
plt.xlabel('Location on Line AB (cm)\n(Approximate, assuming equally-spaced nodes)')
plt.ylabel('Stress (MPa)')
plt.legend(['10/10','12/12','14/14'])
plt.show()

plt.plot(x80[0], yy80[0], x80[1], yy80[1], x80[1], yy80[1], x80[2], yy80[2])
plt.title('Vertical Stress Distribution Along Line AB for Varied Mesh Resolution with 80 cm Side Length')
plt.xlabel('Location on Line AB (cm)\n(Approximate, assuming equally-spaced nodes)')
plt.ylabel('Stress (MPa)')
plt.legend(['10/10','12/12','14/14'])
plt.show()