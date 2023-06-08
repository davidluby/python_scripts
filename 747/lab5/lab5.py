"""
David Luby
ME 747
Lab 5 Plots and Calculations
11-14-2022
"""

import matplotlib.pyplot as plt
import math
import scipy
import numpy as np

tCal = 7*60/(1000*2*math.pi) # tachometer output (V*s/rad)
pCal = .015*180/math.pi # potentiometer output (V/rad)


Ri = 10.02e3
Rf = 0.99e6
R = 10.04e3
C = 10e-6

gain1 = -Ri*C
gain2 = -Rf/Ri

file = open('Instrument Capture 2022-11-01 16-32-30 Oscilloscope - Waveform Data.csv')
i = -1
wT = [] # tachometer output (omega)
tO = [] # op amp output (theta)
t = [] # time
for lines in file:
    i += 1
    if i == 2:
        null, dontcare, interval, count = lines.split(',')
        time = 0
    if i > 10000:
        a,b = lines.split(',')
        wT.append(float(a)/tCal)
        tO.append(float(b)*gain2*math.pi/180)
        time = time + float(interval)
        t.append(time)
file.close()

fig, ax1 = plt.subplots()
ax1.plot(t, wT)
plt.title('Angular Velocity from Tachometer and Integrated Angular Displacement Against Time')
plt.xlabel('Time (s)')
ax1.set_ylabel('Angular Velocity (rad/s)', color='C0')
ax1.tick_params(axis='y', color='C0', labelcolor='C0')
ax2 = ax1.twinx()
ax2.plot(t, tO, 'C1')
ax2.set_ylabel('Angular Displacement (rad)', color='C1')
ax2.tick_params(axis='y', color='C1', labelcolor='C1')
ax2.spines['left'].set_color('C0')
ax2.spines['right'].set_color('C1')
fig.legend(['$\omega_{tach}$', r'$\theta_{int,c}$'], bbox_to_anchor=(.9,.875))
plt.xlim([0, 1])
plt.show()

file = open('Instrument Capture 2022-11-01 14-38-10 Oscilloscope - Waveform Data.csv')
i = -1
tP = [] # potentiometer output (theta)
tO2 = [] # other op amp output
t2 = [] # time
for lines in file:
    i += 1
    if i == 2:
        null, dontcare, interval, count = lines.split(',')
        time = 0
    if i > 27500:
        a,b = lines.split(',')
        tP.append(float(a)/pCal)
        tO2.append(float(b)*gain1*math.pi/180)
        time = time + float(interval)
        t2.append(time)
file.close()

plt.plot(t2, tP, t, tO)
plt.legend([r'$\theta_{pot}$',r'$\theta_{int,c}$'])
plt.title('Angular Displacement from Potentiometer and Integrated Angular Displacement Against Time')
plt.ylabel('Angular Displacement (rad)')
plt.xlabel('Time (s)')
plt.show()


"""
plt.plot(t,tO,t2,tO2)
plt.show()
"""

fig, ax1 = plt.subplots()
ax1.plot(t, tO)
plt.title('Comparison of Integrated Angular Displacement with and without Drift Compensation Against Time')
plt.xlabel('Time (s)')
ax1.set_ylabel('Angular Displacement (rad)', color='C0')
ax1.tick_params(axis='y', color='C0', labelcolor='C0')
ax2 = ax1.twinx()
ax2.plot(t2, tO2, 'C1')
ax2.set_ylabel('Angular Displacement (rad)', color='C1')
ax2.tick_params(axis='y', color='C1', labelcolor='C1')
ax2.spines['left'].set_color('C0')
ax2.spines['right'].set_color('C1')
fig.legend([r'$\theta_{int,c}$', r'$\theta_{int}$'], bbox_to_anchor=(.9,.875))
plt.xlim([0, 1])
plt.show()

# integrating wtach

w = np.array(wT)
t = np.array(t)
k = 0
tPy = [] # theta from integrating discrete data omega tach
for y in w:
    k += 1
    if k < 90006:
        tNew = np.array([t[k-1],t[k]])
        wNew = np.array([w[k-1],w[k]])*gain2*100
        tPy.append(np.trapz(wNew,tNew))

fig, ax1 = plt.subplots()
ax1.plot(t, wT)
plt.title('Angular Velocity from Tachometer and Analytically Integrated Angular Displacement Against Time')
plt.xlabel('Time (s)')
ax1.set_ylabel('Angular Velocity (rad/s)', color='C0')
ax1.tick_params(axis='y', color='C0', labelcolor='C0')
ax2 = ax1.twinx()
ax2.plot(t[0:90005], tPy, 'C1')
ax2.set_ylabel('Angular Displacement (rad)', color='C1')
ax2.tick_params(axis='y', color='C1', labelcolor='C1')
ax2.spines['left'].set_color('C0')
ax2.spines['right'].set_color('C1')
fig.legend(['$\omega_{tach}$', r'$\theta_{int,Python}$'], bbox_to_anchor=(.9,.875))
plt.xlim([0, 1])
plt.show()

plt.plot(t,tO,t2,tP,t[0:90005], tPy)
plt.title('Experimental and Analytical Integrated Angular Displacement with and without Drift Compensation Against Time')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.xlim([0,1])
plt.legend([r'$\theta_{int,c}$', r'$\theta_{pot}$', r'$\theta_{int,Python}$'], bbox_to_anchor=(.9,.875))
plt.show()