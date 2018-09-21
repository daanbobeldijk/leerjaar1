
proceed = input("Please input an integer: ")
while len(proceed) == 0 or (not proceed.isdigit()):
    proceed = input("Please input an integer: ")
proceed = int(proceed)
if proceed > 0:
    print("Positive.")
elif proceed < 0:
    print("Negative.")
elif proceed == 0:
    print("Zero.")
if proceed % 2 == 0:
    print("Even.")
else:
    print("Odd.")