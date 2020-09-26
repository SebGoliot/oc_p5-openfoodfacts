import npyscreen
from model.product import Product, Substitute
from view.forms_const import *
from view.main_form import MainForm
from view.product_notif_form import ProductsNotifyForm
from view.products_form import ProductsForm
from view.search_form import SearchForm
from controller.db_manager import DbManager

class App(npyscreen.NPSAppManaged):

    def __init__(self):
        self.db_mgr = DbManager()
        self.categories = self.db_mgr.get_categories()
        self.subst_search = None
        super().__init__()


    def onStart(self):
        self.addForm(MAIN, MainForm, name='OpenFoodFacts')
        self.addForm(SEARCH_FORM, SearchForm, name='OpenFoodFacts - Search')


    def product_notify(self, product):
        try:
            self.removeForm(PRODUCT_NOTIFY)
        except KeyError:
            pass

        self.addForm(
            PRODUCT_NOTIFY,
            ProductsNotifyForm,
            name = product.name,
            product = product
            )
        self.switchForm(PRODUCT_NOTIFY)


    def late_add_form(self, form_id, **kwargs):
        name, products = None, None
        try:
            self.removeForm(form_id)
        except KeyError:
            pass

        if form_id == PRODUCTS_SEARCH:
            search = kwargs.get('search')
            if not search:
                raise RuntimeError("Missing kwarg: 'search'")
  
            products = self.db_mgr.find_product(search)
            name = 'OpenFoodFacts - Search Results'

        elif form_id == PRODUCTS_CATEGORY:
            category = kwargs.get('category')
            if not category:
                raise RuntimeError("Missing kwarg: 'category'")
            if isinstance(category, int):
                products = self.db_mgr.get_products_from_category(category)
            else:
                for cat in self.categories:
                    if cat[1] == category:
                        products = self.db_mgr.get_products_from_category(cat[0])
                        name = 'OpenFoodFacts - Search'
                        break

        elif form_id == PRODUCTS_FAVORITES:
            favorites = self.db_mgr.get_favorites()
            products = []
            print(favorites)
            for favorite in favorites:
                print(favorite)
                products.append(
                    Substitute(
                        Product.from_db_payload(
                            self.db_mgr.get_product_from_id(favorite[1])
                        ),
                        Product.from_db_payload(
                            self.db_mgr.get_product_from_id(favorite[2])
                        )
                    )
                )
            print(products)
            name='OpenFoodFacts - Favorites'

        try:
            self.addForm(
                form_id, ProductsForm,
                name=name, products = products
                )
            self.switchForm(form_id)
        except Exception as e:
            print(products)
            print(f'Oops :\n{e}')
            return
