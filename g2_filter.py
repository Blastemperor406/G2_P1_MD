import requests
from llama_index.readers.string_iterable import StringIterableReader
from dotenv import load_dotenv
import pandas
from llama_index.core import TreeIndex
load_dotenv()
import os
import json


def g2_call(name):
    headers = {'Authorization': 'Token token='+os.environ.get("g2_token")}
    filters = {'filter[name]': name} 
    response = requests.get('https://data.g2.com/api/v1/products',headers=headers,params=filters)
    if response.status_code == 200:
        # Extract the JSON data from the response
        out = response.json()
        # Process the products data as needed
        product_names = [item['attributes']['name'] for item in out['data']]
        if name in product_names:
            print('Product found')
            return True
        else:
            print('Product not found')
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
    a=query_engine.query("Is this a 'Business to Business' or a 'B2B' product? Words like 'business','Sellers' and 'CRM' are indicative of B2B product .Answer as 'True' or 'False'")
    #b=query_engine.query("What is the product's name?")
    if a.response=='True':
        return True
    else:
        return False

def g2_filter(d,function_call):
    print(function_call)
    name=d["Name"]
    if g2_call(name)==False:
        if b2b_filter(d["Description"])==True:
            function_call(d)
        else:
            return 
    else:
        return