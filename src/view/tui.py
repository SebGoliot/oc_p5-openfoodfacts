import npyscreen
from view.forms_const import *
from view.main_form import MainForm
from view.products_form import ProductsForm
from view.search_form import SearchForm
from controller.db_manager import DbManager
from view.search_result_form import SearchResultForm

class App(npyscreen.NPSAppManaged):

    def __init__(self):
        self.db_mgr = DbManager()
        self.categories = self.db_mgr.get_categories()
        self.current_category = ''
        self.search = ''
        super().__init__()

    def get_category_id(self):
        for category in self.categories:
            if category[1] == self.current_category:
                return category[0]

    def onStart(self):
        self.addForm(MAIN, MainForm, name='OpenFoodFacts')
        self.addForm(SEARCH, SearchForm, name='OpenFoodFacts - Search')

    def late_add_form(self, form_id):
        try:
            self.removeForm(form_id)
        except:
            pass

        if form_id == SEARCH_RESULT:
            self.addForm(SEARCH_RESULT, SearchResultForm,
                name='OpenFoodFacts - Search Results')
        if form_id == PRODUCTS:
            self.addForm(PRODUCTS, ProductsForm, name='OpenFoodFacts - Search')

        self.switchForm(form_id)
