%%writefile errores.m
clear;
clc;

% Input data
datain = [0.000; 1.000; 2.000; 3.000; 4.000; 5.000; 6.000; 7.000; 8.000; 9.000; 10.000];
dataoutup = [-1.12; 0.21; 1.18; 2.09; 3.33; 4.50; 5.26; 6.59; 7.73; 8.68; 9.80];
dataoutdown = [-0.69; 0.42; 1.65; 2.48; 3.62; 4.71; 5.87; 6.89; 7.92; 9.10; 10.20];

% Calculate the average of the ascending and descending data
dataprom = (dataoutdown + dataoutup) / 2;

% Fit the data using least squares
qup = polyfit(datain, dataoutup, 1);
qdown = polyfit(datain, dataoutdown, 1);
qprom = polyfit(datain, dataprom, 1);

% Number of samples
N = length(datain);

% Calculate delta
M1 = N * sum(datain.^2);  % Changed ^ to .^
M2 = sum(datain)^2;
M12 = M1 - M2;

% Calculate m and b
m1 = N * sum(datain .* dataprom);
m2 = sum(datain) * sum(dataprom);
mf = (m1 - m2) / M12;

bb1 = sum(dataprom);
bb2 = sum(datain.^2);  % Changed ^ to .^
b1 = bb1 * bb2;
b2 = sum(datain .* dataprom) * sum(datain);
bf = (b1 - b2) / M12;

% Generate the fitted line
mreal = qprom(1);
breal = qprom(2);
y1 = mreal * datain + breal;

% Plot the data and the fitted line
figure(1);
plot(datain, dataprom, 'r*');
xlabel('Datos de Entrada');
ylabel('Datos de Salida sin ajuste');
hold on;
plot(datain, dataprom);
hold off;

figure(2);
plot(datain, y1, 'r+', datain, datain, 'b*');
xlabel('Datos de Entrada');
ylabel('Datos de Salida con ajuste');
hold on;
plot(datain, y1);
hold off;

% Calculate real data from the fit
datainreal = y1 * 1.082 - 0.846;

% Calculate uncertainties
p1 = mf * datain;
A = p1';

bfreal = repmat(bf, N, 1);
B = dataprom - bfreal;
C = (B - A).^2;  % Changed ^ to .^
p4 = sum(C);
Sqo2 = (1 / (N - 2)) * p4;
Sqo = sqrt(Sqo2);

% Uncertainty of the slope
Sm = Sqo * sqrt(N / M12);

% Uncertainty of the intercept
Sb = Sqo * sqrt(sum(datain.^2) / M12);  % Changed ^ to .^

% Three standard deviations
SbF = 3 * Sb;
SmF = 3 * Sm;

fprintf('y = (x) * %2.3f + %5.3f \n\n', mreal, breal);
fprintf('pendiente = %2.3f\n', mf);
fprintf('cruce con la ordenada (offset) = %2.3f\n', bf);
fprintf('desviacion estandar de la pendiente = %2.3f\n', Sm);
fprintf('desviacion estandar del cruce por la ordenada = %2.3f\n', Sb);
fprintf('Tres desviaciones estandar de la pendiente = %2.3f\n', SmF);
fprintf('Tres desviaciones estandar del cruce por la ordenada = %2.3f\n', SbF);

% Determination of Sqi
mfreal = repmat(mf, N, 1);
qi = (y1 + bfreal) ./ mfreal;
Sqi = sqrt(Sqo.^2 / mf.^2);

% Instrumental errors
eabs = abs(max(datain) - max(y1));
erel = eabs / max(datain);
erelp = erel * 100;
exa = abs((1 - erel) * 100);
fprintf('error absoluto = %2.3f\n', eabs);
fprintf('error relativo porcentual = %2.3f\n', erelp);
fprintf('exactitud = %2.3f\n', exa);

% Hysteresis
dif = abs(dataoutup - dataoutdown);
eh = max(dif);
eH = (eh / max(datain)) * 100;
fprintf('\n eH = %2.3f por ciento %5.3f \n\n', eH);

% Linearity
difL = abs(datain - y1);
el = max(difL);
eL = (el / max(datain)) * 100;
fprintf('\n eL = %2.3f por ciento %5.3f \n\n', eL);

% Sensitivity
difk = abs(y1 - datain);
ek = max(difk);
eK = (ek / max(datain)) * 100;
fprintf('\n eK = %2.3f por ciento %5.3f \n', eK);

% Zero shift
difz = abs(y1(1) - datain(1));
ez = max(difz);
eZ = (ez / max(datain)) * 100;
fprintf('\n eZ = %2.3f por ciento %5.3f \n', eZ);

% Repeatability
eR = (2 * Sqi / max(datain)) * 100;
fprintf('\n eR = %2.3f por ciento %5.3f \n', eR);

% Instrument uncertainty
UI = max(datain) * sqrt((eH / 100).^2 + (eL / 100).^2 + (eK / 100).^2 + (eZ / 100).^2 + (eR / 100).^2);

% Design uncertainty
Uo = 0.5 * (datain(2) - datain(1));
UD = sqrt(Uo.^2 + UI.^2) * 10;
fprintf('\n Incertidumbre de diseño UD = %2.3f\n', UD);
print -dpng errores.png
