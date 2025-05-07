import json


with open("products.json", "r") as file:
    data = json.load(file)
    print(data)