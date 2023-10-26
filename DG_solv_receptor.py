#Author Elpiniki Paspali
#usage: python DG_solv_receptor.py

import numpy as np

# Load the SASA data for the receptor and membrane (in Å^2)
data_receptor = np.loadtxt('SASA_free_500.dat')
data_membrane = np.loadtxt('SASA_membrane.dat')

# Extract the SASA values (2nd column)
sasa_receptor = data_receptor[:, 1]
sasa_membrane = data_membrane[:, 1]

# Load the Lj (nonpolar solvation coefficient)
Lj = 0.0054  # Adjust this value based on your system

# Calculate the ΔG_solv components for each frame
delta_sasa = sasa_receptor - sasa_membrane
delta_g_polar = delta_sasa * 0.0072  # Conversion factor (kcal/mol·Å^2)
delta_g_nonpolar = Lj * delta_sasa

# Calculate the total ΔG_solv for each frame
delta_g_solv_receptor = delta_g_polar + delta_g_nonpolar

# Save the results in an output file
with open("delta_g_solv_receptor_per_frame.txt", "w") as output_file:
    for frame, dgs in enumerate(delta_g_solv_receptor):
        output_file.write(f"Frame {frame}: ΔG_solv_receptor = {dgs} kcal/mol\n")

print("ΔG_solv for the receptor per frame has been saved to delta_g_solv_receptor_per_frame.txt")
