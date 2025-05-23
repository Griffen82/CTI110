# Michael Urbi
# May 4, 2025
# Final
# Using what we learned of loops, functions, and modules for a check-out program

# Github CTI 110-002 repository link: github.com/Griffen82/CTI110

# Function to display available items
def show_avail_items(grocer):
    item = len(grocer)
    product = list(grocer.keys())
    price = list(grocer.values())
    print(f"{'Grocery Item':<50} {'Price'}")
    print("-"*60)
    for i in range(1, item+1):
        call = i - 1
        print(f'{product[call]:<50} {"$"+price[call]}')

    print("-"*60, "\n")
    return product

# Function to add items to user cart
def grocery_list(items):
    print("*Welcome to the Grocery Checkout*\n")
    choice = input("Enter an item to add to the cart or type \"end\" to stop adding items: ")
    basket = []

    while choice.lower() != "end":
        if choice in items:
            basket.append(choice)
            choice = input("Enter an item to add to the cart or type \"end\" to stop adding items: ")
        else:
            print("That item is not in stock.")
            choice = input("Enter an item to add to the cart or type \"end\" to stop adding items: ")
    else:
        return basket

# Function to display items in user's cart
def show_cart(basket):
    cart = {}
    print()
    print("The items currently in your cart are:")
    item = len(basket)
    for i in range(1, item+1):
        qty = basket.count(basket[(i - 1)])
        cart.update({basket[(i - 1)]: qty})
    print(f'{"Item":<50} {"Quantity"}')
    print("-"*60)
    l_cart = len(cart)
    for i in range(1, l_cart+1):
        product = list(cart.keys())
        product.sort()
        print(f'{product[(i - 1)]:<50} {cart.get(product[(i - 1)])}')

# Function displaying itemized receipt
def calc_total(cart, cost):
    print()
    print("Grocery Checkout Receipt")
    print(f'{"Item":<15} {"Ind. Price":<15} {"Quantity":<15} {"Total"}')
    print("-"*60)
    basket = {}
    subtotal = 0
    items = len(cart)
    for i in range(1, items+1):
        qty = cart.count(cart[(i - 1)])
        basket.update({cart[(i - 1)]: qty})
        subtotal = subtotal + float(cost.get(cart[(i-1)]))
    l_basket = len(basket)
    for i in range(1, l_basket+1):
        product = list(basket.keys())
        product.sort()
        price = str(cost.get(product[(i-1)]))
        it_total = (float(price) * int(basket.get(product[(i - 1)])))
        sit_tot = str(f'{it_total:.2f}')
        print(f'{product[(i-1)]:<15} {"$"+price:<15} {basket.get(product[i - 1]):<15} {"$"+sit_tot}')
    print()
    stot = str(f'{subtotal:.2f}')
    print(f'{"SUBTOTAL: ":<30} {"$"+stot}'"\n")
    tax = str(f'{(subtotal * .02):.2f}')
    print(f'{"TAX: ":<30} {"$"+tax}')
    total = str(f'{(float(tax) + float(subtotal)):.2f}')
    print(f'{"TOTAL: ":<30} {"$"+total}')
    return total

# Function dispensing change to user
def payment(r_change):
    print("Dispensing...\n")
    i_change = float(r_change) * 100
    change = int(i_change)
    if change==0:
        print("No change")
    
    dollars = change//100
    quarters = (change - (dollars*100))

    if dollars > 0:
        print(dollars, end=' ')
        if dollars == 1:
            print("Dollar")
        else:
            print("Dollars")

    quarter = quarters//25
    dimes = (quarters - (quarter*25))

    if quarter > 0:
        print(quarter, end=' ')
        if quarter == 1:
            print("Quarter")
        else:
            print("Quarters")

    dime = dimes//10
    nickels = (dimes - (dime*10))

    if dime > 0:
        print(dime, end=' ')
        if dime == 1:
            print("Dime")
        else:
            print("Dimes")

    nickel = nickels//5
    pennies = (nickels - (nickel*5))

    if nickel > 0:
        print(nickel, end=' ')
        if nickel == 1:
            print("Nickel")
        else:
            print("Nickels")

    penny = pennies//1

    if penny > 0:
        print(penny, end=' ')
        if penny == 1:
            print("Penny")
        else:
            print("Pennies")

# Main function with store dictionary & asking user total cash used to pay for shopping            
def shopping():

    grocer = {
        "apples":"3.69",
        "berries":"4.00",
        "chocolate":"2.89",
        "turkey":"6.99",
        "cheese":"4.00",
        "pepsi":"7.89",
        "eggs":"3.50",
        "bread":"3.00"
        }
    i_want = show_avail_items(grocer)
    i_have = grocery_list(i_want)
    show_cart(i_have)
    total_owed = calc_total(i_have, grocer)
    total = float(total_owed)
    print("\n\nYou owe $" +total_owed+ " for the groceries.\n")
    s_pay = input("How much cash will you put in the self-checkout machine? ")
    pay = float(s_pay.strip("$"))
    change = pay - total
    f_change = f'{change:.2f}'
    s_change = str(f'{change:.2f}')
    print("Your change is: $"+s_change+ ".""\n")
    payment(f_change)
shopping()
