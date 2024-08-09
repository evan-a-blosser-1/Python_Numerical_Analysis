import numpy as np
import matplotlib.pyplot as plt

# Define temperature (in Kelvin)
temperature = 298.15  # You can choose any desired temperature

# Define a range of pressures (in Pascals or bar)
pressures = np.linspace(1e5, 1e7, 100)  # Example range from 100 kPa to 10 MPa

# Example data (you should replace these with real data)
delta_H_solid = -60000  # Enthalpy change for solid phase (J/mol)
delta_S_solid = -100  # Entropy change for solid phase (J/mol*K)

delta_H_liquid = -40000  # Enthalpy change for liquid phase (J/mol)
delta_S_liquid = 100  # Entropy change for liquid phase (J/mol*K)

delta_H_gas = -20000  # Enthalpy change for gas phase (J/mol)
delta_S_gas = 200  # Entropy change for gas phase (J/mol*K)

# Calculate Gibbs free energy change for each phase
delta_G_solid = delta_H_solid - temperature * delta_S_solid * np.ones_like(pressures)
delta_G_liquid = delta_H_liquid - temperature * delta_S_liquid * np.ones_like(pressures)
delta_G_gas = delta_H_gas - temperature * delta_S_gas * np.ones_like(pressures)

# Create plots
plt.figure(figsize=(10, 6))
plt.plot(pressures, delta_G_solid, label='Solid Phase')
plt.plot(pressures, delta_G_liquid, label='Liquid Phase')
plt.plot(pressures, delta_G_gas, label='Gas Phase')

# Add labels and legend
plt.xlabel('Pressure (Pa)')
plt.ylabel('Gibbs Free Energy (J/mol)')
plt.title(f'Gibbs Free Energy of Water at {temperature} K')
plt.legend()

# Show the plot
plt.show()
