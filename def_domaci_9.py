from tkinter.font import names


def calculate_delivery(grad):
  if grad == "Beograd":
    return 600
  elif grad == "Novi Sad":
    return 800
  elif grad == "Subotica":
    return 700
  elif grad == "Zrenjanin":
    return 450
  elif grad == "Nis":
    return 700
  elif grad == "Sombor":
    return 550

calculate_delivery("Beograd")

print("\n----------------BEOGRAD-------------\n")

product_price_bg = 1200
print(f"Cena proizvoda u Beogradu je: {product_price_bg: .2f} RSD.")
product_delivery_bg = calculate_delivery("Beograd")
print(f"Cena dostave u Beogradu je: {calculate_delivery("Beograd"): .2f} RSD.")
total_price = product_price_bg + calculate_delivery("Beograd")
print(f"Ukupna cena porudzbine je: {total_price: .2f} RSD.")


print("\n----------------NOVI SAD-------------\n")

product_price_ns = 1000
print(f"Cena proizvoda u Novom Sadu je: {product_price_ns: .2f} RSD.")
product_delivery_ns = calculate_delivery("Novi Sad")
print(f"Cena dostave u Novom Sadu je: {calculate_delivery("Novi Sad"): .2f} RSD.")
total_price = product_price_ns + calculate_delivery("Novi Sad")
print(f"Ukupna cena porudzbine je: {total_price: .2f} RSD.")




print("\n----------------SUBOTICA-------------\n")

product_price_sb = 800
print(f"Cena proizvoda u Novom Sadu je: {product_price_sb: .2f} RSD.")
product_delivery_sb = calculate_delivery("Subotica")
print(f"Cena dostave u Sbotici je: {calculate_delivery("Subotica"): .2f} RSD.")
total_price = product_price_sb + calculate_delivery("Subotica")
print(f"Ukupna cena porudzbine je: {total_price: .2f} RSD.")




print("\n----------------ZRENJANIN-------------\n")

product_price_zr = 900
print(f"Cena proizvoda u Zrenjaninu je: {product_price_zr: .2f} RSD.")
product_delivery_zr = calculate_delivery("Zrenjanin")
print(f"Cena dostave u Zrenjaninu je: {calculate_delivery("Zrenjanin"): .2f} RSD.")
total_price = product_price_zr + calculate_delivery("Zrenjanin")
print(f"Ukupna cena porudzbine je: {total_price: .2f} RSD.")





books = []



def add_books(name, author):
  books.append({"book_name":name, "book_author": author})


add = add_books("Cica Gorio", "Onore de Balzak")
print(books)

add = add_books("Zlocin i kazna", "Dostojevski")

print(books)


def find_book(name):
  for book in books:
    if book['book_name'] == name:
      return book

search = find_book("Zlocin i kazna")
print(search)


def delete_book(name):
  search_book = find_book(name)
  if search_book is None:
    print("There is no such book")
 # else:
   # books.remove(name)

#delete = delete_book("Cica Gorio")
print(books)



def city_pricing(city):
  if city == "Beograd":
    return 500
result = city_pricing("Beograd")
print("Cena dostave je",result)


















