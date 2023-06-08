from menu import Menu, MenuItem
from coffee_marker import CoffeeMarker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMarker()
menu = Menu()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"what would you like? ({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink != "NotFound":
            is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
            is_payment_successful = money_machine.make_payment(drink.cost)
            if (is_resource_sufficient and is_payment_successful):
                coffee_maker.make_coffee(drink)
