from typing import (
    Any,
    Union
)
from abc import ABC, abstractmethod

# Create the Couch class but not give it any valid attributes yet.
class Couch:
    def __init__(self) -> None: 
        self._color = None
        self._material = None
        self._size = None
        self._weight  = None

    def __str__(self) -> str:
        return f"{self._size} {self._color} couch made of {self._material} that is {self._weight}"

# Create the abstract builder interface.
class AbsBuilder(ABC):
    """
    Abstract builder.
    """
    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def build(self) -> Any: ...

# Create the abstract director interface.
class AbsDirector(ABC):
    """
    Abstract director.
    """
    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def direct(self) -> Any: ...

# Create the CouchBuilder class, inheriting from the abstract builder class
class CouchBuilder(AbsBuilder):
    """
    Couch builder.
    """
    def __init__(self) -> None:
        self._couch = Couch()
    
    # Define all the methods that edit all the attributes.
    def set_color(self, color: str) -> Couch:
        self._couch._color = color
        return self._couch
    
    def set_material(self, material: str) -> Couch:
        self._couch._material = material
        return self._couch

    def set_size(self, size: str) -> Couch:
        self._couch._size = size
        return self._couch
    
    def set_weight(self, weight: str) -> Couch:
        self._couch._weight = weight
        return self._couch

    # Override the "build" method and give it it's custom functionality.
    def build(self) -> Couch:
        return self._couch

# Create the CouchDirector class, inheriting from the abstract director class
# The couch director is responsible for giving the instructions to the builder.
class CouchDirector(AbsDirector):
    """
    Couch director.
    """
    def __init__(self, builder: CouchBuilder):
        self._builder = builder

    def direct(self) -> CouchBuilder:
        self._builder.set_color("cyan")
        self._builder.set_material("leather")
        self._builder.set_size("big")
        self._builder.set_weight("heavy")
        return self._builder # Returns the builder after setting everything.
    
class Client:
    def __init__(self) -> None:
        self._builder = CouchBuilder()
        self._director = CouchDirector(self._builder)

    def make_couch(self) -> Couch:
        return self._director.direct().build()

def main() -> None:
    client = Client()
    couch = client.make_couch()
    print(couch)

if __name__ == "__main__":
    main()