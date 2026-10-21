%%writefile divT_GGT.m
% clear all; % Borra todas las variables
% clear; % Borra ventana de comandos
clc; % Borra ventana de comandos
% Close all; % Borra todas las ventanas 

% Entrada de valores de resistencia fija R1 y voltaje de alimentación (VIN)%
R1 = 1000;
R2 = 10000;
R3 = 100000;
VIN = 5;

RVAR = (1:100:100000); % Cálculo del voltaje de salida del divisor de tensión con una resistencia variable de 100K en serie con la resistencia R1
VO1 = VIN * (RVAR ./ (R1 + RVAR));

RVAR = (1:100:100000); % Cálculo del voltaje de salida del divisor de tensión con una resistencia variable de 100K en serie con la resistencia R2
VO2 = VIN * (RVAR ./ (R2 + RVAR));

RVAR = (1:100:100000); % Cálculo del voltaje de salida del divisor de tensión con una resistencia variable de 100K en serie con la resistencia R3
VO3 = VIN * (RVAR ./ (R3 + RVAR));

% Combine all data into one matrix
data_matrix = [RVAR', VO1', VO2', VO3'];

% Write the combined data to a single CSV file
csvwrite('combined_data.csv', data_matrix);

% Plot the data
plot(RVAR, VO1, "k:", RVAR, VO2, "r*", RVAR, VO3, "b--");
title("Gráfica GTG");
legend("VO1", "VO2", "VO3");
xlabel("Resistencia variable");
ylabel("Voltaje de salida");
print -dpng divT_GGT.png
