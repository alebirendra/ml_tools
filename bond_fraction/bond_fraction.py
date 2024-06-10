import numpy as np
from pymatgen.core import Structure
from pymatgen.io.cif import CifParser

def load_structure(file_path):
    """
    Load a crystal structure from a CIF file using pymatgen.

    Parameters:
    file_path (str): Path to the CIF file.

    Returns:
    Structure: Pymatgen Structure object.
    """
    parser = CifParser(file_path)
    structure = parser.get_structures()[0]
    return structure

def identify_bonds(structure, distance_threshold=2.0):
    """
    Identify bonds in a crystal structure based on a distance threshold.

    Parameters:
    structure (Structure): Pymatgen Structure object.
    distance_threshold (float): Distance threshold to consider a bond.

    Returns:
    list: List of tuples representing bonded atom pairs.
    """
    bonds = []
    for i, site1 in enumerate(structure.sites):
        for j, site2 in enumerate(structure.sites):
            if i < j:
                distance = site1.distance(site2)
                if distance < distance_threshold:
                    bonds.append((site1.specie.symbol, site2.specie.symbol))
    return bonds

def calculate_bond_fractions(bonds):
    """
    Calculate the fraction of each bond type in a list of bonds.

    Parameters:
    bonds (list): List of tuples representing bonded atom pairs.

    Returns:
    dict: Dictionary with bond types as keys and their fractions as values.
    """
    bond_counts = {}
    total_bonds = len(bonds)
    
    for bond in bonds:
        bond_type = "-".join(sorted(bond))
        if bond_type not in bond_counts:
            bond_counts[bond_type] = 0
        bond_counts[bond_type] += 1
    
    bond_fractions = {bond: count / total_bonds for bond, count in bond_counts.items()}
    return bond_fractions

def bond_fraction_feature_vector(bond_fractions, all_possible_bonds):
    """
    Create a feature vector from bond fractions.

    Parameters:
    bond_fractions (dict): Dictionary with bond types and their fractions.
    all_possible_bonds (list): List of all possible bond types.

    Returns:
    np.ndarray: Feature vector.
    """
    feature_vector = np.zeros(len(all_possible_bonds))
    
    for i, bond in enumerate(all_possible_bonds):
        if bond in bond_fractions:
            feature_vector[i] = bond_fractions[bond]
    
    return feature_vector

# Example Usage
if __name__ == "__main__":
    # Path to the CIF file
    file_path = 'path/to/your/structure.cif'
    
    # Load the crystal structure
    structure = load_structure(file_path)
    
    # Identify bonds
    bonds = identify_bonds(structure)
    
    # Calculate bond fractions
    bond_fractions = calculate_bond_fractions(bonds)
    print("Bond Fractions:\n", bond_fractions)
    
    # Define all possible bonds for feature vector (example for a system with C, H, O)
    all_possible_bonds = ['C-C', 'C-H', 'C-O', 'H-H', 'H-O', 'O-O']
    
    # Create the feature vector
    feature_vector = bond_fraction_feature_vector(bond_fractions, all_possible_bonds)
    print("Feature Vector:\n", feature_vector)
