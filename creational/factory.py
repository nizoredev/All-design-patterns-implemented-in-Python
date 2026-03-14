from typing import (
  Any,
  Union
)
from abc import ABC, abstractmethod

class InvalidObjArg(Exception): ...

class Apple:
  def __str__(self) -> str:
    return "Apple object"
    
class Pear:
  def __str__(self) -> str:
    return "Pear object"
    
class Orange:
  def __str__(self) -> str:
    return "Orange object"

class AbsFactory(ABC): 
  @staticmethod
  @abstractmethod
  def create(obj: str, *args, **kwargs) -> Any: ...

FoodFactoryTypes = Union[Apple, Pear, Orange]

class FoodFactory(AbsFactory):
  @staticmethod
  def create(obj: str, *args, **kwargs) -> FoodFactoryTypes:
    match obj.lower():
      case "apple":
        return Apple(*args, **kwargs)
      case "pear":
        return Pear(*args, **kwargs)
      case "orange":
        return Orange(*args, **kwargs)
      case _: 
        raise InvalidObjArg("You must provide a valid object name for the factory!")

def main() -> None:
  apple = FoodFactory.create("apple") # Might seem kinda unnecessary to use abstract base class if I don't instantiate it but whatever
  print(apple)

if __name__ == "__main__": 
  main()
