# ByteBites Models
# Classes:
# Customer     - Represents a user with a name and a purchase history (list of Transactions).
# Menu         - Holds a list of FoodItems and supports filtering by category.
# Transaction  - Records a single order: a list of FoodItems and a computed total.
# FoodItem     - A menu item with a name, price, category, and popularity rating.
#
# Relationships:
#   Customer  1 -- * Transaction  (a customer places many transactions)
#   Menu      1 -- * FoodItem     (a menu contains many food items)
#   Transaction * -- * FoodItem   (a transaction includes many food items)

class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items: list[FoodItem] = []

    def filter_by_category(self, cat: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == cat]


class Transaction:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def get_total(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Transaction] = []
