from shapely.geometry import LineString
from matplotlib import pyplot as plt

# Function to plot the graph with given points
def plot_graph(points):
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])

    # Plot the lines
    plt.plot(x[:2], y[:2], color='purple', label='2x + y = 500')
    plt.plot(x[2:4], y[2:4], color='orange', label='x = 150')
    plt.plot(x[4:6], y[4:6], color='cyan', label='y = 250')

    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    plt.title('Plotting')

    line1 = LineString([(x[0], y[0]), (x[1], y[1])])
    line2 = LineString([(x[2], y[2]), (x[3], y[3])])
    line3 = LineString([(x[4], y[4]), (x[5], y[5])])

    # Find intersections and plot them
    intersection = line1.intersection(line3)
    plt.plot(*intersection.xy, 'ro', label='Intersection 1')

    intersection2 = line1.intersection(line2)
    plt.plot(*intersection2.xy, 'go', label='Intersection 2')

    # Plot additional points
    plt.plot(x[4], y[4], 'bo', label='Point 1')
    plt.plot(x[2], y[2], 'mo', label='Point 2')

    # Fill the region with color
    x_fill = [x[4], intersection.xy[0][0], intersection2.xy[0][0], x[2]]
    y_fill = [y[4], intersection.xy[1][0], intersection2.xy[1][0], y[2]]

    plt.fill(x_fill, y_fill, color='green', alpha=0.4, label='Shaded Region')

    # Show legends
    plt.legend()

    plt.show()

    # Print the coordinates of the intersections
    print("Point of Intersection 1: ")
    print(intersection.xy[0][0])
    print(intersection.xy[1][0])
    print("Point of Intersection 2: ")
    print(intersection2.xy[0][0])
    print(intersection2.xy[1][0])

    # Calculate and print the values of Z for each point
    z = []
    for i in range(0, 4):
        eqn = 8 * x[i+2] + 5 * y[i+2]
        z.append(eqn)
        print("Z =", z)

    # Find and print the maximum Z value and its corresponding point
    max_val = max(z)
    xy_index = z.index(max_val)
    print("The Value of Z =", max_val, "at point (", x[xy_index+2], ",", y[xy_index+2], ")")

# Example usage with points provided by the user
points = [(250, 0), (0, 500), (0, 250), (250, 250), (150, 0), (150, 500)]
plot_graph(points)