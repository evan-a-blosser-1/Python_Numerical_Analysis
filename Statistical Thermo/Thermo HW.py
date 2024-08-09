import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
#constants 
C = 1.5349e6
L = 42.92e3
R = 8.134
# Temp. from 50 to 100 celsius converted to kelvin
T = np.linspace(323,373,100)
# Derived Equation
p = C*np.exp(-L/(R*T))
# Endpoints
ic(p[0])
ic(p[99])
# Pressures at Temp. 
p_50 = 0.1234
p_100 = 1.013
# Percent Error
perr_50 = np.absolute((p[0]-p_50)/p_50)*100
perr_100 = np.absolute((p[99]-p_100)/p_100)*100
output_message = f"""
{'-'*42}
| Percent error for 50 deg. C
|   {perr_50:.5f}%
|
| Percent error for 100 deg. C
|   {perr_100:.5f}%
{'-'*42}
""" 
print(output_message)
#plot
plt.plot(T,p)
plt.xlabel('Temperature (K)')
plt.ylabel('Pressure (bar)')
plt.show()

