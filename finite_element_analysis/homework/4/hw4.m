l = 4;

lhalf = 4/2;

lthird = 4/3;

e = 100;

t = 1;

a = l*t;

ahalf = lhalf*t;

athird = lthird*t;

force = 500;

syms x2 y2 y3 z2 z3 z4

a = e*a*x2/l == force

b = 2*e*ahalf*y2/lhalf - e*ahalf*y3/lhalf == force;

bb = -e*ahalf*y2/lhalf + e*ahalf*y3/lhalf == force;

c = 2*e*athird*z2/lthird - e*athird*z3/lthird == force;

cc = -e*a*z2/lthird + 2*e*a*z3/lthird - e*athird*z4/lthird == force;

ccc = -e*athird*z3/lthird + e*athird*z4/lthird == force;


sola = solve([a], [x2]);
solb = solve([b, bb], [y2, y3]);
solc = solve([c, cc, ccc], [z2, z3, z4]);

plot(1, sola, 'o', 2, solb.y2, 'o', 3, solc.z3, 'o')
legend('one', 'two', 'three')
ylabel('disp')
xlabel('elemenets')


