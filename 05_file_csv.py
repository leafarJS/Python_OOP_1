
import csv
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
  
  @classmethod  
  def instaniate_from_csv(cls):
    with open('data.csv', 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)
    
    for i in items:
      Item(
        name = i.get('name'),
        price = float(i.get('price')),
        quantity = int(i.get('quantity'))
      )  
      
  @staticmethod
  def is_integer(num):
    # we will count out the floats that are point zero
    # for i.e: 5.0, 10.0
    if isinstance(num, float):
      # count out the floats that are point zero
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False
    
  def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity}')"


print(Item.is_integer(7))
print(Item.is_integer(8.3))