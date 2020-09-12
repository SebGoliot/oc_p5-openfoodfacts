import npyscreen
from npyscreen.wgtextbox import FixedText  
from settings import CATEGORIES
from view.buttons import BackButton, ExitButton, CategoryButton

class SearchForm(npyscreen.FormBaseNew):
    def create(self):
        self.buttons = {}
        
        self.add(
            FixedText,
            value='Choississez une catégorie',
            editable=False
        )

        self.nextrely += 2
        
        for category in CATEGORIES:
            self.buttons[category] = self.add(
                CategoryButton,
                name=category
            )

        self.back_button = self.add(BackButton, name='Back', relx=-24, rely=-3)
        self.exit_button = self.add(ExitButton, name='Exit', relx=-12, rely=-3)
