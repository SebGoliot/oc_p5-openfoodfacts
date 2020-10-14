import npyscreen
from npyscreen.wgtextbox import FixedText, Textfield
from openfoodfacts.settings import CATEGORIES
from openfoodfacts.view.buttons import (
    BackButton,
    ExitButton,
    CategoryButton,
    SearchFieldButton,
)
from openfoodfacts.view.forms_const import PRODUCTS_SEARCH


class SearchForm(npyscreen.FormBaseNew):
    def create(self):

        self.add(FixedText, value="Recherchez un produit:", editable=False)
        self.search_field = self.add(
            Textfield, name="Search Field", value="", relx=25, rely=2
        )
        self.add(
            SearchFieldButton,
            name="Rechercher..",
            relx=30,
            btn_dest=PRODUCTS_SEARCH,
        )

        self.nextrely += 1
        self.add(FixedText, value="--- ou ---", editable=False)

        self.add(FixedText, value="Parcourez une catégorie", editable=False)

        self.nextrely += 2

        for category in CATEGORIES:
            self.add(CategoryButton, name=category)

        self.add(BackButton, name="Retour", relx=-24, rely=-3)
        self.add(ExitButton, name="Quit", relx=-12, rely=-3)
