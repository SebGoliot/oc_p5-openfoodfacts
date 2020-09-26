import npyscreen
from npyscreen.wgtextbox import FixedText
from view.buttons import BackButton, FindSubstituteButton, SaveProductButton

class ProductsNotifyForm(npyscreen.FormBaseNew):

    DEFAULT_COLUMNS = 60
    DEFAULT_LINES = 15
    SHOW_ATX = 10
    SHOW_ATY = 2

    def __init__(self, *args, **kwargs):
        self.product = kwargs.get('product')
        if not self.product:
            raise RuntimeError("Missing kwarg: 'product'")

        super().__init__(*args, **kwargs)

    def create(self):

        if self.product.stores == '':
            stores = "Aucun magasin n'a été trouvé"
        else:
            stores = ', '.join([x for x in self.product.stores.split(',')])

        self.add(
            FixedText,
            value= f"Score : {self.product.score.upper()}",
            editable=False,
            color= self.get_score_color()
        )
        self.add(
            FixedText,
            value= "Disponible à :",
            editable=False
        )
        self.add(
            FixedText,
            value= stores,
            editable=False
        )

        if self.parentApp.subst_search:
            self.add(
                SaveProductButton,
                name = 'Ajouter aux favoris',
                rely = -4,
                favorite_id = self.product.product_id,
                substitued_id = self.parentApp.subst_search['from'].product_id)
        else:
            self.add(
                FindSubstituteButton,
                name = 'Rechercher un substitut',
                rely = -4,
                from_product = self.product)

        
        self.add(BackButton, name='Retour', relx=46)


    def get_score_color(self):
        colors = {
            'A': 'GOOD',
            'B': 'STANDOUT',
            'C': 'CONTROL',
            'D': 'DANGER',
            'E': 'CRITICAL',
        }
        return colors.get(self.product.score.upper())
