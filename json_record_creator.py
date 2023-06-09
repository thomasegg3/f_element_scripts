import json
import pandas as pd
import numpy as np
from rdkit import Chem

def organic_phase(extractant_list, extractant_conc, extractant_unit, solvent_list, solvent_volfracs, organic_vol, organic_unit):
    '''
    Function to write dictionary for organic phase

    @param extractant_list : list of extractant ligands
    @param extractant_conc : list of extractant concentrations
    @param extractant_unit : units of extractant concentration
    @param solvent_list : list of solvent
    @param solvent_volumes : volumes of solvent
    @organic vol : volume of organic phase
    '''
    # Initialize dictionary
    organic_dictionary = {'extractants' : [], 'solvents' : [], 'volume' : []}

    # Extractants
    for extractant, concentration, unit in zip(extractant_list, extractant_conc, extractant_unit):

        # Create extractant dictionary
        extractant_dict = {
            'identity': extractant,
            'concentration': {
                'quantity': concentration,
                'unit': unit
            }
        }

        # Add extractant to the organic dictionary element
        organic_dictionary['extractants'].append(extractant_dict)

    # Solvents
    for solvent, volume in zip(solvent_list, solvent_volfracs):

        # Create solvent dictionary
        solvent_dict = {
            'identity': solvent,
            'volfraction': volume
        }

        # Add solvent to solvent dictionary element
        organic_dictionary['solvents'].append(solvent_dict)

    # Volumes
    organic_dictionary['volume'] = {
        'quantity': organic_vol,
        'unit': organic_unit
    }

    # Return dictionary
    return organic_dictionary

def aqueous_phase(solute_list, solute_conc, solute_unit, pH, aq_vol, aq_unit):
    '''
    Function to write dictionary for aqueous layer

    @param solute_list : list of solutes present
    @param solute_conc : solute concentrations
    @param solute_unit : unite of volume
    @param pH : pH value
    @param aq_vol : volume of aqueous layer
    @param aq_unit : units
    '''
    # Initialize dictionary
    aqueous_dictionary = {'solutes': [], 'pH': [], 'volume': []}

    # Solutes
    for solute, concentration, unit in zip(solute_list, solute_conc, solute_unit):

        #Create solute dictionary
        solute_dictionary = {
            'identity': solute,
            'concentration' : {
                'quantity': concentration,
                'unit': unit
            }
        }

        # Add solutes to solute dictionary
        aqueous_dictionary['solutes'].append(solute_dictionary)

    # pH
    aqueous_dictionary['pH'] = pH

    # Volume
    aqueous_dictionary['volume'] = {
        'quantity': aq_vol,
        'unit': unit
    }

    # Return dictionary
    return aqueous_dictionary

def reaction_conditions(temp_val, temp_unit, time_val, time_unit):
    '''
    Function to write reaction conditions dictionary

    @param temp_val : temperature value
    @param temp_unit : temperature unit
    @param time_val : time value
    @param time_unit : time unit
    '''
    # Initialize dictionary
    reac_condition_dictionary = {'temperature': [], 'time': []}

    # Temperature
    reac_condition_dictionary['temperature'] = {
        'quantity': temp_val,
        'unit': temp_unit
    }

    # Time
    reac_condition_dictionary['time'] = {
        'quantity': time_val,
        'unit': time_unit
    }

    # Return dictionary
    return reac_condition_dictionary

def metals(metal_list, metal_conc, metal_unit, d_val_list, quant_list):
    '''
    Function to write metals list

    @param metal_list : list of rare metals
    @param metal_conc : list of concentrations
    @param metal_unit : list of metal concentration units
    @param d_val_list : list of D values
    @param quant_list : list of quantification methods
    '''
    # Initialize dictionary
    metal_list = []

    # Create metal list
    for metal, concentration, unit, d, quant in zip(metal_list, metal_conc, metal_unit, d_val_list, quant_list):

        # Create metal dictionary
        metal_dict = {
            'identity': metal,
            'initial concentration':{
                'quantity': concentration,
                'unit': unit
            },
            'D': d,
            'quantification method': quant
        }

        # Add to metal list
        metal_list.append(metal_dict)

    # Return list
    return metal_list

def observations(third_phase, comment):
    '''
    Function to fill in observations

    @param third_phase : Is there a third phase
    @param comment : comment on figure
    '''
    # Initialize dictionary
    observation_dictionary = {'third phase': [], 'comment': []}

    # Third phase
    observation_dictionary['third phase'] = third_phase

    # Comment
    observation_dictionary['comment'] = comment

def provenance(doi, file):
    '''
    Function to create provenance dictionary

    @param doi : paper DOI
    @param file : file link
    '''
    # Initialize provenance dictionary
    provenance_dictionary = {'doi': [], 'attached_file': []}

    # DOI
    provenance_dictionary['doi'] = doi

    # Attached file
    provenance_dictionary['attached_file'] = file

def record(time, username, name, email, orcid, org):
    '''
    Function to create record

    @param time : current time
    @oaram username : username
    @param name : name
    @param email : email address
    @param orcid : orcid
    @param organization : GO RAMS!
    '''

########
# MAIN #
########
if __name__ == '__main__':
    
    # Prompt user to enter organic info
    print('ORGANIC PHASE')
    print('_____________')

    # Organic lists
    extractant_list = []
    extractant_conc = []
    extractant_unit = []
