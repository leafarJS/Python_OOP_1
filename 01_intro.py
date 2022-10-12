"""
TODO todas son variables de tipo class str o int
item_1 = "Phone"
item_1_price = 100
item_1_quantity = 5
item_price_total = item_1_price * item_1_quantity

print(type(item_1)) # str
print(type(item_1_price)) # int
print(type(item_1_quantity)) # int
print(type(item_price_total)) # int 
"""

class Item:
  def calculate_total_price(self, x, y):
    return x * y

item_1 = Item()
item_1.name  = "Phone"
item_1.price = 100
item_1.quantity = 5
result = item_1.calculate_total_price(item_1.price, item_1.quantity)
print(result)

item_2 = Item()
item_2.name  = "laptop"
item_2.price = 1000
item_2.quantity = 3 
result = item_2.calculate_total_price(item_2.price, item_2.quantity)
print(result)














""" 
print(type(item_1)) # str
print(type(item_1.name)) # str
print(type(item_1.price)) # int
print(type(item_1.quantity)) # int
 """