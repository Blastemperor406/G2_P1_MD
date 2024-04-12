from data_collectors.Producthunt_API import ProductHunt
import asyncio
import os
if __name__=="__main__":
    api=ProductHunt(os.getenv("PRODUCTHUNT_API"))
    api.get_data()