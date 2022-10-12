
class Item:
  
  pay_rate = 0.8 #the pay rate after 20% discount
  
  def __init__(self, name:str, price:float, quantity=0)-> None:
    #run validation to the received arguments
    assert price >= 0, f"Price {price} is not greater or equal to zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
    
    #assing to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    
  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate


item_1 = Item("Phone", 100, 5)
item_1.apply_discount()
print(item_1.price)

item_2 = Item("laptop", 1000, 3)
item_2.apply_discount()
print(item_2.price)
""" 
result2 = item_2.calculate_total_price()
print(result2)
result2.apply_discount()
print(result2) 
"""


print(Item.__dict__) # all the attribute for Class level
print(item_1.__dict__) # all the attribute  for instance level



""" 
print(type(item_1)) # str
print(type(item_1.name)) # str
print(type(item_1.price)) # int
print(type(item_1.quantity)) # int
 """