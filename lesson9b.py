from lesson9 import KitchenAppliance


class CoffeeMachine(KitchenAppliance):
    Coffee_Types = ["Espresso", "Americano", "Cappuccino", "Latte", "Mocha"]

    def __init__(self, model_number='101', brand='Xtreme Caffeine'):
        if coffee_type not in CoffeeMachine.Coffee_Types:
            CoffeeMachine.Coffee_Types.append(coffee_type)
        super().__init__(model_number, brand)
        self.coffee_type = coffee_type

coffee_type = input("What type of coffee would you like? ")
if coffee_type not in CoffeeMachine.Coffee_Types:
   CoffeeMachine.Coffee_Types.append(coffee_type)

print('Making you a ' + coffee_type + ' ☕')
print('Thanks for using Xtreme Caffeine')