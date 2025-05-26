import re


ourNumbers = "12345"


# r - sve sto se pretrazuje gleda se kao string
# ^ - mora da se trazi od pocetka stringa
# \d - trazi brojeve od 0 - 9, matching
# + - nastavlja da trazi
# $ - predstavlja kraj stringa


# da li su samo brojevi unutar necega?

pattern = r"^\d+$"

if re.match(pattern, ourNumbers):
    print("samo brojevi")
else:
    print("nisu samo brojevi")



# regex koji proverava samo slova:


sentence = "I love Python"
letter_pattern = r"^[a-z, A-Z]+$"

#charachter class: [a-z]

if re.match(letter_pattern, sentence):
    print("Samo slova")
else:
    print("Nisu samo slova")

importantSentence = "Today will rain"

capitalPattern = r"^[A-Z]"

if re.match(capitalPattern, importantSentence):
    print("Pocinje velikim")
else:
    print("Ne pocinje velikim")



phone_number = "38165703"
phone_Pattern = r"^38(1|2|5|9)"

phone_match = re.match(phone_Pattern, phone_number)
print(phone_match)



phone_Map = {"381" : "Serbia",
"382" : "Bosnia&Herzegovina",
"383" : "Montenegro",
"385" : "Croatia"}


if phone_match:
    prefix = "38"+phone_match.group(1)
    country = phone_Map[prefix]
    print(f"Prefix number is {prefix} and prefix country is {country}.")






