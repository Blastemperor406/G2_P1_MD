from data_collectors.SaasWorthy_Scraper import SaasWorthy
import asyncio


if __name__=="__main__":
    api=SaasWorthy(hosts=["kafka-1:19092","kafka-2:19093","kafka-3:19094"])
    asyncio.run(api.start())