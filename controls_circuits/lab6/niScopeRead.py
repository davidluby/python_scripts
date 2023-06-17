"""
this script can be called to import csv data from an ni oscilloscope

it accepts a string input corresponding to the name of the csv file
it accepts an integer input corresponding to the number of columns

it outputs two waveforms and a time vector
"""

import numpy as np

def scopeRead(fileName, cols):

    file = open(fileName)
    i = -1
    y0 = [] # first output
    t = [] # time

    # one-column csv handler
    if cols == 1:
        for lines in file:
            i += 1
            if i == 2:
                dontCare, dontC, interval, count = lines.split(',')
                time = 0
            if i > 7:
                a = lines.strip('')
                y0.append(float(a))
                time = time + float(interval)
                t.append(time)
        file.close()
        return(np.array(y0), np.array(t))

    # two-column csv handler
    if cols == 2:
        y1 = [] # second output
        for lines in file:
            i += 1
            if i == 2:
                dontCare, dontC, interval, count = lines.split(',')
                time = 0
            if i > 7:
                a,b = lines.split(',')
                y0.append(float(a))
                y1.append(float(b))
                time = time + float(interval)
                t.append(time)
        file.close()
        return(np.array(y0), np.array(y1), np.array(t))