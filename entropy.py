#Author Elpiniki Paspali: elpiniki.paspali@strath.ac.uk
#usage: python entropy.py 
import mdtraj as md
import numpy as np

# List of trajectory file paths
trajectory_files = ['9A_002M_PME_D2.dcd', '9A_002M_PME_D3.dcd', '9A_002M_PME_D4.dcd', '9A_002M_PME_D5.dcd', '9A_002M_PME_D6.dcd', '9A_002M_PME_D7.dcd', '9A_002M_PME_D8.dcd', '9A_002M_PME_D9.dcd', '9A_002M_PME_D10.dcd', '9A_002M_PME_D11.dcd', '9A_002M_PME_D12.dcd', '9A_002M_PME_D13.dcd', '9A_002M_PME_D14.dcd', '9A_002M_PME_D15.dcd', '9A_002M_PME_D16.dcd', '9A_002M_PME_D17.dcd', '9A_002M_PME_D18.dcd', '9A_002M_PME_D19.dcd', '9A_002M_PME_D20.dcd', '9A_002M_PME_D21.dcd']  # Add your file paths

# Initialize a list to store the entropy values for each trajectory
entropy_values = []

# Loop through each trajectory
for trajectory_file in trajectory_files:
    # Load the trajectory
    traj = md.load(trajectory_file, top='GnRH_receptor_wild_POPC_002M_SC.psf')  # Replace with your topology file

    # Define a selection for the solute (e.g., a ligand) based on its atom indices
    solute_indices = [0, 1, 2]  # Replace with your atom indices

    # Extract the positions of the solute atoms
    solute_positions = traj.xyz[:, solute_indices, :]

    # Calculate the covariance matrix of the solute positions
    solute_covariance = np.cov(np.transpose(solute_positions.reshape(len(traj), -1)))

    # Calculate the eigenvalues of the covariance matrix
    eigenvalues = np.linalg.eigvalsh(solute_covariance)

    # Calculate the entropy from the eigenvalues
    kb = 0.0019872041  # Boltzmann constant in kcal/mol/K
    temperature = 300.0  # Replace with your simulation temperature in Kelvin
    entropy = np.sum(0.5 * kb * temperature * np.log(2 * np.pi * np.e * eigenvalues))

    # Append the entropy value to the list
    entropy_values.append(entropy)

# Calculate the average entropy over all trajectories
average_entropy = np.mean(entropy_values)

# Specify the output file path
output_file_path = 'average_entropy_output.txt'

# Write the average entropy to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(f'Average entropy of the solute: {average_entropy} kcal/mol\n')

print(f'Average entropy has been saved to {output_file_path}')
