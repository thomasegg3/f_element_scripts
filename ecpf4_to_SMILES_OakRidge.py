# Tom Egg
# June 6, 2023
# Code to streamline bs data entry work

from rdkit import Chem
import pubchempy as pcp
from rdkit.Chem import AllChem
import pandas as pd

if __name__ == '__main__':
    '''
    Ingest excel sheet of chemical names and convert to smiles
    '''

    input_file = input('Name: ')

    mol = pcp.get_compounds(input_file, 'name')
    print(mol)