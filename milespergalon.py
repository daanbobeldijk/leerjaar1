drivenMiles= input("The amount of miles you drove: ")
while len(drivenMiles) == 0 or (not drivenMiles.isdigit()):
    drivenMiles = input("Please write down the amount of miles you drove: ")

gallonsGas = input("The amount of gallons gas you've used: ")
while len(gallonsGas) == 0 or (not gallonsGas.isdigit()):
    gallonsGas = input("Please write down the amount of gallons gas you've used: ")

drivenMiles = int(drivenMiles)
gallonsGas = int(gallonsGas)
mpg = drivenMiles / gallonsGas

print("Your car drove ", mpg, "miles per gallon.")