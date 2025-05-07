import json


with open ("data/user.json", "r") as file:
    data = json.load(file)
    data.append({     "name" : "Milos",
                      "age" : 24,
                      "height": 160,
                      "gender": "male"})
    print(data)


    with open("data/user.json", "w") as file:
        json.dump(data, file, indent = 5)

print(data)


# r = read,
# w = write

