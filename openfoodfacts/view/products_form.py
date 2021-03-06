import npyscreen
from openfoodfacts.model.product import Product, Substitute
from openfoodfacts.view.buttons import BackButton, ExitButton, ProductButton


class ProductsForm(npyscreen.FormMultiPage):
    """This form is used to display a list of product buttons. """

    def __init__(self, *args, **kwargs):
        self.products = kwargs.get("products")
        super().__init__(*args, **kwargs)

    def create(self):
        self.buttons = {}

        if isinstance(self.products[0], Substitute):
            self.products = [
                product.substitute.get_tuple() for product in self.products
            ]

        for product in self.products:
            self.buttons[str(product[0])] = Product.from_db_payload(product)
            self.add_widget_intelligent(
                ProductButton, name=product[1], product_id=product[0]
            )

        self.add(BackButton, name="Retour", relx=-24, rely=-3)
        self.add(ExitButton, name="Quit", relx=-12, rely=-3)
