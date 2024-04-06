from data_collector.Producthunt_API import ProductHunt


api=ProductHunt("https://api.producthunt.com/v2/api/graphql","cC_itI8AinMwOQE5zhcpbKWZq2syCxszY7RnndcR_yk")
data=api.get_data()
api.database.insert_products(data)
