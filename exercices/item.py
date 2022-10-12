
import csv

class Item:
  pay_rate = 0.8 #the pay rate after 20% discount
  all = []
  
  def __init__(self, name:str, price:float, quantity=0)-> None:
    
    #run validation to the received arguments
    assert price >= 0, f"Price {price} is not greater or equal to zero!"
    assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
    
    #assing to self object
    self.__name = name
    self.__price = price
    self.quantity = quantity
    
    #called all instances
    Item.all.append(self)
    
  @property
  def price(self):
    return self.__price  

  def apply_discount(self):
    self.__price = self.__price * self.pay_rate
    
  def apply_increment(self, increment_value):
    self.__price = self.__price + self.price * increment_value
  
    
  @property
    #property decorator = read-Only Attribute
  def name(self):
    return self.__name
  
  @name.setter
  # modificar un atributo encapsulado
  def name(self, value):
    if len(value) > 10:
      raise Exception("The name is too long")
    self.__name = value
    
  def calculate_total_price(self):
    return self.__price * self.quantity
  
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
    return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity}')"
  
  
  #TODO abstraction
  def __connect(self, smpt_server):
    pass
  
  def __preparate_body(self):
    return f""" 
    Hello Someone
    We have {self.name} {self.quantity} times.
    Regards, Jorge
    """
  def __send(self):
    pass
  
  def send_email(self):
    self.__connect('')
    self.__preparate_body() 
    self.__send()
    
