def checkOdd():
    global odd
    if proceed % 2 == 0:
        odd = "Odd"
    else:
        odd = "Even"


def requestOdd():
    global color
    print("The pocket is: ", color)


def checkNumber():
    global proceed
    proceed = input("Please input a roulette number between 0 and 36: ")
    while len(proceed) == 0 or (not proceed.isdigit()):
        proceed = input("Please input a roulette number between 0 and 36: ")
    proceed = int(proceed)
    checkOdd()

checkNumber()
if proceed > 36 or proceed < 0:
    checkNumber()
else:
    if proceed == 0:
        print("Pocket is green.")
    elif proceed >= 1 and proceed <= 10:
        if odd == "Odd":
            color = "red."
            requestOdd()
        else:
            color = "black."
            requestOdd()
    elif proceed >= 11 and proceed <= 18:
        if odd == "Odd":
            color = "black."
            requestOdd()
        else:
            color = "red."
            requestOdd()
    elif proceed >= 19 and proceed <= 28:
        if odd == "Odd":
            color = "red."
            requestOdd()
        else:
            color = "black."
            requestOdd()
    elif proceed >= 29 and proceed <= 36:
        if odd == "Odd":
            color = "black."
            requestOdd()
        else:
            color = "red."
            requestOdd()

