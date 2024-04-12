from data_collectors.SaasWorthy_Scraper import SaasWorthy
from data_collectors.AppSumo_Scraper import AppSumo
import asyncio

async def main():
    collector=SaasWorthy()
    await collector.start()

    # collector1=AppSumo()
    # await collector1.start()

asyncio.run(main())