import time
import npyscreen
from npyscreen import npyspmfuncs
from controller.db_manager import DbManager
from view.forms_const import CATEGORY, PRODUCTS, SEARCH, SEARCH_RESULT

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(None)

class BackButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchFormPrevious()

class SearchButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(SEARCH)
        
class FavoritesButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm(CATEGORY)

class ResetDBButton(npyscreen.ButtonPress):
    def whenPressed(self):  
        notification_message = ("Veuillez patienter...\n"
        "Cette opération peut durer un certain temps...")
        npyscreen.notify(notification_message, title='Réinitialisation...')
        self.parent.parentApp.db_mgr.create_db(drop=True, populate=True)

class CategoryButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.current_category = self.name
        self.parent.parentApp.late_add_form(PRODUCTS)

class SearchFieldButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.search = self.parent.search_field.value
        self.parent.parentApp.late_add_form(SEARCH_RESULT)
        
class ProductButton(npyscreen.ButtonPress):
    def whenPressed(self):
        npyscreen.notify(message='aled', title='oskour')
        time.sleep(2)