import json

with open ("data.json", "r") as file:
    data = json.load(file)
    print(data)
    data.append({"name": "Mirko",
                 "gender": "male",
                 "height": 190,
                 "weight": 88,
                "age": 34})
    print(data)



with open("data.json", "w") as file:
    json.dump(data, file, indent = 5)

