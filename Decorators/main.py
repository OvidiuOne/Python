# pachete predefinite.

# #Exemplu
# import random
# import time
#
#
# if __name__ == "__main__":
#     print("I will wait for 5 seconds.")
#     time.sleep(5)
#     print("I will continue program.")
#     my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(random.choice(my_numbers))


# if __name__ == "__main__":
#     max_tries = 3
#     current_try = 1
#     while True:
#         user_age = input("Age: ")
#
#         try:
#             user_age = int (user_age)
#         except ValueError:
#             print("Invalid age. Try again.")
#             curent_try += 1
#             continue
#
#         if user_age <= 18:
#             print("You have not acces here")
#         else:
#             print("Acces granted")
#
#         break
#     else:
#         print("You excedded number of tries.")

# def for_loop():
#     max_tries = 3
# la curs

# from time import monotinic_ns, sleep
#
# def iterante_with_while(numbers):
#     start_time = monotinic_ns()
#
#     print("Iterate using 'While' loop.")
#     time.sleep(1)      # =intarziere 1 secunda
#     index = 0
#     while index < len(numbers):
#         #print(numbers[index])
#         index += 1
#     end_time = monotinic_ns()
#     execution_time = end_time - start_time
#     print(f"Execution time: ")
#
# def iterate_with_for(numbers):
#     print("Inerate using 'for' loop. ")
#     for number in numbers:
#         print(number)
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3] ###numbers = list(range(1000000))
#
#     iterate_with_for(numbers)
#     iterante_with_while(numbers)
#
# #### CU cat listele sunt mai lungi while va dura mai mult , for mai repede. Execution time.
#     # while_loop()
#     # for_loop()
# ### Este mult mai eficient sa folosim for , nu while. Numar cunoascut.
#
#
# # fara mosificare de functie.
#
# def execution_time():
#     def a():
#         pass
#     return


## Decorator este o functie care primeste o functie sa o decoreze.

# def execution_time(function_to_decorate):
#     def wrapper (numbers):
#         start_time = monotonic_ns()
#         end_time = monotonic_ns()
#         execution_time = end_time - start_time
#         execution_time_ms = execution_time / 10000000
#         print(f"Execution time: {execution_time_ms}(ms)")
#     return wrapper
#
#
# def iterante_with_while(numbers):
#     print("Iterate using 'While' loop.")
#     index = 0
#     while index < len(numbers):
#         index += 1
#
# def iterate_with_for(numbers):
#     print("Inerate using 'for' loop. ")
#     for number in numbers:
#         pass
#
#
# if __name__ == "__main__":
#     numbers = list(range(10000000))
#     decorated_list_with_while = execution_time(iterante_with_while)
#     decorated_list_with_while(numbers)


# def s(a, b):
#     return a + b
# if __name__ == "__main__":
#
#
# ###### f2(*args) = f2(1, 2, 3, 4, 5 ......)  va lua elementul din tuplu.

#
# """"Documentatie"""
#
# from functools import wraps # pe baza functiei f
# # primeste un argument.
#
# def dec(f):
#     wraps(f)
#
# ##f2.__wrapped__(10) # accces la functia fara decorator.


# @def_with_parameter (15) # o functie care apeleaza

########## Functia map ######### este folosita sa obtinem o lista de aceleasi segmente avand alte elemente.

# my_list = list(range(100))
# ## [0 , 1, 2, 3]   ---->  [0, 1, 4, 9]
# # mapped_list = []
# # for element in my_list:
# #     mapped_list.append(element **2)
# # print('mapped_list')
#
# # metoda map
# #my_list = list(map(lambda element: element ** 2, my_list))
# my_list = list(map(lambda element: element if element % 2 ==0 else " ", my_list))
# print('my_list', my_list)

## putem sa pastram si lista initial, another_list =
##Exemplu - curs

#list comprehention

# my_list = list(range(10))
# my_list = [number for number in my_list if number % 3 == 0]
# print('my_list', my_list)
#
# Putem folosi mai mult de liste.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10]
# output = [n for n in my_list if n % 2 == 0]
# output = list(n for n in my_list if n % 2 == 0)
# output = tuple(n for n in my_list if n % 2 == 0)
# output = set(n for n in my_list if n % 2 == 0)
# print('output'.....)

# ## funtia zip - asocieri de secvente
#
# # animals = ["cat", "dog", "elephant", "fish"]
# # children = ["Ionut", "Daniel", "Marcel"]
# #
# # output = []
# # for index, animal in enumerate(animals):
# #     output.append((animal, children[index]))
# #     except IndexError
# #     pass
# # print(output)
#
# ##### ---> metoda zip
# #
# animals = ["cat", "dog", "elephant", "fish"]
# children = ["Ionut", "Daniel", "Marcel"]
# output = list(zip(animals,children))
# print('output', output)
# #
# # ## The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
# # ## iterator is paired together, and then the second item in each passed iterator are paired together etc.
# # ## Shortest seqvence from all the list.
#
# ### zip_longest - asociaza elementele care nu au val cu None , sau definim fillvalue = .....


# Ex 1.
# keys = ["name", "grade", "city"]
# values = ["Mihai", 5 , "Craiova"]
# output = dict(zip(keys, values))
# print('output', output)
# #dict([("k1", "v1")........])

# keys = ["name", "grade", "city"]
# student = [
#     ["Mihai", 5 , "Craiova"],
#     ["Ionut", 5 , "Iasi"],
#     ["Marcel", 5 , "Sibiu"]
# ]
# output = [
#     dict(zip(keys,student))
#     for student in students
# ]
# print('output', output)
#
# ##sau
# output = {key: value for key, value in zip(keys, value)} ### este vorba de dictionar.

