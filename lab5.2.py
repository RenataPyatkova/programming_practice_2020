import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
deg = 1
p = np.polyfit(x, y, deg=1, cov=True)

f = p[0][0] * np.array(x)**deg + p[0][deg]
plt.plot(x, y, '--o')
plt.grid(True)
plt.show()
