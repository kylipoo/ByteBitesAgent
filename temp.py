from models import Customer,  Menu, Transaction, FoodItem

burger = FoodItem("Spicy Burger", 9.99, "MainCourse", 4.5)
menu = Menu()
menu.items.append(burger)
soda = FoodItem("Cola", 1.99, "Drink", 4.0)
menu.items.append(soda)
icecream = FoodItem("Vanilla Ice Cream", 3.99, "Dessert", 4.8)
salad = FoodItem("Caesar Salad", 7.99, "Appetizer", 4.2)
fries = FoodItem("French Fries", 2.99, "Side", 4.3)
pasta = FoodItem("Pasta Alfredo", 11.99, "MainCourse", 4.6)
menu.items.append(icecream)

newOrder = Transaction()
newOrder.items = [] 
newOrder.add_item(burger)
newOrder.add_item(soda)
newOrder.add_item(icecream)
newOrder.add_item(burger)
print(newOrder.get_total())

john = Customer("John Doe")
john.purchase_history.append(newOrder)

healthyOrder = Transaction()
healthyOrder.add_item(salad)
healthyOrder.add_item(pasta)
john.purchase_history.append(healthyOrder)



def test_correct_transaction_total():
    assert newOrder.get_total() == 9.99 + 1.99 + 3.99 + 9.99, "Total should be the sum of item prices"

def test_transaction_history():
    assert len(john.purchase_history) == 2, "John should have 2 transactions in his history"
    assert john.purchase_history[0].get_total() == 9.99 + 1.99 + 3.99 + 9.99, "First transaction total should match"
    assert john.purchase_history[1].get_total() == 7.99 + 11.99, "Second transaction total should match"
