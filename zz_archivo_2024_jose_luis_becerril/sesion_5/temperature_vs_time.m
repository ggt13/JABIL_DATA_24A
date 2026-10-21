%%writefile temperature_vs_time.m

% Generate synthetic data
n = 1000; % Number of data points (reduced for demonstration)
time = linspace(1, 100, n); % Time data
temperature = 0.5 * time + 10 + randn(1, n) * 2; % Linear relationship with noise

% Perform least squares fitting
X = [ones(size(time)); time];
coefficients = (X * X') \ (X * temperature');

% Calculate fitted values
fitted_values = X' * coefficients;

% Plot the data and the fitted line
plot(time, temperature, '.', 'MarkerSize', 10); hold on;
plot(time, fitted_values, 'r', 'LineWidth', 2);
xlabel('Time');
ylabel('Temperature');
title('Least Squares Fitting of Temperature vs Time');
legend('Data', 'Fitted Line');
grid on;
print -dpng temperature_vs_time.png
