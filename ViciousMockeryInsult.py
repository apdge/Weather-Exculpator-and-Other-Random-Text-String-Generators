# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:07:32 2024
@author: apdge (A. P. D. G. Everett)
This program is based off of my Weather Exculpator progran, but adapted to 
generate insults based off of a picture I saw on Facebook called:
    "Your Vicious Mockery Insult"
So, whilst I claim no authorship to the table itself, I do claim authorship
of this program.
"""
import random

# Lists representing the three columns of words
column1 = [
    "Steamy", "Witless", "Lumpy", "Shitty", "Moist", "Chunky", 
    "Lousy", "Bulbous", "Trashy", "Dumbass", "Crusty", "Brainless"
]
column2 = [
    "Knob", "Bum", "Turd", "Bulge", "Ass", "Wang", 
    "Shit", "Chode", "Fuck", "Jizz", "Cock", "Dong"
]
column3 = [
    "Gremlin", "Licker", "Spasm", "Fiend", "Shitter", "Raider", 
    "Demon", "Juggler", "Pixie", "Fiddler", "Sniffer", "Fungus"
]

# Function to generate a random insult, ensuring no repetition
def generate_insult(previous_insult=None):
    while True:
        part1 = random.choice(column1)
        part2 = random.choice(column2)
        part3 = random.choice(column3)
        insult = f"{part1} {part2} {part3}"
        if insult != previous_insult:
            return insult

# Store the last generated insult
last_insult = None

# Generate and print a random insult
if __name__ == "__main__":
    for _ in range(5):  # Generate and print multiple insults
        insult = generate_insult(last_insult)
        print("Your Vicious Mockery insult:")
        print(insult)
        last_insult = insult
