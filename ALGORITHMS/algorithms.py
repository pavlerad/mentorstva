

numbers = [3, 5, 7, 18, 4, 7, 9, 7, 5]

duplicates = []
seen  = set()

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

#pronadji broj 7


#for number in numbers:
  #  if number in duplicates:
       # duplicates.append(number)
   # else:
      #  seen.add(number)

#print(duplicates)



#print(f"Number seven has been shown")



numbers = [4, 2, 6, 9, 7]

numbers_lenght = len(numbers) #duzina liste
print(numbers_lenght)

#range_nums = (range(numbers_lenght)) #rang liste
#print(range_nums)


#bubblesSort


for i in range(numbers_lenght):
    print(i)
    swapped = False
    for j in range(0, numbers_lenght - i - 1):
        if numbers[j] > numbers[j+1]:
           numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
           swapped = True
    if not swapped:
        break

print(numbers)



#Fibonacci ---> saberi poslednja dva broja, sabira do 100


#num = [0,1]

#1+0 = 1 ---> [0, 1, 1]
#1+1 = 2 ---> [0, 1, 1, 2]
#2+1 = 3 ----> [0, 1, 1, 2, 3]
#3+2 = 5 ---> [0, 1, 1, 2, 3, 5]


numbers = [0, 1]

while numbers[-1] < 100:
    next_number = numbers[-1] + numbers[-2]
    if next_number > 100:
        break
    numbers.append(next_number)
print(numbers)










def zbir(name ="Marko",age= 16):
    print(f"Hello {name}. You are {age} years old.")
zbir("Uros")



