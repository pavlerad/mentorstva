import time

products = {}

print("\nLista proizvoda izgleda ovako: \n")

for keys, items in products.items():
    print(keys, items)

available_options = ["obrisi", "dodaj", "lista"
    , "stop", "istorijat", "obrisi sve"
    , "najskuplji proizvod", "pnp"]


history = []


options = None
while options not in available_options:
    options = input(f"\nSta zelite da uradite sa proizvodima? {", ".join(available_options)} ").lower()

    if options == "obrisi":
        product = None

        while product not in products:
            product = input("Koji proizvod zelite da obrisete? ").lower()


        del products[product]
        time.sleep(2)
        msg = f"Proizvod '{product}' je obrisan.\n"
        print(msg)
        history.append(msg)
        print(f"Vasa lista proizvoda sada izgleda ovako: \n")

        for keys, values in products.items():
            print(f"{keys} - {values}")

        options = None


    elif options == "dodaj":
        product = None

        while product in products or product is None:
            product = input("Unesite ime proizvoda koji zelite da dodate: ").lower()

        price = None
        quantity =  None
        while price is None or price <= 0:
                price = int(input("Molimo unesite cenu proizvoda: "))
                msg = f"Vas proizvod '{product}' sada ima cenu {price: .2f} RSD"
                print(msg)
                history.append(msg)
                products[product] = {}
                products[product] = {"cena": price, "kolicina": quantity}

        quantity = None


        msg = f"Uspesno ste dodali proizvod '{product}'."
        print(msg)
        history.append(msg)
        options = None

        def add_product(price, quantity):
            while quantity is None or quantity <= 0:
                quantity = int(input("Molimo unesite kolicinu proizvoda: "))
                msg = f"Sada vas proizvod '{product}' ima cenu {price: .2f} RSD i kolicinu {quantity}."
                print(msg)
                history.append(msg)
                print("-----------------------------------------\n")
                products[product] = {"cena": price, "kolicina": quantity}


        urlam = add_product("150", 100)
        print(urlam)

    elif options == "lista":
        options = None
        msg = "Vasa lista proizvoda izgleda ovako: \n"
        print(msg)
        history.append(msg)
        time.sleep(2)
        for keys, values in products.items():
            time.sleep(2)
            print(f"{keys} - {values}")
            options = None

    elif options == "istorijat":
        print(history)
        options = None

    elif options == "obrisi sve":
        products = {}
        msg = "Vasi proizvodi su obrisani."
        print(msg)
        history.append(msg)
        options = None

    elif options == "najskuplji proizvod" or "pnp":

        highest_price = 0
        max_product_name = ""

        for product in products:

            if highest_price < products[product]["cena"]:
                highest_price = products[product]["cena"]
                max_product_name = product



        msg = f"Najvisa cena je {highest_price: .2f} RSD, a koju ima proizvod '{max_product_name}'."
        print(msg)
        history.append(msg)
        options = None
