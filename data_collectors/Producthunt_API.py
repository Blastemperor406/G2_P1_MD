import requests

# from .data_storage.database import Database
from data_storage.kafka import Kafka
class ProductHunt():
    
    def __init__(self, url: str, api_key: str) -> None:
        self.url=url
        self.key=api_key
        # self.storage=Database()
        self.storage=Kafka(["0.0.0.0:9093","0.0.0.0:9092","0.0.0.0:9094"])
    def fetch_data(self,query):
        
        headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json",
        }
        response = requests.post(self.url, headers=headers, json={"query": query})
        return response.json()

    def get_data(self):
        query = """
        query {
          posts(order: NEWEST, first: 40) {
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
        """
        data = self.fetch_data(query)
        products = data.get("data", {}).get("posts", {}).get("edges", [])
        
        product_list = []
        for edge in products:
            product = edge.get("node", {})
            product_list.append({
                "Name": product.get("name").strip(),
                "Description": product.get("description").strip(),
                "Website": product.get("website").strip(),
            })
        
        return product_list
    

if __name__=="__main__":
    api=ProductHunt("https://api.producthunt.com/v2/api/graphql","cC_itI8AinMwOQE5zhcpbKWZq2syCxszY7RnndcR_yk")
    data=api.get_data()
    # api.storage.insert_products(data)
    for i in data:
        api.storage.insert_products({"Description":i["Description"],"Website":i["Website"],"Name":i["Name"]})