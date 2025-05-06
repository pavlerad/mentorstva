##lenght = float(input("Enter the lenght: "))
##width = float(input("Enter the width:  "))
##area = lenght * width
import time

#print(f"\n\n\nThe total area is: {area}m²")

# item = input("What are you buying? ")
# price = float(input("What is the price? "))
# quantity = int(input("How many pieces are you buying? "))

#total = price * quantity

#print(f"You have bought {quantity} x {item}/s")
#print(f"Your total is {total}$")

##noun = input("Enter a noun: ")
##adjective = input("Enter an adjective: ")
##verb = input("Enter a verb: ")
##noun1 = input("Enter a noun1: ")
##adjective1 = input("Enter an adjective1: ")

#print("\n\n\nleggo!")

#print(f"Today I saw {noun}")
#print(f"It was not too {adjective}")
#print(f"Later, I {verb} to the cinema, where I saw this {noun1}")
#print(f"Everyone was so {adjective1}")
#input("\n\n\nPress the enter key to exit:")

#people = 20
#remainder = people % 6
#print(remainder)


# import math


#x = 3.50
#y = 4
#z = 5

#result = min(x, y, z)
#print(result)

#print(math.pi)
#print(math.e)

#x = 11.3

#result = math.ceil(x)
#result = math.floor(x)
#print(result)

## circumference of a circle

## import math

# radius = float(input("Enter the radius of a circle: "))
#circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}")

## area of a circle

#import math

# A = math.pi * radius

#radius = float(input("Please input the radius of a circle: "))
#area = math.pi * pow(radius, 2)
#print(f"The area of a circle is: {round(area, 9)} cm²")

# import math

# A = pi * r²
# A = area

# radius = float(input("Please enter the radius of a circle value: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round,(area, 2)} cm²")
# print(area)

#import math
# a = 3.6567

## circle circumference

## a = math.pi * pow(r, 2), where r is radius, a is area

# import math

#Triangle calculator

# formula is c = sqrt(pow(a, 2)) + (pow(b,2)))

#import math

#a = float(input("Please enter a value for a triangle side 1: "))
#b = float(input("Please enter a value for a triangle side 2: "))

#c = math.sqrt(pow(a, 2)) + (pow(b,2))
#print(f"Side C = {c}")


# Circumference of a circle

## formula is: C = 2pi * r, where C = circumference, r = radius

#import math

#radius = float(input("Enter the  radius: "))
#circumference = 2* math.pi * radius
#print(f"The circumference is: {round(circumference, 2)} cm²")

#if circumference >= 100:
    #print("Circumference is too big")
#elif circumference == 100:
   # print("Circumference is good")
#else:
  #  print("Circumference is small")

# area of circle

# formula A = pi * 2r^2

##import math

# radius = float(input("Enter the radius: "))
# area = math.pi * pow(radius, 2)
# area = print(f"The area is {round(area, 2)} cm²")

## The hypotenuse calculator

## the formula is: c = sqrt of a^2 + b^2

#import math

#a = float(input("Enter the side a: "))
#b = float(input("Enter the side b:  "))

#c = math.sqrt(pow(a, 2) + pow(b, 2))

#print(f"The hypotenuse is: {round(c, 2)} cm²")


#is_online = True

#if is_online:
    #print("Hello! Send me message!")
#else:
   # print("You are offline!")


#is_online = True
#while is_online != False:
   # print("Hello! You are online!")

#import random

#the_number = random.randint(1, 100)
#guess = int(input("Take a guess: "))
#tries = 1

#while guess != the_number:
  #  if guess > the_number:
     #   print("Lower...")
  #  else:
       # print("Higher...")

 #   guess = int(input("Take a guess:  "))
  #  tries += 1
#print("You guessed it! The number was", the_number)





# calculator program

#operator = input("Please enter the operator (+, -, *, /): ")
#num1 = float(input("Please enter the number one: "))
#num2 = float(input("Please enter the number two: "))

#if operator == "+":
    #result = num1 + num2
     #print(f"Your result is: {(round(result, 2))}")
#elif operator == "-":
   #  result = num1 - num2
   #  print(f"Your result is: {(round(result, 2))}")
#elif operator == "*":
     #result = num1 * num2
     #print(f"Your result is: {(round(result, 2))}")
#elif operator == "/":
     #result = (num1 / num2)
     #print(f"Your result is: {(round(result, 2))}")
#else:
     #input(f"The operator {operator} is invalid")

#input("\n\n\nPlease press enter to finish the code: ")


#import random

#the_number = random.randint(1, 100)
#guess = int(input("Please take a guess: "))
#tries = 1

#while guess != the_number:
    #if guess > the_number:
   #     print("Lower...")
   # else:
       # print("Higher..")

  #  guess = int(input("Please take a guess: "))
   # tries += 1

# weight converter program

#weight = float(input("Please enter your weight: "))
#unit = input("Please enter the unit of measure (Kg or Lbs): ")

#if unit == "Kg":
   # weight = round(weight /2.250, 1)
    #print(f"Your weight is {weight} Lbs")
#elif unit == "Lbs":
   # weight = round(weight * 2.250, 1)
   # print(f"Your weight is {weight} Kg")
#else:
    #print("The entered unit was invalid. Please try again!")


#input("\n\nPlease press enter key to exit: ")



# temperature converter program


#unit = input("Please enter the unit of measure (Celsius or Fahrenheit): ")
#temperature = float(input("Please enter the temperature: "))

#if unit == "Celsius":
  #  temperature = round((9 * temperature) / 5 + 32, 1);
   # print(f"Your temperature is: {temperature} Fahrenheit")

#elif unit == "Fahrenheit":
   # temperature = round((temperature - 32) * 5 /9, 1)
   # print(f"Your temperature is: {temperature}  Celsius")
#else:
   # print("Your unit input is invalid. Please try again: ")
   # input("\t\t\t\tPlease press enter button to exit: ")


# Logical operators


#temperature = 35
#is_raining = False


#if temperature < 5 and not is_raining:
  #  print("The event will be held")
#elif temperature < 50 and not is_raining:
  #  print("The event will be cancelled")
#else:
  #  print("The event will be rescheduled")


# conditional expressions

#age = 15

# print("Adult" if age > 15 else "Young")

# a = 10
# b = 11

# max_num = a if a > b else b
# print(max_num)


# a = 10
# b = 20

# min_num = a if a < b else b
# print(min_num)

# age = 25

# print("Adult" if age >= 25 else "Youngster")

#access_level = input("Enter your access level: ")
#name = "Pavle"

# if access_level != "Admin":
   # print("You do not have access level range to access the page.")
# else:
  #  print("Welcome, ",name, "!")
  #  input("\t\t\t\tPlease press the enter key to exit.")

#user_role = input("Please input your user role: ")
#access_level = "You have full access" if user_role == "Admin" else "Your access level is set to 'guest'"
#print(access_level)
#input("\t\t\tPlease press enter key to exit.")


# user_role = "Admin"
# access_level = "Full access" if user_role == "Admin" else "guest"
# print(access_level)

# a = 9
# b = 10

# min_num = a if a < b else b
# print(min_num)
# break


#name = input("Please enter your name: ")
#name = name.replace("a", "b")
#print(name)
#input("\t\t\tPress enter to exit this box: ")


#print(help(str))

#name = input("Please enter your name: ")
#name = name.replace("p", "l")
#print(name)

#name = input("Please enter your name: ")

#if not name.find("b") == -1:
  #  print("Your name cannot contain letter 'b'")
#elif len(name) < 5:
  #  print("Please enter a name that contains more than 5 characters!")
#else:
   # print(f"Welcome, {name}!")


# name cannot contain digits

#name = input("Enter your name: ")

#if name.isdigit() == -1:
  #  print("Name cannot contain digits!")
#else:
   # print("Welcome", name, "!")

#name = input("Please input your name: ")

#if not name.isalpha():
   # print("Your name must contain only letters!")
#else:
 #   print("Welcome", ",", name, "!")

#name = input("Please input your name: ")
#result = name.isdigit()
#print(result)



##username = input("Please input your name: ")
###if not username.count("a"):
   ## print("Your username must contain letter 'a'!")
##elif username.isalpha() or not username.islower():
    #print("Your username must contain at least two numbers and written in lowercase!")
##else:
  #  print("Welcome",username,"!")
#input("\t\t\tPlease press enter key to exit:")

# String indexing


#credit_card = "3467-7890-4346-1231"

#last_digits = credit_card[-4:]
#print(f"XXXX-{last_digits}")

##reverse_credit = credit_card[::-1]
##print(reverse_credit)

#credit_card = "5374-9842-0101-5576"

#credit_numbers = credit_card[6:11]
#print(credit_numbers)

##credit_card = "2334-6478-0304-2346"

##last_digits =  credit_card[::2]
## print(f"The digits are: {last_digits}")

## Format specifiers

#price = 2.90

#print(f"Your favorite food is {price:10,.2f}")


# import random

# the_number = random.randint(1, 100)
# guess = int(input("Please take a guess: "))
# tries = 1

# while guess != the_number:
   #  if guess > the_number:
       #  print("Lower...")
  #   else:
      #   print("Higher...")

   #  guess = int(input("Please take a guess: "))
    # tries += 1


# for x in (range (1, 22)):
  #   print(x)
# word = input("Enter your word: ")
# for letter in word:
  #   print(letter)


# countdown program

# import time



# my_time = int(input("Please enter your time: "))

# for i in range(my_time, 0, -1):
   #  print(i)
  #   time.sleep(1)
# print("USTAJ!!!")

#columns = int(input("Please enter a number of columns: "))
# rows = int(input("Please enter the number of rows: "))
# symbol = input("Please enter the symbol to use: ")

# for x in range(rows):
   #  for y in range(columns):
     #    print(symbol, end= "")
   # print()

#import time


# initializing string
#strn = "Pavle"

# printing geeksforgeeks after delay
# of each character
# for i in range(0, len(strn)):
   # print(strn[i])



#name = ""
# while name == "":
  #  print("You did not enter your name.")
   # name = input("Enter your name: ")
# print(f"Hello, {name}")



#name = input("Please enter your name: ")

# while name == "":
  #  print("You did not enter your name.")
   # name = input("Please enter your name: ")
# print(f"Hello {name}")



#num = int(input("Please enter your number: "))

#while num < 0 or num > 10:
 #   print("Your number is not valid")
 #   num = int(input("Please enter your number: "))

#print(f"{num} is valid")

#input("\t\t\tPress the enter key to exit")

#import random

#number = int(input("Please enter your number: "))

##for x in range(20, 0, -5):
  #  if x == 13:
    #    continue
   # else:
     #   print(x)

#print("Urlam")

# input("\t\t\tPress the enter key to exit. ")


#import time

# my_time = int(input("Please input your time: "))



# for x in range(my_time, 0, -1):
   # print(x)
  #  time.sleep(1)
# print("Urlam")











# import random

# word = "Cestitam"

# high = len(word)
# low = -len(word)

# for x in range (10):
   #  position = random.randrange(high)
   #  print("word[", position, "]\t", word[position])



# print("\t\t\t\t\tYou are the most welcomed person in this group")

#name = "Pavle"

#print(f"Welcome, {name}")

#name = input("Please enter your name: ")

#for letter in name:
   # print(letter, end=" ")


#import time

#my_time = int(input("Please enter your time: "))


#for i in range (my_time, 0, -10):
   # time.sleep(2)
   # print("\n\n\nUSTAJANJE!!!")


#name = 2 , "Zec", 2.55

#print(name)


#guess the name game


#name = "Marko"
#guess = input("Please enter your guess name: ")
#tries = 1


#while guess != name:
   # print("Incorrect! Please try again!")
   # tries += 1
   # guess = str(input("Let`s try again! My name is: "))

#else:
  #  print("Congratulations! That is my name!")



# weight conversion program

# name = input("What is your name? ")
# print(f"Hello {name}!")
# age = int(input("How old are you? "))
# print(f"You are {age} years old. Happy birthday! ")

# rectangle formula practice


# A = w x l

# width = float(input("Please enter the width: "))
# length = float(input("Please enter the length:  "))

# area = float(round(length * width, 1))

# print(f"The total area of the triangle is {area}cm²")


# item = input("What item would you like to buy? ")
#price = float(input("What is the price of your item? "))
#quantity = int(input("How many items would you like to buy? "))
#total = float(round(quantity * price, 1))

#print(f"You have bought {quantity} {item}(s)")
#print(f"Your total is {total} dollars")
#print("\n\nThank you for buying at Yopas!")

#madlib game

#verb1 = input("Please enter a verb: ")
#noun1 = input("Please enter a noun: ")
#noun2 = input("Please enter a noun: ")
#adjective1 = input("Please enter a description: ")
#verb2 = input("Please enter a verb: ")

#print(f"Today i was {verb1} towards {noun1}.")
#print(f"When i met with it, we went together to {noun2}")
#print(f"There, we were {adjective1} and {verb2}.")

#a = 3
#b = 5.5454
#c = 6

#result = round(b, 2)
#print(result)

#result = abs(3)
#print(result)

#result = pow(c, 2)
#print(result)

#result = min(a,b,c)
#print(result)

# import math

#print(math.pi)
#print(math.e)
#x = 3
#result = math.sqrt(x)
#print(result)

#x = 1.9
#print(math.ceil(x))
#print(math.floor(x))



import math


#c = 2pi * r

#radius = float(input("Please enter the radius: "))
#unit = input("Please enter your unit of measure (CM or KM): ")

#circumference = float(round(2*math.pi * radius, 2))

#print(f"The circumference of your circle is {circumference} {unit}")


#A = pi * r^2

#radius = float(input("Please enter the radius: "))
#unit = input("Please enter your unit of measure (CM or M): ")

#area = round(math.pi * pow(radius, 2), 2)
#print(f"Area of the circle is {area} {unit}")


#c = math.sqrt(a)^2

#a = float(input("Please enter side a: "))
#b = float(input("Please enter side b: "))
#c = round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)
# print(f"Side c is {c}")

#age = int(input("Please enter you age: "))

#if age > 100:
  #  print("You are too old to access the content.")
#elif age > 18 and age < 100:
 #   print("Congrats! You are signed up now!")
#else:
   # print("Invalid input. Please try again.")

#is_online = True

#if is_online != False:
   # print("You are offline!")
#else:
   # print("You are ready to connect to the server!")

#operator = input("Please enter your operator (+, -, *, /): ")
#number1 = float(input("Please enter your number 1: "))
#number2 = float(input("Please enter your number 2: "))


#if operator == "+":
 #   result = number1 + number2
  #  print(f"Your result is {result}")
#elif operator == "-":
 #   result = number1 - number2
  #  print(f"You result is {result}")
#elif operator == "*":
 #   result = number1 * number2
  #  print(f"Your result is {result}")
#elif operator == "/":
 #   result = round(number1/number2, 2)
  #  print(f"Your result is {result}")
#else:
 #   print("Your operator is invalid. Please try again.")


# weight converter program

# weight = float(input("Please enter your weight: "))
# unit = input("Please enter the unit of measurement (Kg or Lbs): ")

#if unit == "Kg":
 #   weight = weight*2.205
 #   unit = "Lbs"
 #   print(f"Your weight is {weight} {unit}")
# elif unit == "Lbs":
   # weight = round(weight/2.205, 2)
   # unit = "Kg"
   # print(f"Your weight is {weight} {unit}")
# else:
   # print("The unit entered is invalid. Please try again!")

# temperature conversion program

#temperature = float(input("Please input the temperature: "))
#unit = input("Please enter the unit of measurement (C or F): ")

#if unit == "C":
  #  temperature = round((9 * temperature) / 5 + 32, 1)
  #  print(f"Your temperature in Fahrenheit is {temperature} F.")
#elif unit == "F":
  #  temperature = round((temperature - 32) * 5 / 9, 1)
  #  print(f"Your temperature in Celsius is: {temperature} C.")
#else:
   # print("Please enter a valid input.")

#temp = 10
#is_raining = False

#temp = int(input("Please input the temperature: "))

#if temp > 10 and is_raining == False:
  #  print("The event is live")
#elif temp < 10 or is_raining != True:
 #   print("The event is cancelled")
#else:
# print("Incorrect query")


# num = 23

#print("EVEN" if num % 2 else "ODD")

#a = 10
#b = 6

#min_num = a if a < b else b
#print(min_num)

# temperature = 30

# print("HOT" if temperature > 20 else "COLD")

# user_role = "Nomad"

# print("Full Access" if user_role == "Admin" else "Limited access")


#name = input("Enter your full name:  ")
#result = len(name)
#print(result)

#len(name)
#name.find()
#name.rfind()
#name.capitalize()
#name.upper()
#name.lower()
#name.isdigit()
#name.isalpha()
#name.count("")
#name.replace(,,)
# print(help(str))



# username = input("Please enter your username: ")

#if len(username) > 12:
   # print("Access denied. Please make your username shorter.")
#elif not username.find(" ") == -1:
  #  print("Your username cannot contain spaces! Please try again.")
#elif not username.isalpha():
  #  print("Your username cannot contain digits! Please try again.")

#else:
  #  print(f"Username accepted. Access granted, welcome '{username}'! ")

#credit_card = "1356-45090-2349"

#print(credit_card[0:4])


#price = 3000

#print(f"Price 1 is ${price:>10}")

#name = "Mirko"

#result = name.upper()
#print(result)


#age = int(input("Please enter your age: "))

#while age < 5:
   # print("You are not allowed to access this content.")
    #age = int(input("Please enter your age again:"))
#else:
  #  print("Welcome home!")



# num = int(input("Please enter your number: "))

# while num < 1 or num > 10:
   # print("Your number is not valid. Please enter a number between 1 and 10: ")
  #  num = int(input("Enter you number: "))


# print(f"Thank you, your number is: {num}")

# kamatna stopa

#num = int(input("Please enter your number: "))

# while num < 0 or num > 10:
 #   print("Your number is invalid. Please try again!")
  #  num = int(input("Please enter your number: "))

# print("Great! Your number has been accepted!")


# interesna stopa kalkulator


#while True:
#    principle = float(input("Enter the principle amount: "))
 #   if principle < 0:
        #print("Principle rate cannot be less than zero, please try again.")
 #   else:
   #     break

#while True:
   # rate = float(input("Enter the rate amount: "))
 #   if rate < 0:
  #      print("Rate cannot be less than zero, please try again")
  #  else:
  #      break

#while True:
  #  time = int(input("Enter the time in years: "))
 #   if time < 0:
  #      print("Time cannot be less than a year, please try again. ")
  #  else:
   #     break


#total = principle * pow((1+ rate / 100), time)
#print(f"Balance after {time} year/s is: {total:.2f}$")

#while True:
   # age = int(input("Enter your age: "))
   # if age <= 0:
      #  print("Your age cannot be equal to zero or negative! Please try again!")
   # else:
      #  print(f"Your age is: {age}")
      #  break

#import random

#x = random.randrange(0, 500)
#i =+ 1
#for i in range(x):
    #print(i, x)

#import time

#x = "Urlam"

#time.sleep(2)
#for i in x:
   # print(i)


#print("Urlam od srece", "kao nikada dosad", end ="")
#print("\t\nCestitalica")
#print("Urlam kao zmaj", "A ti se ne das")
#print("Urlam \\ Kao zmaj", "Lepa 'lukic'")
#print("\a")
#print("You\t" + "can`t concatenate" + "\tInteger and" + \
#"\ta string", "\n")
#result = 20 + 5

#print("20 + 5 =", result)
#name = "Pavle"
#print(name.upper())
#print(name.lower())
#print(name.capitalize())
#print(name.rfind("v"))
#print(name.swapcase())
#print(len(name))
#print(name.replace("P","L"))
#print(name.title())
#print(" You can`t\t" + "concatenate this\t"+"str"+"ing")
#print(name.casefold())
#print(name.capitalize())


#x = 5

#name = "Pavle"
#result = name * 52
#print(result)

#car = input("Enter the desired car: ")
#loan = int(input("Enter the monthly amount of loan: "))

#while loan >= 12:
  #  print("The entered amount cannot be greater than 12")
   # loan = int(input("Enter the monthly amount of loan: "))
#print("Application accepted! Thank you for your application for the loan program")

#favourite_dish1 = input("Please enter the first favourite dish: ")
#favourite_dish2 = input("Please enter the second favourite dish: ")

#dish = favourite_dish1 + favourite_dish2
#print(dish)

#Napojnica

#predjelo = float(input("Molimo unesite cenu predjela (RSD): "))
#glavno_jelo = float(input("Molimo unesite cenu glavnog jela (RSD): "))
#pice = float(input("Molimo unesite cenu pica (RSD): "))

#total = round(predjelo + glavno_jelo + pice, 2)
#print("Vas racun iznosi", total,"RSD")

#napojnica1 = round((20*total) / 100, 2)
#print("Napojnica koju dajete konobaru iznosi: ", napojnica1, "RSD")

#pass

#predjelo2 = input("Unesite svoje predjelo: ")
#cena_predjelo2 = float(input("Unesite cenu predjela (RSD): "))
#jelo2 = input("Unesite svoje glavno jelo: ")
#cena_jelo2 = float(input("Unesite cenu glavnog jela (RSD): "))
#pice = input("Unesite svoje pice: ")
#cena_pice = float(input("Unesite cenu pica: "))

#total2 = round(cena_predjelo2 + cena_jelo2 + cena_pice, 2)
#print("Vas racun iznosi: ", total2, "RSD")

#napojnica2 = round((15*total2) / 100, 2)
#print("Vasa napojnica konobaru iznosi: ", napojnica2, "RSD")


#Prodavac automobila


#automobil = input("Unesite ime automobila: ")
#cena_automobil = float(input("Unesite osnovnu cenu automobila (EUR): "))
#porez = round((cena_automobil * 5) / 100, 2)
#registracija = round((cena_automobil * 10) / 100, 2)
#ukupan_porez = round(float(porez + registracija), 2)
#print(f"Ukupan porez je {ukupan_porez:.3f}", "EUR")

#provizija_prodavca = float(input("Unesite proviziju prodavca (EUR): "))
#transport = float(input("Unesite cenu transporta (EUR): "))

#total = cena_automobil + ukupan_porez + provizija_prodavca + transport
#print("Ukupna cena automobila je:", total, "EUR")

# Guess my numberd

#import random


#number = random.randint(0, 100)
#guess = int(input("Please enter your number: "))
#tries = 1

#while guess != number:
  #  if guess > number:
  #      print("Lower...")
  #  else:
 #       print("Higher...")

 #   guess = int(input("Please enter your number: "))

 #   tries += 1

#print("Congratulations! The correct number is: ",number)

#input("Please press enter to exit the program: ")


#kolacic srece


#definition1 = "Sreca je kada se igras sa ljubimcem!"
#definition2 = "Sreca je kada ispijas jutarnju kafu sa nekim!"
#definition3 = "Sreca je kada se ljubis sa nekim!"
#definition4 = "Sreca je kada se bavis sportom!"
#definition5 = "Sreca je kada trcis po kisi!"


#import random

#choice = random.randint(1, 5)

#if choice == 1:
#    print("Vas odabrana definicija je: ", definition1)
#elif choice == 2:
 #   print("Vas odabrana definicija je: ", definition2)
#elif choice == 3:
  #  print("Vas odabrana definicija je: ", definition3)
#elif choice == 4:
 #   print("Vas odabrana definicija je: ", definition4)
#elif choice == 5:
  #  print("Vas odabrana definicija je: ", definition5)
#else:
   # print("Molimo pokusajte opet!")



# bacanje novcica

#coin_flip = broj bacanja novcica koji je jednak 100 puta
##coin_tail je pismo
##coin_head je glava

#import random

#print("Dobrodosli u bacanje novcica, vas prvi simulator bacanja novcica! Pismo ili glava?\n")


#coin_flip = 100
#coin_head = random.randrange(0, 51)
#coin_tail = int(coin_flip - coin_head)



#print("Novcic je bacen", coin_flip, "puta\n")

#print("Glava je bacena", coin_head, "puta")

#print("Pismo je baceno", coin_tail, "puta")

#Guess my number


#Login programe

#username = ""
#password = ""
#security = 0

#while not username:
  #  username = input("Please input your username: ")

#while not password:
   # password = input("Please input your password: ")


#if username == "Marko" and password == "Urlam123":
  #  print("Welcome", username,"!")
  #  security = 5
   # print("Access granted.")
#elif username == "Cmist" and password == "Urlauk321":
   # print("Welcome", username,"!")
  #  security = 3
#elif username == "Beli" and password == "Pegla123":
 #   print("Welcome", username,"!")
  #  security = 7
   # print("Access granted")
#else:
   # input("Access denied. You are not so exclusive!")

# Guess my number

import random
from turtledemo.clock import datum


#the_number = random.randint(1, 100)
#guess = int(input("Please enter your number: "))
#tries = 1


#while guess != the_number and tries <= 10:
  #  if guess < the_number:
       # print("Higher..")
   # else:
      #  print("Lower...")

  #  if tries >= 10:
     #   print("Game over! You have exceeded number of",tries,"tries!")
     #   break


  #  guess = int(input("Please enter your number: "))
 #   tries +=1

#else:
   # print("You guessed it! The number was", the_number,"!!")
   # print("And it only took you", tries, "tries!\n")



#input("\n\nPress the enter key to exit.")



#def add(a, b):
   # return a * b

#result = add(5, 9)
#print(result)


#Igrac bira celobrojni broj izmedju 1 i 100.
# Izabrao je celorojni broj i pamti ga.
# Program ispisuje uvodnu recenicu.
# Kompjuter pokusava da pogodi broj.
#Bira po deseticama: 10, 20, 30.
#Igrac, nakon 10 kaze: "Vise..! Nakon 20 takodje kaze "Vise!" Nakon 30 takodje kaze "Vise"!
#Kompjuter pita: "Da li je taj broj veci od 50 a manji od 60?
#Igrac odgovara: "Da"
#Kompjuter pita: Da li je taj broj manji ili veci 55?
# Igrac odgovara: "Manji".
# Kompjuter pita: Da li je to broj 53?
#Igrac: "Ne"
#Kompjuter: "54"?
#Igrac: "Ne"
#Kompjuter: 52?
#Igrac: "Bravo! Pogodio si!" Zamisljeni broj je 52!

#inventory = ("wallet", "money","sandwich")

#high = len(inventory)
#low = -len(inventory)

#for letter in inventory:
  #  if letter >= 0:
  #  print(letter[1])
#else:
 #   print("Urlam")

#RECI = "aeiou"


#inventory = ()

#if not inventory:
 #   print("You are empty handed")
 #   inventory = ("Sword",
        #         "axe",
       #          "shield",
        #         "healing potion")

   # print("The tuple inventory is: ")
 #   print(inventory)

#input("\t\tPress the enter key to discover your inventory.")



#lista filmova

#name = input("Please enter your name: ")
#print("Hello,", name,"!")

#count = True

#start_num = int(input("Please enter your starting number: "))
#end_num = int(input("Please enter your ending number: "))
#step = int(input("Please enter your step you want to count by: "))

#for x in range(start_num, end_num, step):
  #  if start_num >= end_num or start_num <= 0:
   #     print("Please input a valid integer! Cannot be less than 0 or greater than end number! ")
   # elif end_num <= start_num:
    #    print("End number cannot be less or equal than starting number! ")
  #  else:
    #    print(x)

#input("\n\nPlease enter enter key to exit! ")


# Chapter 4, Challenge 1
# Write a program that counts for the user.
# Let the user enter the starting number, the ending number, and the amount by which to count.

#start = int(input("What number should I count from: "))
#end = int(input("What number should I count to: "))

#while start != end:
 #   print(start)
  #  if start < end:
    #    start = start + 1
 #   if start > end:
      #  start = start - 1

#print(end)
#input('Finished! Press enter.')


#message = input("Please enter your message: ")

#while message:
   # print(message[::-1])
 #   break
#input("Press the enter key to exit.")


#nested = [("Pavle", 2000), ["Pavle", "Filip", "Aleksa", "Bakoc"]]
#print(nested[0][1])

#star_num = int(input("Please enter the starting count number: "))
#end_num = int(input("Please enter the ending count number: "))
#step = int(input("Please enter the step number: "))
#count = None

#while star_num > end_num or end_num == 0:
  #  print("Your count is not valid. Please try again!")
  #  break

#print("\nYour count is:  \n")

#for num in range(star_num, end_num, step):
  #  print(num)
  #  if num == 20:
    #    continue
#else:
  #  print("\nYou have reached your end. Congratulations!")
  #  input("\n\nPress enter key to exit.")



#user_message = input("Please enter your message: ")

#print("\n\nYour reversed message is: ", user_message[::-1])

#input("\nCongrats! You have reached the end of the program. Press enter key to exit.")

#lista = ["keys", "lighter", "wallet", "burger", "asparagus"]

#lista.append("kaktus")
#print(lista)
#lista.remove("kaktus")
#print(lista)
#lista.sort()
#print(lista)
#lista.insert(1,"asparagus")
#print(lista)
#x = lista.index("lighter")
#print(x)
#lista.count("burger")
#print(lista)
#lista.pop(1)
#print(lista)


#lista = [("Pavle", 1000),("Marko", 2000),("Goran", 3000),("Jesenka",4000)]
#print(lista[0][1])
#print(lista[1][1])
#print(lista[3][1])
#print(lista[2][1])

#for i in lista:
   # print(i)

#print(lista.sort(reverse=True))

#ime, rezultat = ("Pavle", 1000)
#print(ime)
#print(rezultat)



#name, object, number = ("Pavle", "box", 126)



#print(name.isdigit())

#if name.isalpha():
  #  print("\nYour string is made of digits.")
#else:
 #   print("\nYour name does not contain digits.")

#input("\nPress the enter key to continue.")

#result = [("Pavle", 2000), ("Petar", 1000), ("Marija", 1500)]
#print(result[2][1])

#ime, rezultat = ("Pavle", 2000)

#print("Vas rezultat je",rezultat,"!")

#result.sort()
#print(result)

#result[1] = ("kita", 50)
#print(result)

#del result[1]
#print(result)

#del result[1:2]
#print(result)

#result = result.insert(1, ("Kita", 200))
#print(result)

#poklon1 = ["Pavle", ("lopta", "olovka")]
#poklon2 = ["Marko", ("reket", "sveska", "knjiga")]
#poklon3 = ["Goran",("ikona","sveca","slika")]
#poklon4 = ["Jesenka",("slika","escajg", "noz")]
#poklon5 = ["Pago", ("koska", "granule")]


#print(len(poklon2[1][0:]))

#pavle = ["jakna", "dzemper", "sako"]
#marko = pavle
#print(marko)
#vladan = pavle
#print(vladan)

#pavle[1] = "duks"
#print(pavle)
#print(vladan)
#print(marko)

#marko = pavle[:]
#print(pavle)
#marko[1] = "farmerke"
#print(marko)


#dictionary = {"spanish":"español",
             #   "german":"alemán",
           #   "english":"inglés"}

#print(len(dictionary))

#for term in dictionary:
 #   print(term)

#if "spanish" in dictionary:
   # print("Concha tu madre!!!!!")
#else:
  #  print("Urlam!")

#var = dictionary["spanish"]
#print(var)

#if "spanish" in dictionary:
  #  print("True")
#else:
  #  print("No se ha podido encontrar la traducción correspondiente.")

#print(dictionary.get("danish", "Concha tu madre!"))
#print(dictionary.get("spanish","No way, mate."))

#print(dictionary.get("english"))
#print(dictionary.keys())
#print(dictionary.values())
#print(dictionary.items())



#recnik = {"jugar":"igrati",
      #    "comer":"jesti",
        #  "saltar":"skociti"}


#rint(recnik.get("comer"))

#print(recnik.values()
 #     )

#for key in recnik:
   # print(key)
#else:
    #recnik.get(())






#Program ispisuje listu reci nasumicnim redosledom



#reci = ["ovca", "koza","vuk","labud","zirafa"]

#import random

#izbor = []

#while len(reci) != 0:
   # x = random.choice(reci)
 #   print(x)
#    reci.remove(x)
   # input("Press enter to see another word.")

# input("That`s it!")



## rectangle


#columns = int(input("Please enter the number of columns: "))
#rows = int(input("Please enter the number of rows: "))
#symbol = input("Please enter the sybol you want to use: ")

#for i in range(columns):
   # for x in range(rows):
     #   print(symbol, end="")
   # print()



#fruit = ["banana", "apple", "orange", "lemon"]
#print(fruit[0:3:2])

#input("\nPress the enter key to exit.")

#fruit.insert(0, "lemon")

#print(fruit)


#num_pad = [(1, 2, 3),
      #     (4, 5, 6),
      #     (7, 8, 9),
      #     ("*", 0, "#")]

#for row in num_pad:
 #   for num in row:
    #    print(num, end=" ")
  #  print()






# fruits = ["banana","orange","pineapple","apple"]
# meats = ["steak","beef"]
# liquids = ["water","milk","coke","juice"]

# health = (fruits, meats, liquids)
# print(health)
# print([health[0][2]])

# print("\n\n")


# for x in health:
  #  for name in x:
  #      print(name, end=" ")
  #  print()





#num = [[1, 2, 3],
     #  [4, 5, 6],
    #   [7, 8, 9],
     #  ["*", 0, "#"]]

# for row in num:
   # for y in row:
    #    print(y, end =" ")
   # print()


#fruits = ["banana","apple","orange","grape"]
# vegetables = ["potato","tomato","carrot","ginger"]
#meats = ["turkey","lamb","fish","beef"]

#health = (fruits,vegetables,meats)
# print(health)

#print(health[0][1])

#for fruit in health:
 #   for x in fruit:
    #    print(x, end=" ")
  #  print()


# Quiz game


#questions = ("1. Koja je najvisa zgrada u Beogradu?\n",
    #         "2. Koliko uglova ima trougao?\n",
      #       "3. Kako se zove najveca ulica u Beogradu?\n",
    #         "4. Koji klub iz Srbije je osvojio kosarkasku Evroligu?\n",
     #        "5.  Koji klub iz Srbije je osvojio Ligu sampiona u fudbalu?\n")

#options = (("A. Geneks", "B. Beogradjanka", "C. Kapetan Misino zdanje", "D. Zgrada poste"),
   #        ("A. 4", "B. 10", "C. 3", "D. 6"),
    #       ("A. Knez Mihajlova", "B. Kneza Milosa", "C. Njegoseva", "D. Dimitrija Tucovica"),
        #   ("A. Borac iz Cacka", "B. FMP", "C. Crvena Zvezda", "D. Partizan"),
    #       ("A. Partizan", "B. Rad", "C. OFK Beograd", "D. Crvena Zvezda"))


#answers = ("A", "C", "A", "D", "D")
#guesses = []
#score = 0
#question_num = 0


#print("\n\nWelcome to quiz!!!")



#for question in questions:
 #   print("--------------------------------------\n")
  #  print(question)
  #  for option in options[question_num]:
   #     print(option)

  #  guess = input("\nEnter A, B, C, D: ").upper()
 #   guesses.append(guess)
 #   if guess == answers[question_num]:
  #      score+=1
    #    print("CORRECT!")
  #  else:
 #       print("INCORRECT!")
 #       print(f"{answers[question_num]} is the correct answer.")
 #   question_num+=1


#print("\n\n----------------------------")
#print("---------RESULTS------------")
#print("----------------------------")

#print("\nanswers", end=" ")
#for answer in answers:
  #  print(answer, end=" ")
#print()

#print("guesses", end=" ")
#for guess in guesses:
  #  print(guess, end=" ")
#print()


#score = (score / len(questions) * 100)
#print("\n\nYour score is ", score,"%")
#print(input("\nPress the enter key to exit."))


# import random


# low = 1
# high = 200

#numbers = random.randrange(0, high)
# print(numbers)
#input("\nPress the enter key to exit.")

# options = ("yes", "no", "i do not know", "for sure")

# choice = random.choice(options)
# print(choice)
# input("\nPress the enter key to exit.")

# cards = [1, "kurac", "YES", 7.88, True, "32", 99]

#random.shuffle(cards)
# print(cards)
# input("\nPress the enter key to exit.")

# print("\n----------THE END-------------"
      
      
    #   "\n\t------------YOU SUCK, BTW :* ------------")





# def podaci(ime, prezime, godina_rodj):
 #     print("Kako ste gospodine?")
     # print(f"\nDacete mi svoje ime i prezime.")
     # print(f"\nZovem se {ime} {prezime}.")
     # print("\nKada ste rodjeni? ")
    #  print(f"\nRodjen sam {godina_rodj}.")


#podaci("Pavle", "Radovanovic", "1995")


#def add(x, y):
   #   z = x +y
    #  print(z)
#add(1, 3)

#def subtract(x, y):
    # return x // y
#result = subtract(10, 2)

# print(result)

#def sum(x, y):
  #    return x + y
# result = sum(5, 6)
# print(result)



#def cestitanje(name):
    #  print(f"Happy birthday,",name,"!")

#cestitanje("Pavle")

#def sum (x, y):
  #    return x + y
#result = sum(4, 5)
#print(result)


#for i in range(result):
     # print(i)


#def zvanje(ime, prezime):
  #    print("Hello", ime, prezime,"!")
#zvanje("Marko", "Ciganovic")


#def cestitka(ime, prezime):
 #     print("Srecan rodjendan", ime, prezime,"!!!")
#cestitka("Marko","Radovanovic")

#def zbir(x, y):
 #  z = x + y
 #  return z
#print(zbir(5, 6))



#def stanje (ime, prezime, broj_rac, dug):
  #    print("Dobar dan,",ime, prezime," .Unesite svoj broj racuna: ", broj_rac, "Vase dugovanje iznosi:", dug)
#stanje("Pavle", "Radovanovic", 3454521344, "565.77")





#def podaci(ime, prezime, datum_rodj, grad):
   #   return f"{ime}{prezime}{datum_rodj}{grad}"
#Pavle = podaci(prezime = "Pavle",ime = "Radovanovic", datum_rodj ="\t""11.7.1993""\t", grad ="Beograd")
#print(Pavle)



#def sum(*args):
   #   total = 0
     # for arg in args:
  #          total+=arg
     # return total
#print(sum(1, 6, 8, 10))




# skup_br = [2, 3, 4 , 5 , 6, 7]

# for broj in skup_br:
   #    print(broj)

# imena = {"orange" : "naranja",
   #      "apple": "manzana",
       #  "blueberry": "arrandano",
     #    "banana":"platano"}

#for i in imena:
   #  print(i)


#print("\n\n")

#for i in imena.values():
    #  print(i)

#for i in imena.keys():
     # print(i)


#for key, value in imena.items():
   #   print(f"{key} : {value}")






#import math

#res = int(math.remainder(10, 3))
#print(res)



#def display(message):
 #   print(f"Here`s your message:", message, "!")
#print(display("Hello!"))


#def birthday(age,name):
   # print("Happy birthday,", name,"!!!", "You are", age, "years old.")


#birthday(6, "Marko")

#def birthday(age = 6, name = "Marko"):
    #print("Hello, ", name,". I heard that you are now", age, "years old!")
#birthday()
#print("\n\n\n")

#training_plan = {"CUT" : 1,
              #   "GAINER":2,
             #    "LOSING WEIGHT PROGRESS":3}

# kalkulator podignute tezine iliti izbor trening plana


#for keys, values in training_plan.items():
   # print(keys, values)



# list comprehension






# name = ("Milos")


# height = float(input("Please enter your height: "))
#print("Your height is",height,"cm")
#input("Press enter key to exit.")
#height_m = int(input("Please enter your height in meters: "))
#height_m = height / 100
#print(f"Your height in meters is: {height_m: .2f}","m")
#input("Press enter key to exit.")



# napraviti sledece varijable> program_name, version, is_new_program

#program_name = "Pavlov program"
#version = 13.2
#is_new_program = True

#print(program_name, version, is_new_program)
#print("\n")


#books = ["Seobe", "Na Drini cuprija", "Roman o Londonu"]
#print(books[0])

#books.append("Rani jadi")
#print(books)

#books[0] = "Decaci Pavlove ulice"
#books.remove("Roman o Londonu")
#print(books)

#name = "Pavle"
#last_name = "Radovanovic"
#age = 31


#print("Ja se zovem " + name + ". ""Prezivam se " + last_name + " i imam " + str(age) + " godinu. ")


#print("\n")

#odaci = {"ime": "Pavle",
          #       "prezime": "Radovanovic",
        #  "godina": 23,
        #  "hobbies": ["programiranje", "treniranje", "druzenje"]}



#print(podaci["hobbies"][1])


#ljudi = {"Pavle":"Radovanovic",
        # "Milos":"Obrenovic",
     #    "Luka": "Filipovic"}

# person1 = first_name, last_name
#person2 = first_name, last_name
#person3 = first_name, last_name
#person4 = first_name, last_name

#people = {"person1":
    #          {"first_name": "Pavle",
       #        "last_name": "Radovanovic"},
      #    "person2":
       #       {"first_name":"Marko",
           #    "last_name":"Radovanovic"},
        #  "person3":{"first_name":"Goran",
           #          "last_name":"Radovanovic"},
     #     "person4":{"first_name":"Pavle",
              #       "last_name":"Radovanovic"}
      #    }



#print(people.values())

#age = int(input("Please enter your age: "))
#name = input("Please enter your name: ")
#allowed_age = 18
#username = name+str(age)
#print("\n")
#if age >= 18:
   # print(f"You have access now. Welcome! Your username is: {username}.")
#else:
    #print("You must be at least 18 years old in order to access the site.")
#print("\n")
#print(f"------------------WELCOME, {username}-------------------")
#print("\n")
#input("Press the enter key to exit.")


#name = input("Please enter your name: ")
#password = input("Please enter your password: ")

#if name == "Pavle" and password == "Urlam123":
   # print("Welcome Pavle-Admin.")
#elif name == "toma" and password == "mentorstva":
   # print("Welcome, Tomo. Kako si danas?")
#elif name == "Marija" and password == "Marija123":
 #   print("Welcome, Marija!!!")
#else:
   # print("You are not admin! Please enter your password again!")

#print("\n")
#input("Press the enter key to exit.")

#tajni_pin = int(input("Please enter your PIN: "))
#tries = 1
#amount = 1
#options_main = {"1":"Cash withdrawal",
           #"2":"Payments",
          # "3":"Invoices",
          # "4": "Money deposit"}
#choice = 1
#bank_telephone = 45335698754


import json


with open("GIT/data/user.json", "r") as file:
    data = json.load(file)
    print(data)
    data.append({

          "name": "Petar",
          "age": 50,
          "gender": "male",
          "height": 190,
          "weight": 86})

    print(data)



print(data)





with open("GIT/data/user.json", "w") as file:
    json.dump(data, file, indent = 3)
    print(data)






































































































































































































































































































































































































