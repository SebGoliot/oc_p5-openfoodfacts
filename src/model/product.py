from typing import Tuple


class Product():

    def __init__(self, code: int, name: str, stores: str, grade: str):
        self.code = code
        self.name = name
        self.stores = stores
        self.grade = grade

    @classmethod
    def from_db_payload(cls, payload: Tuple[int, str, str, str]):
        """Create a Product object from a db row payload
        Should be a tuple containing 4 items: code, name, stores and grade
        """
        return cls(*payload)

    def __repr__(self):
        return f'#{self.code}:{self.name} @{self.stores} ^{self.grade}'
