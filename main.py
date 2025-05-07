
from methods import load_file, save_file, delete_file, empty_file

#   with open("data/user.json", "w") as file:
   #     json.dump(data, file, indent = 5)


data = load_file("data/products.json")
user = load_file("data/user.json")
print(data)
print(user)

user.append({"name": "Milica"})

user = save_file("data/products.json", data)
# r = read,
# w = write


delete = delete_file("delete_fajl")


empty = empty_file("data/products.json, ")

