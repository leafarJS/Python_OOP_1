
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.price)
item1.send_email()

item2 = Phone("myItem2", 1500, 3)
item2.apply_increment(0.2)
print(item2.price)
item2.send_email()