#proizvodi = ["iPhone 11", "iPhone12","iPhone13", "iPhone14", "iPhone15", "iPhone16"]

#proizvodi.append("iPhone 16 Plus")
#print(proizvodi)

#item_search = input("Please enter the phone you would like to find: \n")

#if item_search in proizvodi:
   # print("\nWe have found your phone: ",item_search)
#else:
    #print("We have not found your phone.")

#input("\nPress the enter key to exit.")


#user_age = int(input("Please enter your age: "))

#if user_age <= 18:
 #   print("You are a youngster.")
#elif user_age >= 18:
   # print("You are an adult.")
#else:
 #   print("Your input is not valid. Please try again.")
  #  user_age = input("Please enter your age: ")
#print("You are",user_age,"years old.")


#age = int(input("Please enter your age: \n"))

#if age in range (-100, 0):
  #  print("Age cannot be less than 0.")
  #  quit()
#elif age in range(0, 19):
 #   print("You are a teenager.")
#elif age in range(19, 56):
 #   print("You are an adult.")
#elif age in range(56, 81):
   # print("You are a retiree.")
#elif age in range(81, 100):
  #  print("Are you still alive?")
#else:
   # print("Please enter a valid value.")

#input("\nPress the enter key to exit.")

#import time

#proizvodi = {"Krevet": 300,
           # "Lopta":400,
          #  "Stolica":900,
          #  "Stolnjak":30}

#proizvod_search = input("Please enter your proizvod: \n").title()

#if proizvod_search.title() in proizvodi:
  #  print("Your proizvod,",proizvod_search,"is in the list. \n")
  #  time.sleep(3)
   # print("Its price is set to", proizvodi[proizvod_search],"$.\n")
#else:
    #print("You proizvod is not in the list. Goodbye.")
#input("\nPress the enter key to exit.\n")

#print("Here is the list of the proizvodi: \n")

#for keys, values in proizvodi.items():
   # print(f"{keys} - {values}")

# import time

#total = int(input("Please enter your total: "))

# if total >= 1000:
  # discount= 10%total
    #discounted = total * 0.1
   # discounted_price = total - discounted
 #   time.sleep(2)
  #  print(f"You have obtained {discount: .2f},% discount, which is:{discounted: .2f} EUR")
  #  print(f"Your final total is: {discounted_price: .2f} EUR")

#else:
  #  print("\nYou are not eligible for discount application.")

#input("\nPlease press enter to exit the discount bag calculator.")




# napisati petlju koja ispisuje brojeve od 0 do 100, ali samo parne brojeve

#age = ""
#age = input("Koliko imas godina? ")

#while not age.isdigit() or int(age) < 18:
    #age = input("Koliko imas godina? ")
#print("Imas",age,"godina.")


#pitati korisnika da unese ima proizvoda
#kada unese ime proizvoda, prizvod dodati u kasu
#korisnik mora uneti 3 proizvoda ukupno






#kasa = []
#proizvod = input("Unesite ime proizvoda: ")


# while len(kasa) <=2:
   # kasa.append(proizvod)
 #   proizvod = input("Unesite ime proizvoda: ")
   # if len(kasa) == 3:
      #  print("\nStop! Maksimalan dozvoljen unos proizvoda je:", len(kasa), "\n")
       # print("Vasa kasa izgleda ovako: \n")
       #for i in kasa:
         #   time.sleep(3)
          #  print(i)







# ispisivanje petlje koja sadrzi imena ucenika koji su aktivni i njihovog skora

# for student in students:

   # if not student["active"]:
      #  continue

  #  if student["score"] <= 30:
     #   student["grade"] = "D"

 #   elif student["score"] <= 70:
     #   student["grade"] = "C"

   # elif student["score"] >= 71:
    #    student["grade"] = "A"

 #   else:
     #   print(f"Student", student["name"],"not eligible")

 #   print(student["name"], "-", student["score"],"-", student["grade"])




import time
import random

from def_domaci_9 import calculate_delivery

# random numbers
options = None
allowed_options = ["Start", "Exit", "History", "Scores"]
game_history = []
player_name = ""
player_score = 0
scores = []
tries = 10
guess = None
score_table = []
max_score = 0


while options not in allowed_options:
    options = input("What would you like to do? (Start, Exit, History, Scores, Score Table): ").title()

    if options == "Start":
        player_name = input("Please enter your name: ")
        print(f"\nHello, {player_name}!!!")

        time.sleep(2)

        print("\n-------------NUMBER GUESSING GAME-------------\n")

        num = random.randrange(0, 101)
        tries = 10
        total_tries = 1
        print("Let`s try to guess the number between 1 and 100.\n")
        print(f"You have {tries} tries in total.\n")

        print(guess)
        while guess is None:
            print("Ok while")
            guess = int(input("Let`s try to guess the number: "))

        while guess != num and tries > 0:

            if guess < num:
                print("higher...")
            else:
                print("lower...")

            tries -= 1
            total_tries += 1
            guess = int(input(f"Incorrect! You have {tries} tries left. "))


        if guess == num:

            msg = "\n----------------CONGRATULATIONS-----------------\n"
            print(msg)
            print(f"You guessed it!!! The correct number was {num}!!!")
            game_history.append(f"You guessed it!!! The correct number was {num}!!!")
            print(f"\nIt took you only {total_tries} tries!!!\n")
            player_score = total_tries
            print(f"\nYour score is: {total_tries}\n")
            options = None


        elif tries == 0:
            msg = "\n------------------GAME OVER----------------------\n"
            print(msg)
            print(f"Game over. You had your {total_tries} tries.")
            game_history.append(f"Game over. You had your {total_tries} tries.")
            print(f"The correct number was {num}.")
            options = None
            guess = None




    elif  options == "Exit":
            print("You don`t want to play the game. Bye.")
            quit()


    elif options == "History":
        print(game_history)
        options = None


    elif options == "Scores":

        msg = "\n------------------SCORES-------------------\n"
        for i in msg:
            time.sleep(0.05)
            print(i, end=" ")

        def add_scores(name, score):
            scores.append((player_name, player_score))
            return scores

        scores = add_scores(player_name, player_score)

        print(scores)

        if not scores:
            print("\nNo scores recorded yet.\n")

        options = None


    elif options == "Score Table":
        for score in scores:
            score_table.append({"player": player_name, "score": player_score})
        print(score_table)
        options = None



sorted_scores = sorted(scoreboard.items(), key=lambda item: item[1])








