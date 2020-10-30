import npyscreen
from openfoodfacts.view.buttons import (
    SearchButton,
    FavoritesButton,
    ResetDBButton,
    ExitButton,
)


class MainForm(npyscreen.FormBaseNew):
    """This form in the main form of the TUI.
    It displays the main menu.
    """

    def create(self):

        self.search_btn = self.add(SearchButton, name="Rechercher un produit")

        self.nextrely += 1
        self.favorites_btn = self.add(
            FavoritesButton, name="Produits enregistrés"
        )

        self.nextrely += 3
        self.reinit_btn = self.add(
            ResetDBButton, name="Réinitilaliser la base de données"
        )

        self.exitButton = self.add(ExitButton, name="Quit", relx=-12, rely=-3)
