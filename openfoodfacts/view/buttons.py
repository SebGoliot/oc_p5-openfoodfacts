import npyscreen
from openfoodfacts.view.forms_const import *


class BackButton(npyscreen.ButtonPress):
    """Button used to go back in the application """

    def whenPressed(self):
        self.parent.parentApp.switchFormPrevious()


class ExitButton(npyscreen.ButtonPress):
    """Button used to exit the application. """

    def whenPressed(self):
        self.parent.parentApp.switchForm(None)


class SearchButton(npyscreen.ButtonPress):
    """Button used to switch to the Search form. """

    def whenPressed(self):
        self.parent.parentApp.switchForm(SEARCH_FORM)


class FavoritesButton(npyscreen.ButtonPress):
    """Button used to switch to the Favorites form. """

    def whenPressed(self):
        self.parent.parentApp.late_add_form(PRODUCTS_FAVORITES)


class ResetDBButton(npyscreen.ButtonPress):
    """Button used to reset the database, it also displays a notification. """

    def whenPressed(self):
        notification_message = (
            "Veuillez patienter...\n"
            "Cette opération peut durer un certain temps..."
        )
        npyscreen.notify(notification_message, title="Réinitialisation...")
        self.parent.parentApp.db_mgr.create_db(drop=True, populate=True)


class SearchFieldButton(npyscreen.ButtonPress):
    """Button used to perform a search. """

    def whenPressed(self):
        search = self.parent.search_field.value
        self.parent.parentApp.late_add_form(PRODUCTS_SEARCH, search=search)


class CategoryButton(npyscreen.ButtonPress):
    """Button used to switch to a category form. """

    def whenPressed(self):
        self.parent.parentApp.late_add_form(
            PRODUCTS_CATEGORY, category=self.name
        )


class SaveProductButton(npyscreen.ButtonPress):
    """Button used to save a product to the favorites. """

    def __init__(self, *args, **kwargs):
        self.favorite_id = kwargs.get("favorite_id")
        self.substitued_id = kwargs.get("substitued_id")
        super().__init__(*args, **kwargs)

    def whenPressed(self):
        self.parent.parentApp.db_mgr.add_favorite(
            self.favorite_id, self.substitued_id
        )
        self.parent.parentApp.subst_search_from = None
        self.parent.parentApp.switchForm(MAIN)


class FindSubstituteButton(npyscreen.ButtonPress):
    """Button used to perform a substitutes search. """

    def __init__(self, *args, **kwargs):
        self.from_product = kwargs.get("from_product")
        super().__init__(*args, **kwargs)

    def whenPressed(self):
        self.parent.parentApp.subst_search_from = self.from_product
        self.parent.parentApp.switchFormPrevious()
        self.parent.parentApp.late_add_form(
            PRODUCTS_CATEGORY, category=self.from_product.category
        )


class ProductButton(npyscreen.ButtonPress):
    """Button used to display the products, in the TUI and
    in a notification when pressed.
    """

    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.get("product_id")
        super().__init__(*args, **kwargs)

    def whenPressed(self):
        product = self.parent.buttons[str(self.product_id)]

        self.parent.parentApp.product_notify(product)
