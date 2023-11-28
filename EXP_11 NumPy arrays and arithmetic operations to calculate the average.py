import numpy as np

# Assuming 'fuel_efficiency' is your NumPy array with fuel efficiency data
fuel_efficiency = np.array([25, 30, 22, 28, 35, 18, 32, 26])

# Calculate the average fuel efficiency
average_fuel_efficiency = np.mean(fuel_efficiency)

# Determine the percentage improvement between two car models
car_model_1_index = 2  # Replace with the actual index of the first car model
car_model_2_index = 5  # Replace with the actual index of the second car model

fuel_efficiency_model_1 = fuel_efficiency[car_model_1_index]
fuel_efficiency_model_2 = fuel_efficiency[car_model_2_index]

percentage_improvement = ((fuel_efficiency_model_2 - fuel_efficiency_model_1) / fuel_efficiency_model_1) * 100

# Display the results
print("Average Fuel Efficiency:", average_fuel_efficiency)
print(f"Percentage Improvement from Model {car_model_1_index + 1} to Model {car_model_2_index + 1}: {percentage_improvement:.2f}%")
