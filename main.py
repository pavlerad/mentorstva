import json


from methods import load_file


products = load_file("data/products.json")
print(products)



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


from methods import load_file