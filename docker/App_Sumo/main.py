from data_collectors.AppSumo_Scraper import AppSumo
import asyncio
if __name__=="__main__":
    api=AppSumo()
    asyncio.run(api.start())