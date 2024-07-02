import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([0, 6])
y_points = np.array([0, 250])
plt.title("Example 1")
plt.plot(x_points, y_points)
plt.show()

x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])
plt.title("Example 2")
plt.plot(x_points, y_points)
plt.show()
