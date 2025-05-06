from methods import load_file, save_file, delete_file, empty_file

user = load_file("data/user.json")
print(user)

user.append({"name": "test"})


user = save_file("data/user.json", user)
print(user)


empty_file("data/user.json")