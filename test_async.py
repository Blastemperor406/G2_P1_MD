from data_collectors.SaasWorthy_Scraper import SaasWorthy
from data_collectors.AppSumo_Scraper import AppSumo
from data_collectors.Posts_Scraper import DataProcessor
from data_collectors.Producthunt_API import ProductHunt
import asyncio

async def main():
    # collector=SaasWorthy()
    # await collector.start()
    # collector=DataProcessor(["0.0.0.0:9093", "0.0.0.0:9092", "0.0.0.0:9094"])
    # collector.main()
    # collector1=AppSumo()
    # await collector1.start()
    api=ProductHunt(api_key="cC_itI8AinMwOQE5zhcpbKWZq2syCxszY7RnndcR_yk")
    data=api.get_data()
asyncio.run(main())