import requests
import random

api_key = "fq1HNI8Sq9YgAVksiagtpslP08g1HNba"  

search_query = input("Введіть слово для пошуку: ")

url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_query}&limit=1"

response = requests.get(url)

data = response.json()

for gif in data["data"]:
    print(gif["url"])
