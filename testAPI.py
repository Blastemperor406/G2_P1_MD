import requests
headers = {
    'Authorization': 'Token token=7623beff9ca1e3e0479ca27f225244c70fa017fed820b1bb733afa588a1549fb'}
filters = {
    'filter[name]': 'Simple Custom Reports for Jira'}
response = requests.get('https://data.g2.com/api/v1/products',headers=headers,params=filters)

print(response.json())