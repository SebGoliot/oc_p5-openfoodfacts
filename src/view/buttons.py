import npyscreen
from controller.db_manager import DbManager

class ExitButton(npyscreen.ButtonPress):
    def whenPressed(self):
        print(self.parent.parentApp.current_category)
        self.parent.parentApp.switchForm(None)

class BackButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchFormPrevious()

class SearchButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('SearchForm')
        
class FavoritesButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.parentApp.switchForm('CategoryForm')

class ResetDBButton(npyscreen.ButtonPress):
    def whenPressed(self):  
        notification_message = ("Veuillez patienter...\n"
        "Cette opération peut durer un certain temps...")
        npyscreen.notify(notification_message, title='Réinitialisation...')
        DbManager().create_db(drop=True, populate=True)
