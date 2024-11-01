import json

offer_link = []
image_link = []
price = []
title = []

with open("api_response.json") as meu_json:
    dados = json.load(meu_json)

for dado in dados.values():
    if "link" in dado:
        if dado["link"] == None:
            break
        offer_link.append(dado["link"])

print(f"offer_link: {offer_link}")

for dado in dados.values():
    if "imageUrl" in dado:
        image_link.append(dado["imageUrl"])

print(f"image_link: {image_link}")

for dado in dados.values():
    if "Price" in dado:
        price.append(dado["Price"])

print(f"price: {price}")

for dado in dados.values():
    if "nameComplete" in dado:
        title.append(dado["nameComplete"])

print(f"title: {title}")

