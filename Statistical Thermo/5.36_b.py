##################
# Problem 5.36_B #
####################
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
#Constants
#################
K   = 1.381e-23 #J/K
T   = 298       #K
g   = 9.81      # m/s^2
P_0 = 1.013     # bar
m_i = (78/100)*2*14.00674 + (21/100)*2*15.9994 + (1/100)*39.948
# convert units
m_kg = m_i*10**-3
# Apply Avigadro's number
N_A = 6.002e23
m = m_kg/N_A
ic(m)
# Define Pressure as a function
#  of altitude
def Pres_Func(z):
    return P_0*np.exp((-m*g*z)/(K*T))
p_1 = Pres_Func(1430)
p_2 = Pres_Func(3090)
p_3 = Pres_Func(4420)
p_4 = Pres_Func(8850)
output_message = f"""
{'-'*42}
| {p_1}
| {p_2}
| {p_3}
| {p_4}
{'-'*42}
"""
print(output_message)
##################
# problem 5.36_C #
##################
def Temp_Dep(P):
    L = 42.92e3
    c = 2.688172e-3
    return 1/((m_kg*g*z)/(T*L) + c )
# Altitude
z = np.linspace(100,1000,100)
# Temperture
Temp = Temp_Dep(z)
# Plot 
plt.plot(z,Temp)
plt.xlabel('Altitude (meter)')
plt.ylabel('Temperature (K)')
plt.show()