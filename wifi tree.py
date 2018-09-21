

def proceed():
    global yeet
    proceed = input("Type 1 for yes and 0 for no: ")
    while len(proceed) == 0 or (not proceed.isdigit()):
        proceed = input("Type 1 for yes and 0 for no: ")
    if proceed == "1":
        yeet = "true"
    elif proceed == "0":
        yeet = "false"
    else:
        proceed()


print("Please answer the following questions:")
print("--------------------------------------")
yeet = "false"
if yeet == "false":
    print("Did restarting the computer work?: ")
    proceed()
if yeet == "false":
    print("Did restarting the router work?:")
    proceed()
if yeet == "false":
    print("Aren't the cables in the router & modem plugged in unfirmly?:")
    proceed()
if yeet == "false":
    print("Did moving the router to a new location work?:")
    proceed()
if yeet == "false":
    print("Please get a new router and try again.")

if yeet == "true":
    print("Glad we could help, goodbye.")