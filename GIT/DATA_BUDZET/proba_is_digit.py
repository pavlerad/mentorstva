


secret_name = ""

while not secret_name.isalpha():
    secret_name = input("Who is dis? ")
    while len(secret_name) < 5:
        secret_name = input("Please input your full name: ")
    else:
        print(f"Hello, {secret_name}!")
       # break

