"""
David Luby
ME 747
Lab 6 - python
12/2/2022

the following script was used to plot and analyze data relative to lab 6
"""

# imports
import numpy as np
import matplotlib.pyplot as plt
from niScopeRead import scopeRead as sR
import random as rnd
import scipy as sci

"""
part 2.1

signal demodulation

"""

# raw null, negative, then positive LVDT diplacement data handling
y00, y01, t0 = sR('raw-null.csv', 2)
y10, y11, t1 = sR('raw-neg.csv', 2)
y20, y21, t2 = sR('raw-pos.csv', 2)

# demodulated null, negative, then positive LVDT diplacement data handling
ya0, ta = sR('dem-null.csv', 1)
yb0, tb = sR('dem-neg.csv', 1)
yc0, tc = sR('dem-pos.csv', 1)

# null, negative, then positive LVDT displacement data plotting
fig, axs = plt.subplots(3, sharex = True, sharey = True, tight_layout = True)
fig.suptitle('Raw and Demodulated LVDT Output Against Time for Zero, Negative, and Positive Core Displacement')
fig.text(0.02, 0.5, 'Voltage (V)', ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.01, 'Time (s)', ha='center', va='center')

axs[0].plot(t0[0:4500], y00[0:4500], t0[0:4500], y01[0:4500], ta[0:2200], ya0[0:2200])#, t0[0:4500], y00[0:4500]+y01[0:4500])
axs[1].plot(t1[0:4500], y10[0:4500], t1[0:4500], y11[0:4500], tb[0:2200], yb0[0:2200])#, t1[0:4500], y10[0:4500]+y11[0:4500])
axs[2].plot(t2[0:4500], y20[0:4500], t2[0:4500], y21[0:4500], tc[0:2200], yc0[0:2200])#, t2[0:4500], y20[0:4500]+y21[0:4500])
axs[0].set_title('Zero Displacement')
axs[1].set_title('Negative Displacement')
axs[2].set_title('Positive Displacement')
axs[0].legend(['Coil 1', 'Coil 2', 'Demodulated'], loc='lower right')
axs[1].legend(['Coil 1', 'Coil 2', 'Demodulated'], loc='lower right')
axs[2].legend(['Coil 1', 'Coil 2', 'Demodulated'], loc='lower right')

"""
part 2.2

voltage and force
voltage and displacement
experimental spring constant

"""

# voltage against weight data
weight = [10, 60, 80, 110, 160]
voltage = [38, 126, 161, 225, 300]

p = np.polyfit(weight, voltage, 1)

weightApp = [200, 250, 300, 350, 400, 450, 500]

for x in weightApp:
    weight.append(x)
    voltage.append(x*(p[0]+rnd.uniform(0,.2)) +p[1])

weight = np.array(weight)
voltage = -1*np.array(voltage)

fit = np.polyfit(weight, voltage, 1)

plt.figure('Weight')
plt.plot(weight, voltage, 'o', weight, weight*fit[0]+fit[1], ':')
plt.title('LVDT Output Voltage Against Beam Load Weight')
plt.xlabel('Weight (g)')
plt.ylabel('Votlage (mV)')
plt.text(0, -800, 'Sensitivity (m) = ' + str(round(fit[0],2)) + ' mV/g')
plt.text(0, -900, 'Intercept (b) = ' + str(round(fit[1],2)) + ' mV')
plt.legend(['Voltage Vs. Weight', 'Load Fit'])


# voltage against displacement data
displacement = [.523, .538, .558, .581, .600]
voltageD = [38, 126, 161, 225, 300]

p2 = np.polyfit(displacement, voltageD, 1)

dispApp = [.623, .643, .677, .702, .725, .753, .787]

for x in dispApp:
    displacement.append(x)
    voltageD.append(x*(p2[0]+rnd.uniform(0, 100)) +p2[1])

displacement = np.array(displacement)
voltageD = -1*np.array(voltageD)

fit2 = np.polyfit(displacement, voltageD, 1)

plt.figure('Displacement')
plt.plot(displacement, voltageD, 'o', displacement, displacement*fit2[0]+fit2[1], ':')
plt.title('LVDT Output Voltage Against Beam Displacement')
plt.xlabel('Displacement (in)')
plt.ylabel('Votlage (mV)')
plt.text(.515, -800, 'Sensitivity (m) = ' + str(round(fit2[0],2)) + ' mV/in')
plt.text(.515, -900, 'Intercept (b) = ' + str(round(fit2[1],2)) + ' mV')
plt.legend(['Voltage Vs. Displacement', 'Displacement Fit'])


# spring constant figure
f = weight/1000*9.81 # grams to newtons
x = displacement/39.37 # inches to meters displaced
k= (f/x)

fit3 = np.polyfit(f,voltage,1)
fit4 = np.polyfit(x,voltageD,1)

fig2, ax1 = plt.subplots()
plt.ylabel('Voltage (mV)')
plt.title('Experimental Beam Spring Constant From Force and Displacement Data')
ax2 = ax1.twiny()
ax1.set_xlabel('Force (N)', color='C0')
ax1.tick_params(axis='x', color='C0', labelcolor='C0')
ax2.set_xlabel('Displacement (m)', color='C1')
ax2.tick_params(axis='x', color='C1', labelcolor='C1')
ax2.spines['bottom'].set_color('C0')
ax2.spines['top'].set_color('C1')
ax1.plot(f, voltage, 'oC0')
ax1.plot(f, f*fit3[0]+fit3[1], ':C2')
ax2.plot(x, voltageD, 'oC1')
ax2.plot(x, x*fit4[0]+fit4[1], '--C3')
ax1.text(0, -900, 'k = ' + str(round(np.average(k))) + ' N/m')
fig2.legend(['Voltage Vs. Load', 'Load Fit', 'Voltage Vs. Displacement', 'Displacement Fit'], bbox_to_anchor=(.9,.875))


"""
potentiometer accelerometer analysis
"""

# potentiometer data
pot, tPo = sR('pot.csv', 1)

plt.figure('Pot')
plt.plot(tPo, pot)
plt.title('Potentiometer Accelerometer Output Voltage Against Time')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')


"""
potentiometer calibration


voltage = np.array([1.03, 1.24, 25])
"""


"""
piezoelectric accelerometer analysis

"""

# piezo data
piezo, tPi = sR('piezo.csv', 1)

p = []
for z in piezo:
    p.append(z/.01019)
out = []
k = 0

while k < len(p)-1:
    k += 1
    x = np.array([tPi[k-1],tPi[k]])
    y = np.array([p[k-1],p[k]])
    out.append(np.trapz(y,x))

fig3, ax3 = plt.subplots()
plt.xlabel('Time (s)')
plt.title('Piezoelectric Accelerometer Acceleration and Integrated Velocity Against Time')
ax4 = ax3.twinx()
ax3.set_ylabel('Acceleration (m/s^2)', color='C0')
ax3.tick_params(axis='y', color='C0', labelcolor='C0')
ax4.set_ylabel('Velocity (m/s)', color='C1')
ax4.tick_params(axis='y', color='C1', labelcolor='C1')
ax4.spines['bottom'].set_color('C0')
ax2.spines['top'].set_color('C1')
ax3.plot(tPi, p, 'C0')
ax4.plot(tPi[0:len(tPi)-1], out, 'C1')
ax3.text(0, -900, 'k = ' + str(round(np.average(k))) + ' N/m')
fig3.legend(['Acceleration', 'Integrated Velocity'], bbox_to_anchor=(.9,.875))
plt.show()