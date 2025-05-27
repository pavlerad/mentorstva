import re


#username = "Pavle12"

#pattern = r"^[A-Z,a-z]{1,5}+\d{3,}"

#re.match(pattern,username)



bonus_codes = "Pavle123, bonus23, pobeda200"

pattern = r"[A-Za-z]{5,}\d{2}"

challenge = re.findall(pattern, bonus_codes)
print(challenge)


username = "P25, Pa25 ,Pav25, Pavl25, Pavle25"
patrn = r"\b[A-Z,a-z]{1,5}\d{2,}\b"

user = re.findall(patrn,username)
print(user)


