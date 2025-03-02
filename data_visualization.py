import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)  
y = np.random.randint(1, 100, size=10)  

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Random Data')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Data Line Plot")
plt.legend()

plt.savefig("plot.png")
plt.show()
