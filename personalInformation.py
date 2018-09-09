name = input("Please write your (sir)name: ")
while len(name) == 0 :
    print("Please write your name without digits")
    name = input("Please write your (sir)name: ")

adress = input("Please write your streetname, city, state and zipcode: ")
while len(adress) == 0:
    adress = input("Please write your adress: ")

phone = input("Please write your phonenumber: ")
while len(phone) == 0 or (not phone.isdigit()):
    print("Please write your phonenumber without characters")
    phone = input("Please write your phonenumber: ")

major = input("Please write your college major down: ")
while len(major) == 0 :
    print("Please write your major's name without digits.")
    name = input("Please write your major's name: ")

print("Your name is: ", name)
print("Your adress is: ", adress)
print("Your phonenumber is: ", phone)
print("Your major is: ", major)