%% David Luby
% ME 786
% HW 5
% 10-18-2022

clear; clc;

%% No 4.1-a

E = 30E6; %psi
A = 2.1; %in^2

q = (10^-2)*[1.1; 0; 2.4; -.6; -1.8; 2.2];

x1 = 10; y1 = 10; z1 = -22;

x2 = 50; y2 = 40; z2 = 22;

dx = x2-x1; dy = y2-y1; dz = z2-z1;

len = sqrt(dx^2 + dy^2 + dz^2);

l = dx/len; m = dy/len; n = dz/len;

L = [l, m, n, 0, 0, 0; 0, 0, 0, l, m, n];

displacement = L*q

%% No 4.1-b

% dl = pl/ae
    % stress = p/a = dl*e/l
stress = (displacement(1)-displacement(2))*E/len

%% No 4.1-c
lmn = [l*l, m*l, n*l, -l*l, -m*l, -n*l];
stiffness = zeros(6);
for i = 1:1:6
    for j = 1:1:6
        if (i > 3)
            stiffness(i,j) = -1*E*A/len*lmn(j);
        else
            stiffness(i,j) = E*A/len*lmn(j);
        end
    end
end

stiffness

%% No 4.1-d

strainEnergy = 1/2*q'*stiffness*q