import json


with open("products.json", "r") as file:
    data = json.load(file)
    print(data)

with open ("products.json", "r" ) as file:
    data = json.load(file)
    data.append({"grenade": 20,
                 "kiwi": 20})
    print(data)

with open ("products.json", "w") as file:
    json.dump(data, file, indent = 2)
