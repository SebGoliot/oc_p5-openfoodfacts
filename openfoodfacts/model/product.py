from typing import Tuple


class Product():

    def __init__(self, product_id: int, name: str, category:int, score: str, stores: str):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.score = score
        self.stores = stores

    @classmethod
    def from_db_payload(cls, payload: Tuple[int, str, int, str, str]):
        """Create a Product object from a db row payload
        Should be a tuple with 5 items: id, name, category, score and stores
        """
        return cls(*payload)

    def get_tuple(self):
        return (
            self.product_id, self.name, self.category, self.score, self.stores)

    def __repr__(self):
        return (
            f'#{self.product_id}-{self.category}: {self.name} ^{self.score}\n'
            f'buy @ {self.stores}')


class Substitute():

    def __init__(self, substitute: Product, from_product: Product):
        self.substitute = substitute
        self.from_product = from_product
