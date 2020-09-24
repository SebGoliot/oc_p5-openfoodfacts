import npyscreen
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

        try:
            products = kwargs.get('products')
        except KeyError:
            pass

        if form_id == PRODUCTS_SEARCH:
            try:
                search = kwargs.get('search')
            except KeyError:
                return

            products = self.db_mgr.find_product(search)
            name = 'OpenFoodFacts - Search Results'

        elif form_id == PRODUCTS_CATEGORY:
            category = None
            try:
                for cat in self.categories:
                    if cat[1] == kwargs.get('category'):
                        category = cat[0]
            except KeyError:
                return
            
            if category:
                products = self.db_mgr.get_products_from_category(category)
                name='OpenFoodFacts - Search'

        elif form_id == PRODUCTS_FAVORITES:
            products = self.db_mgr.get_favorites()
            name='OpenFoodFacts - Favorites'

        try:
            self.addForm(form_id, ProductsForm, name=name, products = products)
            self.switchForm(form_id)
        except:
            return
