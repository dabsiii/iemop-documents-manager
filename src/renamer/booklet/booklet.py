from abc import ABC, abstractmethod
from typing import List


class Booklet(ABC):

    @abstractmethod
    def __init__(self, final_number: int):
        self.final_number = final_number

    @abstractmethod
    def get_numbers(self) -> List[int]: ...

    @abstractmethod
    def get_starting_number(self) -> int: ...

    @abstractmethod
    def get_final_number(self) -> int: ...

    def __eq__(self, other):
        if isinstance(other, Booklet):
            return self.final_number == other.final_number
        return False

    def __hash__(self):
        return hash(self.final_number)

    def __lt__(self, other):
        if isinstance(other, Booklet):
            return self.final_number < other.final_number
        return NotImplemented

    def __repr__(self):
        return f"Booklet {self.final_number-49}-{self.final_number}"
