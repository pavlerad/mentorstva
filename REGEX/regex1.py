import re


nasiBrojevi = "12345"

sablon_brojevi = r"^\d+$"

if re.match(sablon_brojevi, nasiBrojevi):
    print("Samo brojevi")
else:
    print("Nisu samo brojevi")


recenica = "I love Python"
sablon_slova = r"^[a-z,A-Z]"

if re.match(sablon_slova, recenica):
    print("Samo slova")
else:
    print("Nisu samo slova")



very_important = "Today will not rain."


sablon2 = r"^[A-Z]"

if re.match(sablon2, very_important):
    print("Pocinje velikim slovom.")
else:
    print("Ne pocinje velikim slovom.")

telefon = "382659382"

sablon_telefon = r"^38(1|2|3|5|9)"

phoneMatch = re.match(sablon_telefon, telefon)







phonemap =  {"381" :"Serbia",
            "382" : "Montenegro",
            "383" : "Croatia",
            "385" : "Bosnia&Herzegovina"}




for keys, items in phonemap.items():
    print(keys,"-", items,"\n")


if phoneMatch:
    prefix = "38"+phoneMatch.group(1)
    print(f"Your prefix number is: {prefix} and it belongs to {phonemap[prefix]}.")


name = "Pavle Radovanovic"


patterns = r"^[A-Z][a-z]+ [A-Z][a-z]+$"

if re.match(patterns, name):
    print("YES")
else:
    print("NO")



mail = "toma@gmail.com"

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w"


if re.match(email_pattern, mail):
    print("It is an email.")
else:
    print("It is not an email.")







emails = "pavle11radovanovic@gmail.com"

mejl_sablon = r"^[\w\.-]+[\d]+[\w\.-]+@[\w\.-]+\.\w"



if re.match(mejl_sablon, emails):
    print("yes")
else:
    print("not")