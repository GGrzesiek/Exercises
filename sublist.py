"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None

def sublist(list_one, list_two):
    if list_one == list_two:
        EQUAL = True
    if list_one > list_two:
        master = list_one
        slave = list_two
    else:
        master = list_two
        slave = list_one
    
    for idx in range(len(master) - len(slave) + 1):
        if master[idx: idx + len(slave)] == slave:
            SUPERLIST = True



                
    
