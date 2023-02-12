# Builder pattern builds a complex object using simple objects and 
# using a step by step approach. 
# This type of design pattern comes under creational pattern as 
# this pattern provides one of the best ways to create an object.
# A Builder class builds the final object step by step. 
# This builder is independent of other objects.

from abc import ABC, abstractmethod


# PACKINGS
class Packing(ABC):
    @abstractmethod
    def pack(self):
        raise NotImplemented

class Wrapper(Packing):
    def pack(self) -> str:
        return "Wrapper"

class Bottle(Packing):
    def pack(self) -> str:
        return "Bottle"


# ITEMS
class Item(ABC):
    @abstractmethod
    def name(self) -> str:
        raise NotImplemented

    @abstractmethod
    def packing(self) -> Packing:
        raise NotImplemented

    @abstractmethod
    def price(self) -> float:
        raise NotImplemented


class Burger(Item, ABC):
    def packing(self):
        return Wrapper()

    @abstractmethod
    def price(self) -> float:
        raise NotImplemented

class VegBurger(Burger):
    def price(self) -> float:
        return 10.5
    
    def name(self) -> str:
        return "Veg Burger"

class ChickenBurger(Burger):
    def price(self) -> float:
        return 20.5

    def name(self) -> str:
        return "Chicken Burger"


class Drink(Item, ABC):
    def packing(self):
        return Bottle()

    @abstractmethod
    def price(self) -> float:
        raise NotImplemented

class Coke(Drink):
    def price(self) -> float:
        return 5.0
    
    def name(self) -> str:
        return "Coke"

class Pepsi(Drink):
    def price(self) -> float:
        return 3.0
    
    def name(self) -> str:
        return "Pepsi"

class Water(Drink):
    def price(self) -> float:
        return 2.0
    
    def name(self) -> str:
        return "Water"


# BUILDERS
class Meal:
    def __init__(self):
        self.meal_items = []

    def add_item(self, item: Item):
        self.meal_items.append(item)

    def get_meal_cost(self):
        cost_summary = 0.0

        for item in self.meal_items:
            cost_summary += item.price()
    
        return cost_summary
    
    def show_items(self):
        for item in self.meal_items:
            print(f"Item: {item.name()}")
            print(f"Packing: {item.packing().pack()}")
            print(f"Price: {item.price()}")
            print(f"--------")

class MealBuilder():
    def prepare_veg_meal(self) -> Meal:
        meal = Meal()

        meal.add_item(VegBurger())
        meal.add_item(Water())

        return meal

    def prepare_nonveg_meal(self) -> Meal:
        meal = Meal()

        meal.add_item(ChickenBurger())
        meal.add_item(Coke())

        return meal


class DemoBuilderPattern():
    def main(self):
        meal_builder = MealBuilder()

        veg_meal = meal_builder.prepare_veg_meal()
        print(f"Veg Meal\n")
        veg_meal.show_items()
        print(f"Total Cost: {veg_meal.get_meal_cost()}")
    
        print("\n")

        non_veg_meal = meal_builder.prepare_nonveg_meal()
        print(f"Non-Veg Meal\n")
        non_veg_meal.show_items()
        print(f"Total Cost: {non_veg_meal.get_meal_cost()}")


if __name__ == "__main__":
    demo = DemoBuilderPattern()
    demo.main()
