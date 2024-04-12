from data_collectors.SaasWorthy_Scraper import SaasWorthy
import asyncio


if __name__=="__main__":
    api=SaasWorthy()
    asyncio.run(api.start())