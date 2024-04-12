import requests
# from data_storage.database import Database
from data_storage.kafka import Kafka
import aiohttp
import asyncio
class AppSumo:
    def __init__(self) -> None:
        
        self.categories=["marketing-sales",
                         "operations",
                         "build-it-yourself",
                         "media-tools",
                         "finance",
                         "development-it",
                         "customer-experience"   
                        ]

        self.url = "https://appsumo.com/api/v2/deals/esbrowse/?__cache=a&include_aggs=true&status=current&sort=recommended&per_page=10000&attribute[group]=software&attribute[category]={}"


        self.headers = {
                        "authority": "appsumo.com",
                        "accept": "*/*",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "sec-gpc": "1",
                        "x-csrftoken": "TjDszSceH2FhnxT1dmJIuANZE3GqFlpqFi00hwSLHqRQeS0eYv3Gy6WgPPMj0hoU",
                    }

        self.storage=Kafka(["0.0.0.0:9093","0.0.0.0:9092","0.0.0.0:9094"])

    async def start(self):
        await self.get_data()


    async def insert_data(self,data):
         self.storage.insert_products(data)


    async def get_data(self) -> list:
        results = []
        async with aiohttp.ClientSession() as session:
            for category in self.categories:
                async with session.get(self.url.format(category), headers=self.headers) as response:
                    data = await response.json()
                    for deal in data.get("deals", []):
                        if not deal["has_ended"]:
                            await self.insert_data({
                                "Name": deal["public_name"].strip(),
                                "Description": deal["card_description"].strip(),
                                "Website": ""
                            })
    




if __name__=="__main__":
    collector=AppSumo()
    asyncio.run(collector.start())
