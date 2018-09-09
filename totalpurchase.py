item1 = input("The price of your first item: $")
while len(item1) == 0 or (not item1.isdigit()):
    sales = input("Please write down the price of your first item: $")

item2 = input("The price of your second item: $")
while len(item2) == 0 or (not item2.isdigit()):
    sales = input("Please write down the price of your second item: $")

item3 = input("The price of your third item: $")
while len(item3) == 0 or (not item3.isdigit()):
    sales = input("Please write down the price of your third item: $")

item4 = input("The price of your fourth item: $")
while len(item4) == 0 or (not item4.isdigit()):
    sales = input("Please write down the price of your fourth item: $")

item5 = input("The price of your fifth item: $")
while len(item5) == 0 or (not item5.isdigit()):
    sales = input("Please write down the price of your fifth item: $")
item1 = int(item1); item2 = int(item2); item3 = int(item3); item4 = int(item4); item5 = int(item5)
subtotal = item1 + item2 + item3 + item4+ item5
print("The subtotal of your purchase is: $", subtotal)
print("The amount of tax on these purchases are 7%.")
print("The total price is: $", round(subtotal*1.07, 2))