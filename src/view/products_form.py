import npyscreen
from model.product import Product
from view.buttons import BackButton, ExitButton, ProductButton

class ProductsForm(npyscreen.FormMultiPage):

    def __init__(self, *args, **kwargs):
        self.products = kwargs.get('products')
        super().__init__(*args, **kwargs)

    def create(self):
        self.buttons = {}

        for product in self.products:
            self.buttons[str(product[0])] = Product.from_db_payload(product)
            self.add_widget_intelligent(
                ProductButton, name=product[1], product=product)

        self.add(BackButton, name='Back', relx=-24, rely=-3)
        self.add(ExitButton, name='Exit', relx=-12, rely=-3)
