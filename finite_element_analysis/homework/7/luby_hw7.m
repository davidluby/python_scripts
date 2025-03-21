%% David Luby
% ME 786
% HW 7
% 11-10-2022

clear; clc;

E = 220; % in^4
I = 32E6; % psi

l1 = 5*12; % inches
l2 = 5*12; % inches
l3 = 8*12; % inches
l4 = 6*12; % inches

fDE = -1200*l4/2;
fCD = -1200*l3/2;
fB = -5000;

mD = fDE*l4;
mE = fCD*l3;

syms vB tD tE % displacement b, theta d, theta e

one = [fB == E*I*(vB*(12/(l1^3) +12/(l2^3)))];

two = [mE-mD == E*I*(tD*(4/l3 +4/l4) + tE*(2/l4))];

three = [mE == E*I*(tD*2/l4 + tE*4/l4)];

soln = solve([one two three], [vB tD tE]);

Db = double(soln.vB)
thetaD = double(soln.tD);
thetaE = double(soln.tE);

Dmid = 3-(2*3*3/6 + 3*3*3/36)

Ra = E*I*-12/(l1^3)*Db

Re = E*I*(2/l4*thetaD +4/l4*thetaE)