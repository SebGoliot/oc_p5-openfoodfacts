import npyscreen    
from settings import CATEGORIES
from view.buttons import BackButton, ExitButton

class CategoryForm(npyscreen.FormBaseNew):
    def create(self):
        self.buttons = {}
        for category in CATEGORIES:
            self.buttons[category] = self.add(
                npyscreen.ButtonPress,
                name=category
            )

        self.back_button = self.add(BackButton, name='Back', relx=-24, rely=-3)
        self.exit_button = self.add(ExitButton, name='Exit', relx=-12, rely=-3)
