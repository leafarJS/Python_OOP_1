
class Item:
  def __init__(self, name:str, price:float, quantity:float)-> None:
    #run validation to the received arguments
    assert price >= 0, f"Price {price} is not greater or equal to zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
    
    #assing to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def calculate_total_price(self):
    return self.price * self.quantity

item_1 = Item("Phone", 100, 5)
item_2 = Item("laptop", 1000, 3)

result1 = item_1.calculate_total_price()
print(result1)

result2 = item_2.calculate_total_price()
print(result2)














""" 
print(type(item_1)) # str
print(type(item_1.name)) # str
print(type(item_1.price)) # int
print(type(item_1.quantity)) # int
 """