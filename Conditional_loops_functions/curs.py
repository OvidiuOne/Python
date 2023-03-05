# Exemplu 1
# #a = 15
# print(a)
# print("Valis instruction.")
# # daca nu declaram a , ne apare eroare.

# #Exemplu 2
# a = "15" # atenti  sir de caractere
# b =  "3"
# print(a+b)  # rezultatul est 153
#
# #Exemplu 2
# a= "15"
# b= int(a) # b este numar intreg

#Exemplu 4 - imput    - ne folosim de blocul try....except
# user_input = input("insert a number: ")
# user_input = int(user_input) # valoare intreaga a numarului - o punem intr-un try.
# print(user_input, type(user_input))

# Ne folosim de blocul try....except
# user_input = input("insert a number: ")
#
# try:
#     user_input= int(user_input)
# except ValueError as e: #e de la exeption
#     print(e)
#     print(f"You inserted '{user_input}' witch is not a valid number!")
#
# print("valid instruction.")

# user_input = input("insert a number: ")
#
# try:
#     user_input= int(user_input)
#     print(undefined_variable)
# except ValueError as e:
#     print(f"You inserted '{user_input}' witch is not a valid number!", e, type(e))
#
# print("valid instruction.")

#tratare mai multe exceptii

# exemple
# user_input = input("insert a number: ")
#
# try:
#     user_input= int(user_input)
#     print(undefined_variable)
# except (ValueError, NameError) as e:
#     print(f"You inserted '{user_input}' witch is not a valid number!", e, type(e))
#
# print("valid instruction.")

# user_input = input("insert a number: ")
#
# try:
#     user_input= int(user_input)
#     print(undefined_variable)
# except ValueError as e:
#     print(f"You inserted a ValueError witch is not a valid number!", e)
# except NameError as e:
#     print(f"You inserted a NameError witch is not a valid number!", e)
# except KeyError as e:
#     print(f"You inserted a KeyError witch is not a valid number!", e)
# except IndexError as e:
#     print(f"You inserted a IndexError witch is not a valid number!", e)
#
# print("valid instruction.")

#PROGRAMARE CONDITIONALA IF , ..elif, ..else - se va rezuma la tru sau false.

# user_age = input("Age:")
# #user_age = int(user_age)
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age.")
#
# if type(user_age) == int and user_age >= 18:
#     print("You are a grown up!")

# Exemplu 1
# user_age = input("Age:")
#
# try:
#     user_age = int(user_age)
# except ValueError:
#     print("Invalid age.")
#     sys.exit(0)
# else:                            # else la exceptie
#     if user_age >= 18:
#         print("You are a grown up!")
#     else:
#         print("You are a child!")
# finally:     # se afiseaza la final
#     print("End the program")

# if - elif - else
# user_age = int(input("Age:"))
#
# if user_age <14:
#     print("Nu are buletin")
# elif user_age < 18:
#     print("Este un copil")
# elif user_age < 65:
#     print ("Este un adult")
# else:
#     print ("Este un pensionar")

#Structuri repetitive - while( se verifica conditia si apoi se executa codul ) - for

# while True:   # nr necunoscut de pasi
#     print("Inside whipe loop")

# my_numbers = [54, 23, 78, -2] #len(my_numbers) = 4
# # for item in my_numbers:
# #    #print(item)
# #     print(f"Item with value = {item} is on index " = {my_numbers.index(item)}")
# #print(list(enumerate(my_numbers)))    # arata indexul pe care se afla elementele
# for element in enumerate(my_numbers):
#     #print(element, type(my_numbers))
#     print(f"Item with value = {element[1]} is on idex = {element[0]}")

# for index, number is enumerate(my_numbers):
#     print(f"Item with value = {number} is on index = {index}")

# my_numbers = [12, 56,-2, 14]
# index = 0
# while index < len(my_numbers):
#     print(f"Item with value = {my_numbers[index]} is on index = {index}")
#     index = index + 1


#Exemplus continuat cu while.
# is_valid_age = False
# while not is_valid_age:
#     user_age = input("Age:")
#
#     try:
#         user_age = int(user_age)
#     except ValueError:
#         print("Invalid age.")
#     else:                            # else la exceptie
#         if user_age >= 18:
#             print("You are a grown up!")
#         else:
#             print("You are a child!")

# # Continue
# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if number % 2 == 0:
#         print(f"Number = {number} is even.")
#         continue   # se trece la urmatorul
#
#     print(f"Number = {number} is odd")

# #Break
# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if number % 2 == 0:
#         print(f"Number = {number} is even.")
#         break   # se iese si restul de numere nu va mai fi parsate - se opreste structura repetitiva.
#
#     print(f"Number = {number} is odd")

# #pass -
# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     pass # Nu faec nimic - sa valideze sintaxa

#exemplu


# num_attempts = 0
# while num_attempts < 5:
#     try:
#         user_age = int(input('user_age: '))
#         break
#     except ValueError:
#         num_attempts += 5
#         print("Invalid age.")
#     else:
#         print("Too many attempts")
#         continue
#
#     if user_age >= 18:
#         print("You are a grown up!")
#     else:
#         print("You are a child!")
#     break

# Diferenta de la while si for - sa modificam codul ( de la 0 ) , utilizatorul sa introduca gresit de maxim 5 ori

# while True:
#
#     try:
#         user_age = int(input('user_age: '))
#     except ValueError:
#         print("Invalid age.")
#         continue
#
#     if user_age >= 18:
#         print("You are a grown up!")
#     else:
#         print("You are a child!")
#     break

