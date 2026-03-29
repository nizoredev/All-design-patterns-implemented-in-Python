from typing import (
    Any,
    Union
)
from abc import ABC, abstractmethod
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format="[%(asctime)s] DEBUG: %(message)s"
# )
# logger = logging.getLogger()

# Approach 1: Metaclass approach. 
# Use a metaclass to change the behavior of the class object so that the class doesn't allow
# more than one instance to be created.
# Advantages:
# - Allows any class that uses this metaclass to have this functionality.
# Disadvantages:
# - More complex
class Singleton(type):
    def __new__(cls, name, bases, dct) -> object:
        __class = super().__new__(cls, name, bases, dct) # Get the class object from __new__ but not return it yet.
        setattr(__class, "_instance", None) # Dynamically set _instance attribute to None (to check if the class has already been instantiated).
        original_new = getattr(__class, "__new__") # Get the original __new__ method for future use (because it will be overridden).

        def new(__cls, *args, **kwargs) -> object: # Using double underscore names to prevent naming conflicts.
            if (ins := getattr(__cls, "_instance")) is not None: # Check if _instance is not None, meaning an instance has already been created.
                return ins # Returns the already-existing instance object to prevent new instances from being created.
            
            # If the class hasn't been instantiated, it carries on and creates the instance.
            ins = original_new(__cls, *args, **kwargs) # Use original_new to call the original __new__ method of the class
            setattr(__class, "_instance", ins) # Sets the _instance attribute to whatever was returned by the original_new function (the instance)
            return ins # Returns the instance object
            
        setattr(__class, "__new__", new) # Overrides the __new__ method of the class with the created "new" function to change it's behaviour.

        return __class # At last, it returns the class object.
    
# The class' behaviour will be modified by the metaclass.
class MetaCat(metaclass=Singleton):
    """
    Cat class that uses the Singleton design pattern by using the Singleton metaclass.
    """
    def __init__(self) -> None: ... 

# Approach 2: Normal class approach.
# Statically set the _instance attribute and override the __new__ method of the class to check
# if an instance has already been created.
# Advantages: 
# - Simpler
# Disadvantages:
# - Allows only the classes with this implementation to have the functionality.
class NormCat:
    """
    Cat class that uses the Singleton design pattern by normally changing the class' behavior.
    """
    _instance = None

    def __new__(cls, *args, **kwargs) -> object:
        if cls._instance is not None:
            return cls._instance
        
        cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None: ...
    
def main() -> None:
    # Metaclass approach
    cat = MetaCat()
    cat2 = MetaCat()
    print(cat is cat2) # Prints "True" because both variables point to the same object.

    # Normal class approach
    cat3 = NormCat()
    cat4 = NormCat()
    print(cat3 is cat4) # Prints "True" because both variables point to the same object.

if __name__ == "__main__":
    main()

