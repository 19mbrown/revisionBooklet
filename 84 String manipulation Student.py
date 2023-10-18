# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
userInput = "Ab123"
digits = ""
letters = ""

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
userInput = input ("Enter a 5 character key: ")

# Check the length, a-z, A-Z, 0-9
# =====> Check the length of the string
if (                   != 5):
    print ("Invalid length")
# =====> Check for alphabetic and numeric characters
elif (not                 ):
    print ("Invalid character")
else:       # All good characters, split out the characters
    # =====> Set letters to the first two characters of the input
    letters =
    # =====> Check for alphabetic characters only
    if (                        ):
        print ("First two characters must be alphabetic")
    # =====> Check first letter to be upper case
    elif (not                  ):
        print ("First letter must be upper case")
    # =====> Check second letter to be lower case
    elif (not                      ):
        print ("Second letter must be lower case")
    else:
        # Split out the digits
        # =====> Set digits to the last three characters
        digits =
        # =====> Check all characters are digits
        if (                   ):
            print ("Last three characters must be digits")
        else:
            print ("Well done.  Your entry is valid.")
