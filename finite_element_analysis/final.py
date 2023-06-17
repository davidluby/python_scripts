"""
David Luby
ME 786
Final Exam
12-15-2022
"""

import numpy as np

"""
Problem 2 -- Solving SLE
"""

# initializing vairables
l = 7 # length (m)
e = 220E9 # yield strength (Pa)
i = 1.5E-4 # area moment of inertia(m^-4)
p = 8E3 # distributed force (N/m)
k = 900E3 # spring constant (N/m)

coeff = [[4*e*i/l, -6*e*i/(l**2), 2*e*i/l, 0],
    [-6*e*i/(l**2), (24*e*i/(l**3) + k), 0, 6*e*i/(l**2)],
    [2*e*i/l, 0, 8*e*i/l, 2*e*i/l],
    [0, 6*e*i/(l**2), 2*e*i/l, 4*e*i/l]]
a = np.array(coeff)
aInv = np.linalg.inv(a)

B = [[-p*(l**2)/12], [-2*p*l/2], [0], [p*(l**2)/12]]

X = aInv.dot(B)
names = ['theta1', 'displacement2', 'theta2', 'theta3']
print('Problem 2')

i =-1
for x in X:
    i +=1
    print(names[i],'= %.4f'%x[0])
r1 = (6*e*i/(l**2)*X[0] - 12*e*i/(l**3)*X[1] +p*l/2)/(1000**2)
print('reaction1','= %.4f'%r1)


"""
Problem 3 -- Creating and Solving SLE
"""

E = 30E6 # elastic modulus (psi)
v = .3 # poisson ratio
t = 1 # thickness (in)
A = (21**2)/2
T = 21000*2**.5

nodeX = [0, 21, 0]
nodeY = [21, 0, 0]
x = []
y = []
i = -1
for num in nodeX:
    i +=1
    j = -1
    xs = []
    ys = []
    for nums in nodeX:
        j +=1
        xs.append(nodeX[i]-nodeX[j])
        ys.append(nodeY[i]-nodeY[j])
    x.append(xs)
    y.append(ys)

det = x[0][2]*y[1][2] - x[1][2]*y[0][2] # python indicies begin at zero!

B = 1/det*np.array([[y[1][2], 0, y[2][0], 0, y[0][1], 0],
    [0, x[2][1], 0, x[0][2], 0, x[1][0]],
    [x[2][1], y[1][2], x[0][2], y[2][0], x[1][0], y[0][1]]])

bT = np.transpose(B) # this is actually the B array

D = E/(1-v**2)*np.array([[1, v, 0],
                        [v, 1, 0],
                        [0, 0, (1-v)/2]])
DB = np.matmul(D, B)

K = t*A*np.matmul(bT, DB)
np.set_printoptions(precision=1)
print()
print('Problem 3')
print('K = \n', K)

q3 = T/K[2][2]
print('\nq3 = ', round(q3, 6)) # indicies start at 0!

Q = np.array([0, 0, q3, 0, 0, 0])
strain = np.matmul(B, Q)
stress = np.matmul(D, strain)

print('\nThe strain matrix is: ', strain)
print('The stress matrix is: ', stress)