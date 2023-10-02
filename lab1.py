#Romijul Laskar 20CS8065

import matplotlib.pyplot as plt
import numpy as np

def plot_feasible_region():
    # Constraints: 5x + y >= 10, 2x + 2y >= 12, x + 4y >= 12

    # x range
    x_values = np.linspace(0, 10, 100)

    # corresponding y range
    y_constraint_a = 10 - 5 * x_values
    y_constraint_b = (12 - 2 * x_values) / 2.0
    y_constraint_c = (12 - x_values) / 4.0


    plt.figure(figsize=(8, 6)) # Set the plot size
    plt.xlabel('Number of jars of liquid product (x)')
    plt.ylabel('Number of cartons of dry product (y)')
    plt.grid(True)


    plt.fill_between(x_values, y_constraint_a, where=(y_constraint_a >= 0), alpha=0.2, label='5x + y >= 10') #
    plt.fill_between(x_values, y_constraint_b, where=(y_constraint_b >= 0), alpha=0.2, label='2x + 2y >= 12') # 
    plt.fill_between(x_values, y_constraint_c, where=(y_constraint_c >= 0), alpha=0.2, label='x + 4y >= 12')


    plt.axhline(0, color='black', linewidth=0.5) # Plot the x-axis
    plt.axvline(0, color='black', linewidth=0.5)

    # Plot the optimal solution point
    optimal_x = 8.0
    optimal_y = 2.0  
    # plt.scatter(optimal_x, optimal_y, color='red', marker='o', label='Optimal Solution')

    # Set plot limits
    plt.xlim(0, 10)
    plt.ylim(0, 10)

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

# Call the function to plot the feasible region
plot_feasible_region()
