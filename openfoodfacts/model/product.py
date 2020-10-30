from typing import Tuple


class Product:
    """The Product class represents a product and contains all the
    relevant data needed by the application
    """

    def __init__(
        self, product_id: int, name: str, category: int, score: str, stores: str
    ):
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
        """Returns a tuple containing all the data of a Product instance """
        return (
            self.product_id,
            self.name,
            self.category,
            self.score,
            self.stores,
        )

    def __repr__(self):
        return (
            f"#{self.product_id}-{self.category}: {self.name} ^{self.score}\n"
            f"buy @ {self.stores}"
        )


class Substitute:
    """The Substitute class represents a substitute entry.
    It stores two Product objects, a substitute and a substitued product
    """

    def __init__(self, substitute: Product, from_product: Product):
        self.substitute = substitute
        self.from_product = from_product
