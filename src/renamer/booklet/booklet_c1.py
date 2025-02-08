from src.renamer.booklet.booklet import Booklet


from typing import List


class BookletC1(Booklet):
    def __init__(self, invoice_number: int):
        self._starting_number = self._get_starting_number(invoice_number)
        self._final_number = self._starting_number + 50 - 1

        super().__init__(self._final_number)

    def get_numbers(self) -> List[int]:
        return list(range(self._starting_number, self._final_number + 1))

    def get_starting_number(self) -> int:
        return self._starting_number

    def get_final_number(self) -> int:
        return self._final_number

    @staticmethod
    def _get_starting_number(invoice_number):

        remainder = invoice_number % 50
        start = invoice_number - remainder + 1
        if start > invoice_number:
            return start - 50
        return start
