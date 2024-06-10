clear;
R1=1000;
VIN=5;

R2=(1:1000);
for i=1:3
    for j=1:3
VO=VIN*(R2 ./ (R1+R2));
plot(R2,VO,"k:");
hold on
end
end
V=[R2.', VO.']

R3=(1:10:10000);
for i=1:3
    for j=1:3
VO=VIN*(R3 ./ (R1+R3));
plot(R2,VO,"r*");
hold on
end
end

V=[R3.', VO.']

R4=(1:100:100000);
for i=1:3
    for j=1:3
VO=VIN*(R4 ./ (R1+R4));
plot(R2,VO,"b--");
hold on
end
end
V=[R4.', VO.']

hold off
legend({"R2","R3","R4"})
xlabel("Resistencia variable")