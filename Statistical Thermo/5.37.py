import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
#########
T = np.linspace(0,800,100)
P = 3.59712 + 15.10791e-3*(T-298)


# Plot 
plt.plot(T,P)
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (Bar)')
plt.show()