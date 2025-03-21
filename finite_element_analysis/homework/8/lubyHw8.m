%% David Luby
%  ME 786
%  HW 8
%  11-22-2022

clear;clc;

%% Part 1b
interval = [-1 1 -1 1];

eX = @(x,y) -3 +12*x^2 -5*y^2 -10*y;

eY = @(x,y) y -3*x;

x = linspace(-1,1,25);
y = linspace(-1,1,25);

k = -24;
for i = 1:length(x)
    k = k + 25;
    for j = 1:length(x)
        x0(j+k) = eX(x(i), y(j));
        y0(j+k) = eY(x(i), y(j));
        xN(j+k) = x(i);
        yN(j+k) = y(j);
    end
end

figure()
fcontour(eX, interval)
hold on
title('Horizontal Strain Contour Plot')
ylabel('Vertical Location')
xlabel('Horizontal Location')

figure()
fcontour(eY, interval)
hold on
title('Vertical Strain Contour Plot')
ylabel('Vertical Location')
xlabel('Horizontal Location')

[max, idx] = max(y0);

figure()
quiver(xN,yN,x0,y0)
hold on
title('2-D Strain Gradient Plot')
ylabel('Vertical Location')
xlabel('Horizontal Location')
xlim([-1 1])
ylim([-1 1])

fprintf('The coordinates of the maximum vertical strain are:')
xN(idx)
yN(idx)
fprintf('The value is:')
max