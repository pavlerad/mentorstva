
shops = {



    "Maxi" :

            {"hleb": 200,
              "voda": 300,
              "jabuka": 100},

    "Univerexport":

            {"hleb": 200,
             "voda:": 150,
             "jabuka": 150},

    "Lidl":

            {"hleb": 250,
             "voda:": 300,
             "jabuka": 100},


    "Aman":

            {"hleb": 230,
             "voda:": 400,
             "jabuka": 90},

    "Shop&Go":

            {"voda": 100,
            "jabuka": 200}


}


import time

total_bread_price = 0
max_bread_price = 0
average_bread_price = 0
total_bread_shops = 0
total_shops = len(shops)
max_bread_price_shop = ""

print("Ukupan broj radnji je: ", total_shops,"\n")
print("Ovo je spisak radnji sa proizvodima: \n")

for keys, values in shops.items():
    time.sleep(2)
    print(f"{keys} - {values}")


    if "hleb" in values:
        total_bread_price += values["hleb"]
        total_bread_shops += 1


        if  max_bread_price < values["hleb"]:
            max_bread_price = values["hleb"]
            max_bread_price_shop = keys



print("---------------------------------------------------")
time.sleep(2)
print(f"Ukupan broj radnji koje imaju hleb je: {total_bread_shops}")
print(f"Ukupna cena hleba je: {total_bread_price: .2f} RSD")
average_bread_price = total_bread_price / total_bread_shops
print(f"Prosecna cena hleba je: {average_bread_price: .2f}RSD")
print(f"Maksimalna cena hleba je: {max_bread_price: .2f} RSD, u radnji: {max_bread_price_shop}.")
input("\nPritisni taster 'Enter' za izlazak iz programa.")


