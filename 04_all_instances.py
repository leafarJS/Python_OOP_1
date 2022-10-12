
class Item:
  
  pay_rate = 0.8 #the pay rate after 20% discount
  all = []
  
  def __init__(self, name:str, price:float, quantity=0)-> None:
    #run validation to the received arguments
    assert price >= 0, f"Price {price} is not greater or equal to zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
    
    #assing to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    
    #called all instances
    Item.all.append(self)
    
  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate
    
  def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity}')"


item1 = Item("Phone", 100, 9)
item2 = Item("laptop", 400, 2)
item3 = Item("mouse", 200, 7)
item4 = Item("cable", 800, 4)
item5 = Item("monitor", 600, 6)

print(Item.all)

for i in Item.all:
  print(i.name)