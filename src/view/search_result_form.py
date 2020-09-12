import npyscreen
from npyscreen import ButtonPress
from view.buttons import BackButton, ExitButton

class SearchResultForm(npyscreen.FormMultiPage):
        
    def create(self):
        products = self.parentApp.db_mgr.find_product(self.parentApp.search)


        for i, product in enumerate(products):
            if not i % 24 and i:
                self.add_page()
            self.add(ButtonPress, name=product[0])

        self.add(BackButton, name='Back', relx=-24, rely=-3)
        self.add(ExitButton, name='Exit', relx=-12, rely=-3)
