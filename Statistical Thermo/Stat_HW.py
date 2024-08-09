import numpy as np
import matplotlib.pyplot as plt
# Define Equaiton
def u(y):
    return y**(-5)*np.exp(-1/y)
# Create a linear space for inputs
x = np.linspace(0.0001,1,100)
# Find maximum
max_index = np.argmax(u(x))

max_value = x[max_index]
print(max_value)
plt.plot(x,u(x))
plt.show()

