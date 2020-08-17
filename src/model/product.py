

class Product():

    def __init__(self, code: int, name: str, stores: str, grade: int):
        self.code = code
        self.name = name
        self.stores = stores
        self.grade = grade

    def __repr__(self):
        return f'#{self.code}:{self.name} @{self.stores} ^{self.grade}'
