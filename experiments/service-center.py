#!/bin/env python3
import sys

import matplotlib.pyplot as plt
from sankeyflow import Sankey

UNKNOWN = 0

c_cases = {}
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

benefit_centers = {
    'MSC': {
        'name': 'National Benefits Center',
        'city': '',
        'state': ''
    },
    'LIN': {
        'name': 'Nebraska Service Center',
        'city': 'Lincoln',
        'state': 'Nebraska'
    },
    'SRC': {
        'name': 'Texas Service Center',
        'city': '',
        'state': 'Texas'
    },
    'EAC': {
        'name': 'Vermont Service Center',
        'city': '',
        'state': 'Vermont'
    },
    'WAC': {
        'name': 'California Service Center',
        'city': '',
        'state': 'California'
    },
    'YSC': {
        'name': 'Potomac Service Center',
        'city': '',
        'state': ''
    }
}
c_cases = {
    '2013': {
        'Entrance': 0,  # People entering into US any ways or forms

        'Gotaways': 600000,  # Aliens who snuck inside US illegally
        'Southern': 2500000,  # Entered through the Southern Border
        'humanitarian': 240000,  # Parole via humanitarian
        'Affirmative': 440000,  # Affirmative Asylum Applications

        'F1': 279693,
        'F2': 238417 + 467642,
        'F2A': 238417,
        'F2B': 467642,  # unmarried son/daughter 21yo or older of LPR
        'F3': 804242,
        'F4': 2420977,
        'EB1': 2691,  # Priority workers; extraordinarie
        'EB1_1': 691,  # estimated from EB1
        'EB1_2': 2000,  # estimated from EB1
        'EB1_3': UNKNOWN,
        'EB2_1': 15866,  # Professionals/advanced degree
        'EB2_NIW': 0,  # ????
        'EB2': 15866,
        'EB3_1': 87937,  # skilled worker
        'EB3_2': 0,  # skilled worker
        'EB3_3': 0,  # skilled worker
        'EB3': 87937,  # skilled worker
        'EB4': 362,  # Ministers, religious, US government workers
        'EB5': 4748,  # investors ($500K-1M) creating 10 jobs
        'DV1': 50000,  # Lottery system
        'DV2': 5000,  # NACARA + Nicaraguan
        'E': 0,  # Treaty traders and Investors
        'TN': 0,  # NAFTA professionals
        'K': 0,
        'K_1': 0,
        'K_2': 0,
        'P': 0,  # athletics, players, entertainers
        'R': 0,  # religious workers
        'Q': 0,  # cultural exchange workers
        'IR': 0,  # immediate relatives: spouses, unmarried minor children or parents of US citizens
        'IR_1': 0,
        'IR_2': 0,
        'IR_5': 0,
        'U_Visa': 0,
        'REF': 1000000,  # refugees and asylees
        'Refugee': 0,
        'Asylum': 0,
        'T_Visa': 9000,  # Victims of Human Trafficking
        'DV': 9000,  # Diversity Immigrant Visa
        'VAWA': 9000,  # VAWA
        'SPEC': 9000,  # VAWA, Domestic Violence, children of foreign diplomats, former military immigrants
        'Green': 0,  # Green Card
    }
}
visa_waiting_family_sponsored_f2 = (
        c_cases['2013']['F2A'] +
        c_cases['2013']['F2B']
)
visa_waiting_family_sponsored = (
        c_cases['2013']['F1'] +
        c_cases['2013']['F2'] +
        c_cases['2013']['F3'] +
        c_cases['2013']['F4']
)
visa_waiting_employment_based_eb1 = (
        c_cases['2013']['EB1_1'] +
        c_cases['2013']['EB1_2'] +
        c_cases['2013']['EB1_3']
)
visa_waiting_employment_based_eb2 = (
        c_cases['2013']['EB2_1'] +
        c_cases['2013']['EB2_NIW']
)
visa_waiting_employment_based_eb3 = (
        c_cases['2013']['EB3_1'] +
        c_cases['2013']['EB3_2'] +
        c_cases['2013']['EB3_3']
)
visa_waiting_employment_based = (
        c_cases['2013']['EB1'] +
        c_cases['2013']['EB2'] +
        c_cases['2013']['EB3'] +
        c_cases['2013']['EB4'] +
        c_cases['2013']['EB5']
)
visa_waiting_refugee_asylum = (
        c_cases['2013']['DV'] +
        c_cases['2013']['U_Visa'] +
        c_cases['2013']['VAWA'] +
        c_cases['2013']['T_Visa'] +
        c_cases['2013']['Asylum'] +
        c_cases['2013']['Refugee']
)

#######################################################
# DISPLAY OPERATION
#######################################################
plt.figure(figsize=(200, 100), dpi=75)

visa_nodes = [
    [
        ('Entrance', c_cases['2023']['Entrance'])
    ],
    [
        ('Southern', c_cases['2023']['Southern'])
    ],
    [
        ('F2A', c_cases['2013']['F2A']),
        ('F2B', c_cases['2013']['F2B']),
        ('EB1_1', c_cases['2013']['EB1_1']),
        ('EB1_2', c_cases['2013']['EB1_2']),
        ('EB1_3', c_cases['2013']['EB1_3']),
        ('EB2_1', c_cases['2013']['EB2_1']),
        ('EB2_NIW', c_cases['2013']['EB2_NIW']),
        ('EB3_1', c_cases['2013']['EB3_1']),
        ('EB3_2', c_cases['2013']['EB3_2']),
        ('EB3_3', c_cases['2013']['EB3_3']),
        ('K_1', c_cases['2013']['K_1']),
        ('K_2', c_cases['2013']['K_2']),
        ('IR_1', c_cases['2013']['IR_1']),
        ('IR_2', c_cases['2013']['IR_2']),
        ('IR_5', c_cases['2013']['IR_5']),
        ('VAWA', c_cases['2013']['VAWA']),
        ('DV', c_cases['2013']['DV']),
        ('T_Visa', c_cases['2013']['T_Visa']),
        ('U_Visa', c_cases['2013']['U_Visa']),
        ('Refugee', c_cases['2013']['Refugee']),
        ('Asylum', c_cases['2013']['Asylum']),
    ],
    [
        ('F1', c_cases['2013']['F1']),
        ('F2', c_cases['2013']['F2']),
        ('F3', c_cases['2013']['F3']),
        ('F4', c_cases['2013']['F4']),
        ('EB1', c_cases['2013']['EB1']),
        ('EB2', c_cases['2013']['EB2']),
        ('EB3', c_cases['2013']['EB2']),
        ('EB4', c_cases['2013']['EB4']),
        ('EB5', c_cases['2013']['EB5']),
        ('K', c_cases['2013']['K']),
        ('IR', c_cases['2013']['IR']),
    ],
    [
        ('Family', visa_waiting_family_sponsored),
        ('Employment', visa_waiting_employment_based),
        ('Displaced', 1),
    ],
    [
        ('Green', c_cases['2022']['green_cards']),
        ('Deported', c_cases['2022']['deported'])
    ]
]
visa_flows = [
    ('Outside', 'Encountered', c_cases['2023']['Southern']),
    ('Outside', 'Gotaways', c_cases['2013']['Gotaways']),

    ('Encountered', 'Title_42', c_cases['2013']['Title_42']),
    ('Encountered', 'Title_8', c_cases['2013']['Title_8']),

    ('Title_42', 'Deported_RO', c_cases['2013']['Title_42']),

    ('Title_8', 'Voluntary_Departure', c_cases['2013']['Voluntary_Departure']),
    ('Title_8', 'Expedited_Removal', c_cases['2013']['Expedited_Removal']),
    ('Title_8', 'Court', c_cases['2013']['NTA_detained']),
    ('Title_8', 'Court', c_cases['2013']['Notice_to_appear']),
    ('Title_8', 'Paroled', c_cases['2013']['Paroled']),

    ('Paroled', 'Ongoing', c_cases['2013']['Paroled']),

    ('Other', 'Court', c_cases['2013']['Other_court']),

    ('F2A', 'F2', c_cases['2013']['F2A']),
    ('F2B', 'F2', c_cases['2013']['F2B']),
    ('EB1_1', 'EB1', c_cases['2013']['EB1_1']),
    ('EB1_2', 'EB1', c_cases['2013']['EB1_2']),
    ('EB1_3', 'EB1', c_cases['2013']['EB1_3']),
    ('EB2_1', 'EB2', c_cases['2013']['EB2']),
    ('EB2_NIW', 'EB2', c_cases['2013']['EB2_NIW']),
    ('EB3_1', 'EB3', c_cases['2013']['EB3_1']),
    ('EB3_2', 'EB3', c_cases['2013']['EB3_2']),
    ('EB3_3', 'EB3', c_cases['2013']['EB3_3']),

    ('IR_1', 'IR', c_cases['2013']['IR_1']),
    ('IR_2', 'IR', c_cases['2013']['IR_2']),

    ('K_1', 'K', c_cases['2013']['K_1']),
    ('K_2', 'K', c_cases['2013']['K_2']),

    ('F1', 'Family', c_cases['2013']['F1']),
    ('F2', 'Family', c_cases['2013']['F2']),
    ('F3', 'Family', c_cases['2013']['F3']),
    ('F4', 'Family', c_cases['2013']['F4']),

    ('EB1', 'Employment', c_cases['2013']['EB1']),
    ('EB2', 'Employment', c_cases['2013']['EB2']),
    ('EB3', 'Employment', c_cases['2013']['EB3']),
    ('EB4', 'Employment', c_cases['2013']['EB4']),
    ('EB5', 'Employment', c_cases['2013']['EB5']),

    ('DV', 'Displaced', c_cases['2013']['DV']),
    ('VAWA', 'Displaced', c_cases['2013']['VAWA']),
    ('T_Visa', 'Displaced', c_cases['2013']['T_Visa']),
    ('U_Visa', 'Displaced', c_cases['2013']['U_Visa']),
    ('Asylum', 'Displaced', c_cases['2013']['Asylum']),
    ('Refugee', 'Displaced', c_cases['2013']['Refugee']),
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
