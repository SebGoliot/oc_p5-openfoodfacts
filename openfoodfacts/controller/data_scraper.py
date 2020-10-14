from re import search
import requests
import json
from openfoodfacts.settings import API_ENDPOINT


class DataScraper:
    @classmethod
    def get_api_category(cls, category, limit=250):
        """Gets data from the API corresponding to a category """

        search_args = {
            "sort_by": "unique_scans_n",
            "action": "process",
            "search_terms": category,
            "page_size": limit,
            "json": 1,
        }

        data = requests.get(url=API_ENDPOINT, params=search_args)
        clean_data = cls.sanitize_data(data.content)
        return {"category": category, "content": clean_data}

    @staticmethod
    def sanitize_data(data):
        """Sanitizes data from the api """

        json_data = json.loads(data.decode("utf-8"))
        products = []

        for each in json_data["products"]:

            product = {}
            product["code"] = each.get("code", 0)
            product["product_name"] = each.get("product_name", "")
            product["stores"] = each.get("stores", "")
            product["nutriscore"] = each.get("nutriscore_grade", "e")

            if product["product_name"] == "":
                continue

            products.append(product)

        return products
