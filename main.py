import json


with open ("data/user.json", "r") as file:
    data = json.load(file)
    print(data)
    data.append({"name": "Dijana",
                    "age": 23,
                  "gender": "female",
                  "height": 187})
    print(data)

with open ("data/user.json", "w") as file:
    json.dump(data, file, indent = 5)
    print(data)