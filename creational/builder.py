from typing import (
    Any,
    Union
)
from abc import ABC, abstractmethod

class Couch:
    def __init__(self) -> None: 
        self._color = None
        self._material = None
        self._size = None
        self._weight  = None

    def __str__(self) -> str:
        return f"{self._size} {self._color} couch made of {self._material} that is {self._weight}"

class AbsBuilder(ABC):
    @abstractmethod
    def build(self) -> Any: ...

class CouchBuilder(AbsBuilder):
    def __init__(self) -> None:
        self._couch = Couch()

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

    def build(self) -> Couch:
        return self._couch

class Client:
    def __init__(self) -> None: ...
    
    def make_couch(self) -> Couch:
        couch_builder = CouchBuilder()
        couch_builder.set_color("cyan")
        couch_builder.set_material("leather")
        couch_builder.set_size("big")
        couch_builder.set_weight("heavy")
        return couch_builder.build()

def main() -> None:
    client = Client()
    couch = client.make_couch()
    print(couch)

if __name__ == "__main__":
    main()