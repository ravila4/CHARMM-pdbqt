
"""
Generates a dictionary of charges for each residue and atom name
usng the CHARMM topology file.
"""

import pickle

amino_acids = {}
curr_residue = None

with open("charmm_data.rtf", 'r') as f:
    for line in f:
        items = line.split() 
        if line.startswith("RESI"):
            curr_residue = items[1]
            # Add to amino acid dictionary
            amino_acids[curr_residue] = {}
        elif line.startswith("ATOM"):
            amino_acids[curr_residue][items[1]] = items[3]


print(amino_acids)
pickle.dump(amino_acids, open("amino_acid_charges.pickle", 'wb'))
