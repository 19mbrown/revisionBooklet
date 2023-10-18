# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
pepper1 = "Cayenne"
pepper2 = "Carolina Reaper"
pepper3 = "Habanero"
pepper4 = "African Bird's Eye"
pepper5 = "Banana Pepper"

scoville = [30000, 1400000, 5000, 175000, 500]


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# If there is a space in the pepper's name, report it
if (pepper1.find (" ") != -1):
    print ("Has space: " + pepper1)
if (pepper2.find (" ") != -1):
    print ("Has space: " + pepper2)
if (pepper3.find(" ") != -1):
    print("Has space: " + pepper3)
if (pepper4.find (" ") != -1):
    print ("Has space: " + pepper4)
if (pepper5.find (" ") != -1):
    print ("Has space: " + pepper5)

# Find the largest scoville heat rating and print out the
#   name of the pepper and the rating
maxIndex = 0
index = 0
currMax = 0
for heat in scoville:
    if (heat > currMax):
        currMax = heat
        maxIndex = index
    index = index + 1

if (maxIndex == 0):
    print ("The hottest pepper is " + pepper1 + " at " + str (currMax))
if (maxIndex == 1):
    print ("The hottest pepper is " + pepper2 + " at " + str (currMax))
if (maxIndex == 2):
    print ("The hottest pepper is " + pepper3 + " at " + str (currMax))
if (maxIndex == 3):
    print ("The hottest pepper is " + pepper4 + " at " + str (currMax))
if (maxIndex == 4):
    print ("The hottest pepper is " + pepper5 + " at " + str (currMax))

