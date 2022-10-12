#When to use class methods and when to use static methods?
class Item:
  
  @staticmethod
  def is_integer(num):
    """ 
    this should do something that has a relationship with the class, but not something that must be unique per instance!
    
    esto debería hacer algo que tenga una relación con la clase, ¡pero no algo que deba ser único por instancia!
    """
  @classmethod
  def instatiate_from_something(cls):
    """
    this should do something that has a relationship with the class, but usually, those are used to manipulate different structures of data, to instantiate objects, like we have done whit CSV
    
    esto debería hacer algo que tenga una relación con la clase, pero por lo general, se usan para manipular diferentes estructuras de datos, para crear instancias de objetos, como lo hemos hecho con CSV
    """
    
    
item1 = Item()
item1.is_integer(5)
item1.instatiate_from_something()