#code by Romijul Laskar 20CS8065
from shapely.geometry import LineString
from matplotlib import pyplot as plt

# Data for lines
x1 = [250, 0]
y1 = [0, 500]

x2 = [0, 250]
y2 = [250, 250]

x3 = [150, 150]
y3 = [0, 500]

# Plot the lines
plt.plot(x1, y1, color='purple', label='2x + y = 500')
plt.plot(x2, y2, color='orange', label='x = 150')
plt.plot(x3, y3, color='cyan', label='y = 250')

plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.title('Plotting')

line1 = LineString([(250, 0), (0, 500)])
line2 = LineString([(150, 0), (150, 500)])
line3 = LineString([(0, 250), (250, 250)])

# Find intersections and plot them
intersection = line1.intersection(line3)
plt.plot(*intersection.xy, 'ro', label='Intersection 1')

intersection2 = line1.intersection(line2)
plt.plot(*intersection2.xy, 'go', label='Intersection 2')

# Plot additional points
plt.plot(0, 250, 'bo', label='Point 1')
plt.plot(150, 0, 'mo', label='Point 2')

# Fill the region with color
x = [0, intersection.xy[0][0], intersection2.xy[0][0], 150]
y = [250, intersection.xy[1][0], intersection2.xy[1][0], 0]

plt.fill(x, y, color='green', alpha=0.4,
         label='Shaded Region')  # Random color green

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
    eqn = 8 * x[i] + 5 * y[i]
    z.append(eqn)
    print("Z =", z)

# Find and print the maximum Z value and its corresponding point
max_val = max(z)
xy_index = z.index(max_val)
print("The Value of Z =", max_val,
      "at point (", x[xy_index], ",", y[xy_index], ")")
