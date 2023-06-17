"""
David Luby
ME 747
Lab 7 - Python
12-7-2022

this script is for motor constant analysis and frequency response as a
function of controller type (proportional or integral)

"""

# imports
from niScopeRead import scopeRead as sc
import numpy as np
import matplotlib.pyplot as plt
import math

# data intake
names = ['dist', 'i-4', 'i-1', 'p-4', 'p-1', 'pi-4', 'pi-1', 'ol-2', 'ol-5']

dta = []
gain = []
err = []
noise = []
for name in names:
    y = []
    y1 = []
    t = []
    y, y1, t = sc(name+'.csv', 2)
    y = np.array(y) # motor response data
    y1 = np.array(y1) # step input
    t = np.array(t) # time response
    dta.append(t)
    dta.append(y)
    dta.append(y1)
    avgAbs = np.average(np.absolute(y)) # avg of abs val of output
    gain.append(round(avgAbs, 3)) # gain (steady-state response)
    avgAbsIn = np.average(np.absolute(y1)) # avg of abs of input (SS in)
    err.append(round(avgAbsIn-avgAbs, 2)) # error (diff) of avg abs values
    absDiffNoise = np.absolute(np.absolute(y) - avgAbs) # abs val diff noise
    noise.append(round(np.average(absDiffNoise), 4)) # avg abs val diff noise

tIdx = []
tau = []
i = -3
while i < 26:
    i += 3
    if (i == 21) or (i == 24):
        idx  = -1
        for v in dta[i+1]:
            idx += 1
            if (abs(v) > .632*gain[int(i/3)]) and (idx > 1200):
                tIdx.append(idx)
                tau.append(round(dta[i][idx], 6))
                break


title = ['5 $\u03A9$ Load Resistor with 1 mHz, 6 V Input',
        '400 mHz, 4 V Input with Integral Control',
        '1 mHz, 4 V Input with Integral Control and 5 $\u03A9$ Load Resistor',
        '400 mHz, 4 V Input with Proportional Control',
        '1 mHz, 4 V Input with Proportional Control and 5 $\u03A9$ Load Resistor',
        '400 mHz, 4 V Input with Proportional and Integral Control',
        '1 mHz, 4 V Input with Proportional and Integral Control and 5 $\u03A9$ Load Resistor',
        '400 mHz, 4 Volt Step Input', '400 mHz, 5 Volt Step Input']

i = -1
while i < 8:
    i += 1
    k = i*3
    
    
    if i == 0:
        plt.figure(title[i])
        plt.plot(dta[k], dta[k+1], dta[k], dta[k+2], 4*np.average(tau), dta[k+1][30000], 'or')
        plt.title('Open-Loop Motor Response to '+title[i])
        plt.ylabel('Voltage (V)')
        plt.xlabel('Time (s)')
        plt.legend(['Output', 'Input', r'$t_s$'], loc = 'lower right')
        plt.text(dta[k][200], max(dta[k+2]), '$err_{avg, ss} = $'+
                str((err[i]))+' V')
        plt.text(dta[k][200], max(dta[k+2])*.9, '$Noise_{avg} = $'+
                str((noise[i]))+' V')
        plt.text(dta[k][200], max(dta[k+2])*.8, '$t_{s} = $'+
                str((round(4*np.average(tau), 4)))+' s')
    
    
    if i > 6:
        plt.figure(title[i])
        plt.plot(dta[k], dta[k+1], dta[k], dta[k+2], tau[i-7], dta[k+1][tIdx[i-7]], 'o')
        plt.title('Open-Loop Motor Response to '+title[i])
        plt.ylabel('Voltage (V)')
        plt.xlabel('Time (s)')
        plt.legend(['Output', 'Input', r'$f(t = \tau$)'], loc = 'lower right')
        plt.text(dta[k][200], max(dta[k+2]), 'K = '+str((gain[i]))+' V')
        plt.text(dta[k][200], max(dta[k+2])*.9, r'$\tau = $'+str(tau[i-7])+' s')
        plt.text(dta[k][200], max(dta[k+2])*.8, '$err_{avg, ss} = $'+
                str((err[i]))+' V')
        plt.text(dta[k][200], max(dta[k+2])*.7, '$Noise_{avg} = $'+
                str((noise[i]))+' V')


    if 1 <= i <= 6:
        plt.figure(names[i])
        plt.plot(dta[k], dta[k+1], dta[k], dta[k+2])
        plt.title('Closed-Loop Motor Response to '+title[i])
        plt.ylabel('Voltage (V)')
        plt.xlabel('Time (s)')
        plt.legend(['Output', 'Input'], loc = 'lower right')
        plt.text(dta[k][200], max(dta[k+2]), '$err_{avg, ss} = $'+
                str((err[i]))+' V')
        plt.text(dta[k][200], max(dta[k+2])*.9, '$Noise_{avg, ss} = $'+
                str((noise[i]))+' V')

plt.show()