import numpy as np
from scipy.linalg import eigh

def generate_coulomb_matrix(atomic_numbers, positions):
    """
    Generate the Coulomb matrix for a given set of atomic numbers and positions.

    Parameters:
    atomic_numbers (list): List of atomic numbers.
    positions (list): List of atomic positions (each position is a tuple of x, y, z coordinates).

    Returns:
    numpy.ndarray: Coulomb matrix.
    """
    num_atoms = len(atomic_numbers)
    coulomb_matrix = np.zeros((num_atoms, num_atoms))
    
    for i in range(num_atoms):
        for j in range(num_atoms):
            if i == j:
                coulomb_matrix[i, j] = 0.5 * atomic_numbers[i] ** 2.4
            else:
                distance = np.linalg.norm(np.array(positions[i]) - np.array(positions[j]))
                coulomb_matrix[i, j] = atomic_numbers[i] * atomic_numbers[j] / distance
                
    return coulomb_matrix

def get_features_from_coulomb_matrix(coulomb_matrix, num_eigenvalues=10):
    """
    Extract features from the Coulomb matrix for machine learning.

    Parameters:
    coulomb_matrix (numpy.ndarray): Coulomb matrix.
    num_eigenvalues (int): Number of eigenvalues to consider for the feature vector.

    Returns:
    numpy.ndarray: Feature vector.
    """
    # Compute the eigenvalues of the Coulomb matrix
    eigenvalues, _ = eigh(coulomb_matrix)
    
    # Sort the eigenvalues in ascending order
    sorted_eigenvalues = np.sort(eigenvalues)
    
    # Pad with zeros or truncate to ensure a fixed-length feature vector
    if len(sorted_eigenvalues) < num_eigenvalues:
        padded_eigenvalues = np.pad(sorted_eigenvalues, (0, num_eigenvalues - len(sorted_eigenvalues)), 'constant')
    else:
        padded_eigenvalues = sorted_eigenvalues[:num_eigenvalues]
    
    return padded_eigenvalues

# Example Usage
if __name__ == "__main__":
    # Example atomic numbers and positions for a simple structure
    atomic_numbers = [1, 2, 3]  # Hydrogen, Helium, Lithium
    positions = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
    
    # Generate the Coulomb matrix
    coulomb_matrix = generate_coulomb_matrix(atomic_numbers, positions)
    print("Coulomb Matrix:\n", coulomb_matrix)
    
    # Extract features from the Coulomb matrix
    features = get_features_from_coulomb_matrix(coulomb_matrix, num_eigenvalues=5)
    print("Feature Vector:\n", features)
