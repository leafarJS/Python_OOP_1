
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
    
  def __repr__(self):
    #return f"Item('{self.name}', {self.price}, {self.quantity}')"
    #TODO para mejorar la herencia
    return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity}')"

class Phone(Item):
  def __init__(self, name:str, price:float, quantity=0, broken_phones =0)-> None:
    # call to super function to have access to all attributes and methods 
    super().__init__(name, price, quantity)
    #run validation to the received arguments
    assert price >= 0, f"broken_phones {broken_phones} is not greater or equal to zero!"
     #Assing to self object 
    self.broken_phones = broken_phones
    



cell1 = Phone("Motorola", 135,45,2)
print(cell1.calculate_total_price())

print(Item.all)
print(Phone.all)