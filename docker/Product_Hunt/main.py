from data_collectors.Producthunt_API import ProductHunt
import asyncio
import os
if __name__=="__main__":
    api=ProductHunt(os.getenv("PRODUCTHUNT_API"),hosts=["kafka-1:19092","kafka-2:19093","kafka-3:19094"])
    api.get_data()