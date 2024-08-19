#!/bin/env python3
import sys

import matplotlib.pyplot as plt
from sankeyflow import Sankey

visa = {}
# Source: Table A-1. Number of persons waiting for green card and wait time
# URL: https://bipartisanpolicy.org/download/?file=/wp-content/uploads/2019/03/BPC-Immigration-Task-Force-Immigration-101-Path-to-Citizenship-Issue-Brief-May-2014.pdf
# Source: Wait time according to DOS Visa Bulletin (June 2014);
# Source: Number of persons according to DOS Annual Report (November 2013)
# EB1: Employment-Based First Preference (Priority Workers)
# EB2: Employment-Based Second Preference (Members of the Professions Holding Advanced Degrees or Persons of Exceptional Ability)
# EB3: Employment-Based Third Preference (Skilled Workers and Professionals)
# EB3-Other: Employment-Based Third Preference (Other Workers)
# EB4: Employment-Based Fourth Preference (Certain Special Immigrants)
# EB4-Religious: Employment-Based First Preference Other Workers( Certain Religious Workers)
# EB5: Employment-Based Fifth Preference (Employment Creation)
# EB5-Pilot: Employment-Based Fifth Preference (Pilot Programs)
# EB5-Regional: Employment-Based Fifth Preference (Targeted Employment Areas or Regional Centers)
# F1: Family-Sponsored First Preference (Unmarried Sons and Daughters of U.S. Citizens)
# F2A: Family-Sponsored Second Preference, Subcategory A (Spouses and Children of Permanent Residents)
# F2B: Family-Sponsored Second Preference, Subcategory B (Unmarried Sons and Daughters of Permanent Residents)
# F3: Family-Sponsored Third Preference (Married Sons and Daughters of U.S. Citizens)
# F4: Family-Sponsored Fourth Preference (Brothers and Sisters of U.S. Citizens)
visa = {
    '2013': {
        'IR': 0,  # immediate relatives: spouses, unmarried minor children or parents of US citizens

        'F1': 279693,
        'F2A': 238417,
        'F2B': 467642,  # unmarried son/daughter 21yo or older of LPR
        'F3': 804242,
        'F4': 2420977,
        'EB1_1': 2691,  # Priority workers; extraordinarie
        'EB1': 2691,  # Priority workers; extraordinarie
        'EB2': 15866,  # Professionals/advanced degree
        'EB3': 87937,  # skilled worker
        'EB4': 362,  # Ministers, religious, US government workers
        'EB5': 4748,  # investors ($500K-1M) creating 10 jobs
        'DV1': 50000,  # Lottery system
        'DV2': 5000,  # NACARA + Nicaraguan
        'E': 0,  # Treaty traders and Investors
        'TN': 0,  # NAFTA professionals
        'P': 0,  # athletics, players, entertainers
        'R': 0,  # religious workers
        'Q': 0,  # cultural exchange workers
        'REF': 1000000,  # refugees and asylees
        'Asylum': 0,  # Asylees
        'VAWA': 9000,  # VAWA
        'T_Visa': 9000,  # Victims of Human Trafficking
        'DV': 9000,  # Diversity Immigrant Visa
        'SPEC': 9000  # VAWA, Domestic Violence, children of foreign diplomats, former military immigrants
    }
}
visa_waiting_family_sponsored = (
        visa['2013']['F1'] +
        visa['2013']['F2A'] +
        visa['2013']['F2B'] +
        visa['2013']['F3'] +
        visa['2013']['F4']
)
visa_waiting_employment_based = (
        visa['2013']['EB1'] +
        visa['2013']['EB2'] +
        visa['2013']['EB3'] +
        visa['2013']['EB4'] +
        visa['2013']['EB5']
)
visa_waiting_refugee_asylum = (
    visa['2013']['T_Visa'] +
    visa['2013']['Asylum']
)

#######################################################
# DISPLAY OPERATION
#######################################################
plt.figure(figsize=(200, 100), dpi=75)

visa_nodes = [
    [
        ('F1', visa['2013']['F1']),
        ('F2A', visa['2013']['F2A']),
        ('F2B', visa['2013']['F2B']),
        ('F3', visa['2013']['F3']),
        ('F4', visa['2013']['F4']),
        ('EB1-1', visa['2013']['EB1_1']),
        ('EB1-2', visa['2013']['EB1_2']),
        ('EB1-3', visa['2013']['EB1_3']),
        ('EB2-1', visa['2013']['EB2_1']),
        ('EB2-NIW', visa['2013']['EB2_NIW']),
        ('EB3-1', visa['2013']['EB3_1']),
        ('EB3-2', visa['2013']['EB3_2']),
        ('EB3-3', visa['2013']['EB3_3']),
        ('EB4', visa['2013']['EB4']),
        ('EB5', visa['2013']['EB5']),
        ('IR5', visa['2013']['IR5']),
        ('VAWA', visa['2013']['VAWA']),
        ('DV', visa['2013']['DV']),
        ('K-1', visa['2013']['K_1']),
        ('IR-1/CR-1', visa['2013']['IR_1']),
        ('T-Visa', visa['2013']['T_Visa']),
        ('Asylum', visa['2013']['Asylum']),
        ('IR-2', visa['2013']['IR_2']),
        ('U-Visa', visa['2013']['U_Visa']),
        ('Refugee', visa['2013']['Refugee']),
    ],
    [
        ('Family', visa_waiting_family_sponsored),
        ('Employment', visa_waiting_employment_based),
    ],
]
visa_flows = [
    ('F1', 'Family', visa['2013']['F1']),
    ('F2A', 'Family', visa['2013']['F2A']),
    ('F2B', 'Family', visa['2013']['F2B']),
    ('F3', 'Family', visa['2013']['F3']),
    ('F4', 'Family', visa['2013']['F4']),

    ('EB1', 'Employment', visa['2013']['EB1']),
    ('EB2', 'Employment', visa['2013']['EB2']),
    ('EB3', 'Employment', visa['2013']['EB3']),
    ('EB4', 'Employment', visa['2013']['EB4']),
    ('EB5', 'Employment', visa['2013']['EB5']),
]


if (len(sys.argv) > 1) and str(sys.argv[1]):
    print('Sankey MODE: tax flow')
    s = Sankey(
        flows=visa_flows,
        nodes=visa_nodes,
    )
else:
    print('Sankey MODE: house budget')
    s = Sankey(
        flows=visa_flows,
        nodes=visa_nodes,
    )
s.draw()
plt.show()
