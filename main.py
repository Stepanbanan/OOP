from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()

cofee_maker = CoffeeMaker()
cofee_maker.report()

menu=Menu()


ieslegts=True

while ieslegts:
    iespejas= menu.get_items()
    izvele=input(f"Ko tu velies? ({iespejas})")
    if izvele=="off":
        ieslegts= False
    elif izvele == "report":
        money_machine.report()
        cofee_maker.report()
    else:
        dzeriens = menu.find_drink(izvele)
        if cofee_maker.is_resource_sufficient(dzeriens) and money_machine.make_payment(dzeriens.cost):
            cofee_maker.make_coffee(dzeriens)
            
        #print(cofee_maker.is_resource_sufficient(dzeriens))

