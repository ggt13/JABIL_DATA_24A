import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def imecas_analysis():
    # Load the Excel file
    file_path = 'datos_2022.xlsx'
    sheet_name = 'SIMAJ2022'

    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Extract the required columns
    data = df[['Estacion', 'Date_Time', 'NO2']]

    # Convert 'Date_Time' to datetime format
    data['Date_Time'] = pd.to_datetime(data['Date_Time'])

    # Prepare the data for linear regression
    # We will use 'Date_Time' as the independent variable (X) and 'NO2' as the dependent variable (y)
    # Convert 'Date_Time' to numerical format (e.g., timestamp)
    data['Date_Time_Num'] = data['Date_Time'].astype(int) / 10**9  # Convert to seconds

    X = data[['Date_Time_Num']]
    y = data['NO2']

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict using the model
    data['NO2_Predicted'] = model.predict(X)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Date_Time'], data['NO2'], color='blue', label='Actual NO2')
    plt.plot(data['Date_Time'], data['NO2_Predicted'], color='red', linewidth=2, label='Predicted NO2')
    plt.xlabel('Date Time')
    plt.ylabel('NO2')
    plt.title('Linear Regression of NO2 over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

imecas_analysis()