import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
print(fig.axes)
print(type(fig))

plt.scatter(1.0, 1.0)

print(fig.axes)

plt.show()