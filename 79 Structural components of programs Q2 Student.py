# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
import random

# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
MAX_SIDES = 10

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
roll = 0
numSides = 0

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def welcome ():
    print ("Welcome to the die rolling program")

def rollDie (pSides):
    theFace = 0
    theFace = random.randint (1, pSides)
    return (theFace)

def getSides ():
    sides = 0
    sides = int (input ("How many sides on your die? "))
    if ((sides > MAX_SIDES) or (sides < 6)):
        print ("Invalid input")
        sides = 0
    return (sides)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
welcome ()
numSides = getSides ()
if (numSides != 0):
    roll = rollDie (numSides)
    print ("Your roll is " + str (roll))
print ("Goodbye")

# -------------------------------------------------------------------
# =====> Write your answers here in the right hand column
# Left                                              # Right
# -------------------------------------------------------------------
# Give the name of a library                        #
# Give the name of a constant                       #
# Give the name of a user-devised function          #
# Give the name for a user-devised procedure        #
# Give the name of a parameter                      #
# Give the name of a local variable                 #
# Give the line number(s) for a selection           #
# Give the line number of a statement that          #
#    changes the data type of a variable
#    from integer to string
