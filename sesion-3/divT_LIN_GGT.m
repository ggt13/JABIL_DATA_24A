%%writefile divTLog_GGT.m
% Define parameters
R1 = 1000; % Resistance in ohms - please modify this value
R2 = 1000; % Resistance in ohms - please modify this value
Vin = 10;  % Input voltage in volts - please modify this value

% Define a range of input voltages
Vin_range = linspace(0, Vin, 1000);

% Calculate output voltage for each input voltage
Vout = R2 ./ (R1 + R2) .* log(1 + Vin_range / R1);

% Plot the results
plot(Vin_range, Vout, 'b', 'LineWidth', 2);
xlabel('Input Voltage (V)');
ylabel('Output Voltage (V)');
title('Logarithmic Tension Divider');
grid on;
print -dpng divTLog_GGT.png
