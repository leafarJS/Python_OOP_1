from item import Item

class Phone(Item):
  def __init__(self, name:str, price:float, quantity=0, broken_phones =0)-> None:
    # call to super function to have access to all attributes and methods 
    super().__init__(name, price, quantity)
    #run validation to the received arguments
    assert price >= 0, f"broken_phones {broken_phones} is not greater or equal to zero!"
    #Assing to self object 
    self.broken_phones = broken_phones
    

