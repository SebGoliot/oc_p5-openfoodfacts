import npyscreen
from view.main_form import MainForm
from view.categories_form import CategoryForm

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', MainForm, name='OpenFoodFacts')
        self.addForm('SearchForm', CategoryForm, name='OpenFoodFacts')
        self.addForm('CategoryForm', CategoryForm, name='OpenFoodFacts')