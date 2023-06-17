# this script prepares and plots stress-strain curves

# import packages
import numpy as np
import matplotlib.pyplot as plt
from stressStrain import MYU

# open/read uniaxial tension data
file = open('HW1-Prob2.csv', 'r')
i = 0 # counter to ignore first line
ext = [] # intialize extension vector (mm)
f = [] # initialize force vector (N)

for line in file: # read each line
    i +=1 # add one to i
    if i == 1: # ignore first entry
        pass
    else: # append data to extensiona and force vectors
        x, y = line.split(',')
        ext.append(float(x))
        f.append(float(y))

# convert lists to array data type
ext = np.array(ext)
f = np.array(f)

file.close()

# input problem givens
l = 50 # initial length (mm)
t = 3.19 # initial thickness (mm)
w = 12.55 # initial width (mm)
A = t*w # initial cross sectional area

# engineering stress-strain is with reference to initial area
eStress = f/A # scalar division by initial area
eStrain = ext/l # scalar division by initial length

# true stress-strain is with reference to changing area
tStress = eStress*(1+eStrain) # element-wise eStress * (1 + eStrain)
tStrain = np.log(1+eStrain) # element-wise ln(1 + eStrain)

# plotting engineering
m,y,u = MYU(eStrain,eStress,4,.1)

plt.plot(eStrain, eStress, eStrain[y], eStress[y], 'o', eStrain[u],eStress[u],
 'o')
plt.xlabel('Engineering Strain')
plt.ylabel('Engineering Stress (MPa)')
plt.title('Engineering Stress Against Engineering Strain')
plt.text(.25, 70, '$E$ = ' + str(round(m,2)) + ' $GPa$')
plt.text(.25, 50, r'$\sigma_{ys}$ = ' + str(round(eStress[y],2)) + ' $MPa$')
plt.text(.25, 30, r'$\sigma_{ut}$ = ' + str(round(eStress[u],2)) + ' $MPa$')
plt.text(.25, 10, r'$\epsilon_{ut}$ = ' + str(round(eStrain[u],2)))
plt.show()

# plotting true
m,y,u = MYU(tStrain,tStress,4,.1)

plt.plot(tStrain, tStress, tStrain[y], tStress[y], 'o', tStrain[u],tStress[u],
 'o')
plt.xlabel('True Strain')
plt.ylabel('True Stress (MPa)')
plt.title('True Stress Against True Strain')
plt.text(.2, 70, '$E$ = ' + str(round(m,2)) + ' $GPa$')
plt.text(.2, 50, r'$\sigma_{ys}$ = ' + str(round(tStress[y],2)) + ' $MPa$')
plt.text(.2, 30, r'$\sigma_{ut}$ = ' + str(round(tStress[u],2)) + ' $MPa$')
plt.text(.2, 10, r'$\epsilon_{ut}$ = ' + str(round(tStrain[u],2)))
plt.show()



strain = np.arange(0,.5,.001)
stress = 700*strain**.5
m,y,u = MYU(strain,stress,10,.1)

plt.plot(strain, stress, strain[y], stress[y], 'o', strain[u],stress[u],
 'o')
plt.xlabel('True Strain')
plt.ylabel('True Stress (MPa)')
plt.title('True Stress Against True Strain')
plt.text(.2, 70, '$E$ = ' + str(round(m,2)) + ' $GPa$')
plt.text(.2, 50, r'$\sigma_{ys}$ = ' + str(round(stress[y],2)) + ' $MPa$')
plt.text(.2, 30, r'$\sigma_{ut}$ = ' + str(round(stress[u],2)) + ' $MPa$')
plt.text(.2, 10, r'$\epsilon_{ut}$ = ' + str(round(strain[u],2)))
plt.show()