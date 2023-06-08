"""
David Luby
ME 747
Lab 4 - Plotting and Computation
11/1/2022
"""

# importing packages
import numpy as np
import matplotlib.pyplot as plt

def readData(csv):
    i = -1
    data = []
    file = open(csv) # open csv file
    for line in file: # iterate through csv
        i += 1
        if i == 2:
            void, tStart, tStep, count = line.split(',') # parse time line
            start = float(tStart) - float(tStart)
            step = float(tStep)
            stop = (step*float(count))
            t = np.arange(start, stop, step) # create time data list
        elif i > 5:
            data.append(-1*float(line.strip())) # append voltage data to data list
    file.close()
    return(np.array(data), t)


# calling function for 5 and 2.5 volt data
fiveV, fiveT = readData('Instrument Capture 2022-10-25 16-30-51 Oscilloscope - Waveform Data.csv')
twoV, twoT = readData('Instrument Capture 2022-10-25 16-21-11 Oscilloscope - Waveform Data.csv')

# plotting both data sets
plt.plot(twoT[0:len(twoT)-1250], twoV[1250::], fiveT[0:len(fiveT)-13500], fiveV[13500::])
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.xlim([0,2.25])
plt.title('Summer Output Voltage for 2.5-5 and 5-10 Volt Square Wave Inputs')
plt.legend(['2.5-5 Volts', '5-10 Volts'], loc = 'lower right')
plt.show()
