import requests

search_term = input("Введіть слово, яке ви хочете знайти на Giphy: ")

api_key = "YOUR API KEY"
url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=5"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()["data"]
    for gif in data:
        print(gif["url"])
else:
    print(f"Сталася помилка {response.status_code} при отриманні GIF-зображень.")
