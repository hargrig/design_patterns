# Singleton pattern is one of the simplest design patterns. 
# This type of design pattern comes under creational pattern as this pattern provides 
# one of the best ways to create an object.
# This pattern involves a single class which is responsible to create an object 
# while making sure that only single object gets created. 
# This class provides a way to access its only object which can be accessed directly 
# without need to instantiate the object of the class.


class SingletonClass(object):
    def __init__(self):
        self.data = 10

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)

        return cls.instance


singleton1 = SingletonClass()
singleton2 = SingletonClass()

# print(id(singleton1))
# print(id(singleton2))
