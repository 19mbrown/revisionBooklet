#--------------------------------------------------------------------
# Constants
#--------------------------------------------------------------------
ON_ROLL = 3722          # Students enrolled in college

#--------------------------------------------------------------------
# Global variables
#--------------------------------------------------------------------
languageTable = ["French", "Italian", "Spanish", "Mandarin", "German"]
enrolmentNumbers = [366, 130, 494, 79, 243]
# =====> Write your code here

#--------------------------------------------------------------------
# Main program
#--------------------------------------------------------------------
# =====> Write your code here

for i in range(0, len(languageTable), 1):
    print(languageTable[i], enrolmentNumbers[i], enrolmentNumbers[i] / ON_ROLL)

print("Total for languages is", sum(enrolmentNumbers), "{:.2f}".format(100 * sum(enrolmentNumbers) / ON_ROLL))
