import requests
from llama_index.readers.string_iterable import StringIterableReader
from dotenv import load_dotenv
import pandas
from llama_index.core import TreeIndex
load_dotenv()

def g2_call(name):
    headers = {'Authorization': 'Token token=7623beff9ca1e3e0479ca27f225244c70fa017fed820b1bb733afa588a1549fb'}
    filters = {'filter[name]': name} 
    response = requests.get('https://data.g2.com/api/v1/products',headers=headers,params=filters)
    if response.status_code == 200:
        # Extract the JSON data from the response
        out = response.json()
        # Process the products data as needed
        product_names = [item['attributes']['name'] for item in out['data']]
        if name in product_names:
            return True
        else:
            return False
    else:
        print('Error:', response.status_code)
        return False

def b2b_filter(pd):
    documents = StringIterableReader().load_data(
    texts=pd
    )
    index = TreeIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    a=query_engine.query("Is this a 'Business to Business' or a 'B2B' product? answer as 'True' or 'False'")
    if a.response==['True']:
        return True
    else:
        return False