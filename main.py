import time
from data_collectors.Producthunt_API import ProductHunt
from data_collectors.AppSumo_Scraper import AppSumo
from data_collectors.SaasWorthy_Scraper import SaasWorthy

import multiprocessing



def ph():
    ph=ProductHunt("https://api.producthunt.com/v2/api/graphql","cC_itI8AinMwOQE5zhcpbKWZq2syCxszY7RnndcR_yk")
    data=ph.get_data()
    for i in data:
        ph.storage.insert_products(i)

def aps():
    aps=AppSumo()
    data=aps.get_data()
    for i in data:
        print(i)
        aps.storage.insert_products(i)

def sw():
    sw=SaasWorthy()
    data=sw.get_data()
    for i in data:
        sw.storage.insert_products(data)


if __name__ == "__main__":
    time.sleep(5)
    # Create processes for each function
    process1 = multiprocessing.Process(target=aps)
    process2 = multiprocessing.Process(target=sw)
    process3 = multiprocessing.Process(target=ph)

    # Start the processes
    process1.start()
    process2.start()
    

    # Wait for both processes to finish
    process1.join()
    process2.join()
    


    
