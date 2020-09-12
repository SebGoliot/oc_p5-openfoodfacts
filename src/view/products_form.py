import npyscreen
from view.buttons import BackButton, ExitButton, ProductButton

class ProductsForm(npyscreen.FormMultiPage):

    def create(self):
        products = self.parentApp.db_mgr.get_products_from_category(
            self.parentApp.get_category_id())

        for i, product in enumerate(products):
            if not i % 24 and i:
                self.add_page()
            self.add(ProductButton, name=product[1])

        self.add(BackButton, name='Back', relx=-24, rely=-3)
        self.add(ExitButton, name='Exit', relx=-12, rely=-3)
