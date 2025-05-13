import json
import os

with open ("budzetiranje/podaci.json", "r") as file:
    data = json.load(file)
    data.append({"new": "YES"})
print(data)


with open ("budzetiranje/podaci.json", "w") as file:
    json.dump(data, file, indent = 4)



def load_file(file_name):
    with open("budzetiranje/podaci.json", "r") as file:
        data = json.load(file)
        data.append({"new": "YES"})
    print(data)


def delete_file(file_name):
    os.remove(file_name)


def empty_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent = 4)




