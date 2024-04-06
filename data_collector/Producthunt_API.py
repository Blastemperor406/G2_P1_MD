import requests
from .API_Collector import APICollector


class ProductHunt(APICollector):
    
    def __init__(self, url: str, api_key: str) -> None:
        super().__init__(url, api_key)

    def fetch_data(self,query):
        
        headers = {
            'Authorization': f'Bearer {self.key}',
            'Content-Type': 'application/json',
        }
        response = requests.post(self.url, headers=headers, json={'query': query})
        return response.json()

    def get_data(self):
        query = '''
        query {
          posts(order: NEWEST, first: 10) {
            edges {
              node {

                id
                name
                description
                website
               
              }
            }
          }
        }
        '''
        data = self.fetch_data(query)
        products = data.get('data', {}).get('posts', {}).get('edges', [])
        
        product_list = []
        for edge in products:
            product = edge.get('node', {})
            product_list.append({
                'ID': product.get('id'),
                'Name': product.get('name'),
                'Tagline': product.get('tagline'),
                'Description': product.get("description"),
                'Slug': product.get("slug"),
                'Website': product.get("website"),
                'URL': product.get("url"),
                
            })
        
        return product_list
    

if __name__=="__main__":
    api=ProductHunt("https://api.producthunt.com/v2/api/graphql","<ProductHunt API Key>")
    data=api.get_data()
    api.database.insert_products(data)
    for i in data:
        print(i)
        print("\n\n\n\n")