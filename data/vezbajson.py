import json

with open ("user.json", "r") as file:
    data = json.load(file)
    print(data)
    data.append({"name": "Mirko",
                 "gender": "male",
                 "height": 190,
                 "weight": 88,
                "age": 34})
    print(data)



with open("user.json", "w") as file:
    json.dump(data, file, indent = 4)

