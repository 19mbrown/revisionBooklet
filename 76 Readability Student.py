def getUserOption ():
    validChoice = False
    userChoice = 0
    while (validChoice == False):
        showMenu()
        userChoice = int (input ("Enter an option: "))
        NUM_OPTIONS = 3
        if ((userChoice >= 1) and (userChoice <= NUM_OPTIONS)):
            validChoice = True
        else:
            print("Invalid option, try again")
    return (userChoice)
o = 0
def showMenu ():
    AREA = "Area"
    CIRCUMFERENCE = "Circumference"
    EXIT = "Exit"
    print ("-"*35)
    print ("1 " + AREA)
    print ("2 " + CIRCUMFERENCE)
    print ("3 " + EXIT)
r = 0.0
while (o != 3):
    o = getUserOption ()
    if (o == 1):
        import math
        r = float (input ("Enter the r of a circle: "))
        print ("The area is " + str (math.pi * r ** 2))
    elif (o == 2):
        r = float (input ("Enter the r of a circle: "))
        print ("The circumference is " + str (2 * math.pi * r))
print ("Goodbye")
