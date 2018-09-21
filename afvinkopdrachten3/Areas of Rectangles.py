def lAndW():
    global length
    global width
    length = input("Please input the length: ")
    while len(length) == 0 or (not length.isdigit()):
        length = input("Please input the length: ")
    length = int(length)
    width = input("Please input the width: ")
    while len(width) == 0 or (not width.isdigit()):
        width = input("Please input the width: ")
    width = int(width)

print("---------------------------------------------")
print("Compare your rectangles here: (rectangle1)   ")
lAndW()
length1 = length
width1 = width
rect1 = length1 * width1
print("Total:", rect1)
print("---------------------------------------------")
print("Compare your rectangles here: (rectangle2)   ")
lAndW()
length2 = length
width2 = width
rect2 = length2 * width2
print("Total:", rect2)
print("---------------------------------------------")
print("Your result:                                 ")
if rect1 > rect2:
    print("Rectangle 1 is bigger than rectangle 2.")
elif rect1 < rect2:
    print("Rectangle 2 is bigger than rectangle 1.")
else:
    print("Both rectangles are the same size.")
