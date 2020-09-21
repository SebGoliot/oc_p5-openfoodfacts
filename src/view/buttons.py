import time
import npyscreen
from npyscreen import npyspmfuncs
from view.forms_const import *

class BackButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchFormPrevious()

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(None)

class SearchButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(SEARCH_FORM)
        
class FavoritesButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.late_add_form(PRODUCTS_FAVORITES)

class ResetDBButton(npyscreen.ButtonPress):
    def whenPressed(self):  
        notification_message = ("Veuillez patienter...\n"
        "Cette opération peut durer un certain temps...")
        npyscreen.notify(notification_message, title='Réinitialisation...')
        self.parent.parentApp.db_mgr.create_db(drop=True, populate=True)

class SearchFieldButton(npyscreen.ButtonPress):
    def whenPressed(self):
        search = self.parent.search_field.value
        self.parent.parentApp.late_add_form(PRODUCTS_SEARCH, search = search)

class CategoryButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.late_add_form(
            PRODUCTS_CATEGORY, category = self.name)

class ProductButton(npyscreen.ButtonPress):

    def __init__(self, *args, **kwargs):
        self.product = kwargs.get('product')
        super().__init__(*args, **kwargs)

    def whenPressed(self):
        r = self.parent.buttons[str(self.product)]
        npyscreen.notify(message=repr(r), title=r.name)
        time.sleep(1)
