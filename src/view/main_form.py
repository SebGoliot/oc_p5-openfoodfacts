import npyscreen
from view.buttons import *


class MainForm(npyscreen.FormBaseNew):
    def create(self):

        self.search_btn=self.add(
            SearchButton,
            name='Rechercher un produit'
        )
        self.nextrely += 1
        self.favorites_btn=self.add(
            FavoritesButton,
            name='Produits enregistrés'
        )
        self.nextrely += 3
        self.favorites_btn=self.add(
            ResetDBButton,
            name='Réinitilaliser la base de données',
        )

        self.exitButton = self.add(ExitButton, name="Exit", relx=-12, rely=-3)
