from item import Item 
from phone import Phone


item1 = Item("myItem", 750)

item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)
item1.send_email()

item2 = Phone("myItem2", 1500, 3)
item2.apply_increment(0.2)
item2.apply_discount()
print(item2.price)
item2.send_email()


#setting an attribute
item1.name = "othername"

#getting an attribute
print(item1.name)

#item1.name = "otherItem" #AttributeError: can't set attribute 'name'

"""
print(item1.name) # se puede ver y cambiar
print(item1._name) # no se puede cambiar
print(item1.__name) # no se puede ver ni cambiar """