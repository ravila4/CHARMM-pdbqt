
"""
Generates a dictionary of charges for each residue and atom name
usng the CHARMM topology file.
"""

import pickle

amino_acids = {}
groups = {}
curr_residue = None

with open("charmm_data.rtf", 'r') as f:
    for line in f:
        items = line.split() 
        if line.startswith("RESI"):
            if curr_residue is not None:
                # backbone
                amino_acids[curr_residue]["main"] = dict(groups[1] +
                                                         groups[len(groups)])
                # R group
                r = []
                for i in range(2, len(groups)):
                    r = r + groups[i]
                amino_acids[curr_residue]["r_group"] = dict(r)

            # Update current residue
            curr_residue = items[1]
            # Add to amino acid dictionary
            amino_acids[curr_residue] = {}
            # Start a new group dictionary
            groups = {}
            curr_group = 0
        elif line.startswith("GROUP"):
            # Add group to dictionary
            curr_group += 1
            groups[curr_group] = []
        elif line.startswith("ATOM"):
            # Append atom name and charge
            groups[curr_group].append((items[1], items[3]))


for i in amino_acids:
    print(i)
    print(amino_acids[i])

pickle.dump(amino_acids, open("amino_acid_charges", 'wb'))
