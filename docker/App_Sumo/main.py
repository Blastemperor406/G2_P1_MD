from data_collectors.AppSumo_Scraper import AppSumo
import asyncio

if __name__=="__main__":
    print("Starting Scraper")
    api=AppSumo(hosts=["kafka-1:19092","kafka-2:19093","kafka-3:19094"])
    asyncio.run(api.start())

    