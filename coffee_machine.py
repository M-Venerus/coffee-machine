from assets import resources
from assets import drinks


def drink_choice():
    """Prompt user for drink selection. Secret value 'report' generates resource levels."""
    user_drink = input("What beverage would you like? (espresso/latte/cappuccino): ")
    if user_drink == "report":
        money = "{:.2f}".format(resources["money"])
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee Beans: {resources["coffee"]}g\nMoney: ${money}')
        return "reset"
    else:
        return user_drink
    

def check_resources(drink):
    """Check if resources are available for selected drink."""
    not_available = False
    for resource in drinks[drink]:
        if resource != "price":
            if drinks[drink][resource] > resources[resource]:
                print(f"Sorry, there is not enough {resource}.\n")
                not_available = True
    if not_available:
        main()
            

def drink_price(drink):
    """Return price of selected drink."""
    drink_price = drinks[drink]["price"]
    drink_price_formatted = "{:.2f}".format(drink_price)
    print(f"A {drink} costs $ {drink_price_formatted}")
    return drink_price


def get_money():
    """Prompt user for coin inputs. Return total dollar value."""
    print("Please enter change.")
    nickles = 0.05 * int(input("How many nickles?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    quarters = 0.25 * int(input("How many quarters?: "))
    dollars = 1.00 * int(input("How many dollars?: "))
    total_money = nickles + dimes + quarters + dollars
    return total_money
    
    
def check_and_deposit_money(price, money_inputted):
    """Check if user money inputted is sufficient for drink cost. Deposite money into resources."""
    if money_inputted >= price:
        refund = money_inputted - price
        if refund > 0:
            refund = "{:.2f}".format(refund)
            print(f"Here is your change: ${refund}")
        resources["money"] += price
    else:
        print("Sorry that is not enough money.\n")
        main()
        

def make_drink(drink):
    """Make user selected drink and subtract used resources from resources dict."""
    for resource in drinks[drink]:
        if resource != "price":
            resources[resource] -= drinks[drink][resource]
    print(f"Here is your fresh {drink}. Enjoy!\n")


def main():
    """Execute coffee machine simulation."""
    drink = drink_choice()
    if drink == "reset":
        print("\n")
        main()
    else:
        check_resources(drink)
        price = drink_price(drink)
        money_inputted = get_money()
        check_and_deposit_money(price, money_inputted)
        make_drink(drink)
        main()

main()