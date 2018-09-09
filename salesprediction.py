sales = input("Projected amount of total sales: ")
while len(sales) == 0 or (not sales.isdigit()):
    sales = input("Projected amount of total sales: ")

sales = int(sales)
sales = round(sales * 1.23 - sales, 2)
sales = str(sales) + ""

print("The total amount of profit made is: ", sales)