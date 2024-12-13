# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:07:17 2024
@author: apdge (A. P. D. G. Everett)
In AWS/FM-300/005, there was an exclupation table composed of three columns of 
10 terms in each that would allow a military weather person to generate an 
excuse on the fly:
    "Yeah, sorry sir/ma'am, the (excuse 1) "dynamic vorticity stratification" 
    caused the (excuse 2) "kinematic turbulent field" and this is why your 
    flight from (air field 1) to (air field 2) was rocky as all can be"
Certainly not to be used during a for-real investigation if a plane or chopper
went down, but definitely useful if you want to avoid teling a pissed-off pilot
that "it's winter and your dumbass shouldn't be flying then" but would like to 
avoid an Article 15 or a court-martial for insulting/disrespecting an officer.    

Every Air Force weather person I knew of learnt this table (either at tech 
school or their first operational assignment) and NOAA folks also use it 
(as many people at NOAA are ex-AF weather, so even NOAA/NWS civilians who 
aren't AF veterans also are exposed to it) so I assume the Navy/MC METOC folks 
have it too, but I cannot confirm that.

Given you might need more than one excuse at the same time, this program as 
designed by me generates five excluplations at a time, so hopefully what you
get the first time you run the program is what you need at the time.
"""
import random

# Lists representing the three columns of words
column1 = [
    "Integrated", "Pseudo", "Dynamic", "Potential", "Diurnal",  
    "Stratospheric", "Cumulative", "Absolute", "Kinematic", "Conditional",
]
column2 = [
    "Thermal", "Vorticity", "Solenoidal", "Molecular", "Orographic", 
    "Turbulent", "Solar", "Inertial", "Rotational", "Vapour",
]
column3 = [
    "Equilibrium", "Transfer", "Stratification", "Balance", "Field", 
    "Correlation", "Discontinuity", "Advection", "Trajectory", "Function"
]

# Function to generate a random insult, ensuring no repetition
def generate_excuse(previous_excuse=None):
    while True:
        part1 = random.choice(column1)
        part2 = random.choice(column2)
        part3 = random.choice(column3)
        excuse = f"{part1} {part2} {part3}"
        if excuse != previous_excuse:
            return excuse

# Store the last generated insult
last_excuse = None

# Generate and print a random insult
if __name__ == "__main__":
    for _ in range(5):  # Generate and print multiple insults
        excuse = generate_excuse(last_excuse)
        print("Your Meteorological Exculpation is:")
        print(excuse)
        last_excuse = excuse
