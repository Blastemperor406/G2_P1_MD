import requests
from bs4 import BeautifulSoup
import time
import aiohttp

# from data_storage.database import Database
from data_storage.kafka import Kafka
class SaasWorthy:
    def __init__(self,hosts:list=["0.0.0.0:9093","0.0.0.0:9092","0.0.0.0:9094"]):
        self.categories=[]
        
        self.url = "https://www.saasworthy.com/api/v1/guest/category/product/list"
        self.headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Cookie": "abgroup=A; PHPSESSID=skDtKlDpQqwz7soLrJT95bdS2BRjo9o4y4l8CefT; XSRF-TOKEN=bTmBlqhzVsjhMRoiE33shHUtBbBUNjbIHLyMG33p; GCLB=CKDNmMG7qbD4JxAD; swUid=7a5385b6f7d1bd3505237eaf58229404"
            }
        self.params={
            "start": "0",
            "max": "2000",
            "sortBy": "created",
            "qp": "",
            "page": "0",
            "slug": ""
        }
        
        # self.storage=Database()
        self.storage=Kafka(hosts)

    async def start(self):
         await self.get_categories()

    async def get_categories(self)->None:
            url="https://www.saasworthy.com/list"
            
            r=requests.get(url)
            soup=BeautifulSoup(r.content,"html.parser")

            # Get all categories
            categories=soup.find_all("div",class_="catgry_div")
            
            categories_list=[]

            
            for i in categories:
                    sub_categories=i.find("ul").find_all("li")
                    # Get all subcategories
                    for j in sub_categories:
                        await self.get_data(j.find("a")["href"])


                
    
    async def insert_data(self,result):
        self.storage.insert_products(result)


    async def get_data(self,category)->list:
        
        self.params["slug"]=category
        async with aiohttp.ClientSession() as session:
            
            async with session.get(self.url,params=self.params,headers=self.headers) as resp:
                print(resp.status)
                if resp.status==503:
                    return
                data=await resp.json()                   
                
                for j in data.get("products", []):
                    try:
                        await self.insert_data({"Website":j["vendorURL"].strip(),"Description":j["productDescription"].strip(),"Name":j["productName"].strip()})
                    except Exception as e:
                         print(e)
                         
            
if __name__=="__main__":
    collector = SaasWorthy()
    # data=collector.get_data()
    # collector.storage.insert_products(data)
    collector.start()




