import requests
import json
from model.constants import API_ENDPOINT, API_SEARCH

class DataScraper():
    
    @staticmethod
    def get_api_category(category, limit=250):
        """Gets data from the API corresponding to a category """

        search_args = f"{category}&page_size={limit}&json=1"
        data = requests.get(url=f'{API_ENDPOINT}{API_SEARCH}{search_args}')
        clean_data = DataScraper.sanitize_data(data.content)
        return {'category': category, 'content': clean_data}


    @staticmethod
    def sanitize_data(data):
        """Sanitizes data from the api """

        json_data = json.loads(data.decode('utf-8'))
        products = []
        
        for each in json_data['products']:

            product = {}
            product['code'] = each.get('code', 0)
            product['product_name'] = each.get('product_name', '')
            product['stores'] = each.get('stores', '')
            product['nutriscore'] = each.get('nutriscore_grade', 'e')

            products.append(product)

        return products
