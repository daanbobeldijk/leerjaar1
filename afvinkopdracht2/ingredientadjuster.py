# sugar = 1.5
# butter = 1
# flour = 2.75
#--------------for 48 cookies
sugarOne = 1.5/48
butterOne = 1/48
flourOne = 2.75/48
#for 1 cookie

cookies = input("How many cookies do you want to make: ")
while len(cookies) == 0 or (not cookies.isdigit()):
    cookies = input("Please write down the amount of cookies you want to make: ")

cookiesStr = cookies
cookies = int(cookies)
sugarOne = str(round(sugarOne * cookies,2))
butterOne = str(round(butterOne * cookies,2))
flourOne = str(round(flourOne * cookies,2))

print("To bake ", cookiesStr, "you'll need the following amount of cups:", "\n", sugarOne, " cups of sugar", "\n", butterOne, " cups of butter", "\n", flourOne, " cups of flour")
