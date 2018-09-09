tt = input("The time you've traveled in hours: ")
while len(tt) == 0 or (not tt.isdigit()):
    sales = input("Please write down the time you've traveled in hours: ")

tt = int(tt)
speed = 70
distance = tt*speed

print("You've traveled: ", distance, "miles in ", tt, "hours.")
