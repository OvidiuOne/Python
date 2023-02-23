# my_list = []
# print(my_list, type(my_list))  # o lista goala.

# my_numbers = [2, 4, -3, 12, 10, -15]
# #             0  1   2   3   4   5
# print(my_numbers[3])
# print(my_numbers[6]) # index error - nu folosim- tratare exceptii

# my_numbers = ['a', 'b', -3, 12, 10, -15]
#             -6 -5 -4 -3  -2   -1
# print(my_numbers[-4])   # indexi negativi
# print("lenght of the list =", len(my_numbers)) # len -  aflam cate elemente are lista.
# slice = my_numbers[::] #shallow copy este la fel cu my_numbers[0:len(my_numbers):1]
# slice: my_numbers[start:end:step]         # slice - sa obtinem alta lista din lista existenta
# start face parte din secventa, end nu face parte din secventa , step default este 1
# print(slice, type(slice))      # am copiat lista
# slice = my_numbers[1:4:2]
# print(my_numbers, type(my_numbers))
# print(slice, type(slice))
# slice = my_numbers[::-1] # lsita in ordine inversa

# #adaugare element in lista.
# my_numbers = ['a', 'b', 'c', 'd', 'e', 'd']
# print(my_numbers)
# my_numbers.append('g')    #append pune la final , inserd dai pozitia.
# print(my_numbers)

# my_string = "Ana are mere"
# print(my_string[::])
# my_list = list(my_string)
# print(my_list, type(my_list))

# a = [1, 2, 3]
# b = a
# print(a==b. a is b) # == verificam
# a.append(4)
# b.append(5)

#Structura de data - Tupluri (paranteze rotunde) - 90% ca si listele si este immutable(nu poate fi modificata, adauga sau strerge)
# exemnplu luniile anului, date care nu se modifica si ocupa mai putin loc in memorie.
# my_tuple = (1, 2, 3, True, 'decembrie', -4)
# print('my tuple', my_tuple, type(my_tuple))
# print(my_tuple[-2])

#Exemplu
# my_tuple = (1, 2, 3)
# print(my_tuple)
# my_list = list(my_tuple)
# print(my_list, type(my_list))
# my_list.append(4)
# my_tuple = tuple(my_list)  # cel de sus nu va mai exista, va fi sters.
# print('my_tuple', my_tuple)

# a = (1, 2, 3)
# c = a
# a = (1, 2, 3, 4)
# b = a
# print(a, b, c)

# my_list = [1, 2, 3]
# my_tuple = ('a', my_list, 'b')
# print('my_tuple', my_tuple, type(my_list))
# my_list.append(4)    # modificarea elementului
# print('my_tuple', my_tuple, type(my_list))

# Structura de date - dictionare. {} de forma cheie:valoare
# my_dict = {}
# print(my_dict, my_dict, type(my_dict))

# my_dict = {"name": "Mihai", "age": 30}
# print(my_dict, my_dict, type(my_dict))
#
# my_dict = {
#     "name": "Mihai",
#     "age": 30
# }
# print(my_dict, my_dict, type(my_dict))

#Exemple
# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     2: [1, 2, 3],
#     3: "abc",
#     4: "abc",
#     (1, 2, "a"): {"a": 1, "b": [1, 2, 3]},
#     3: 100    # cheile nu pot fi duplicate , ultima valoare va avea prioritate.
# }
# print(my_dict, type(my_dict))

# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200,
# }

# print(my_dict["age"])
# print(my_dict["name"])
# print(my_dict["city"])
# # print(my_dict["sssss"])  # Key errorr

# my_dict["age"] = 31
# print(my_dict["age"])
# my_dict["country"] = "Romania"
# print(my_dict)
# del my_dict["height"]
# print(my_dict)


# # Exemplu de lista cu dictionar
# student_1 = {"name": "Mihai"}
# student_2 = {"name": "Ionel"}
# student_3 = {"name": "Gigel"}
#
# students = [student_1, student_2, student_3]
# print(students)
# student_2["promoted"] = True # adaugare in lista
# print(students)


#Metoda keys , values, items
# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200
# }
# #print(my_dict.keys()))
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))
#
# Exemplu
# print("are" in "ana are mere")
# print(10 in [1, 10, 100])
# print(10 in (1, 10, 100))
# print("name in {"name": "Mihai": "age": 30}")
# print("Mihai in {"name": "Mihai": "age": 30}".values())

#Exemplu   - get
# my_dict = {
#     "name": "Mihai",
#     "age": 30,
#     "city": "Craiova",
#     "height": 200
# }
# # print(my_dict["country"])   #KeyError
# print(my_dict.get("country"))   #echivalenta print(my_dict.get("country", None))

#Structura de date - seturi   - elementele din set sunt imutable.

# # my_set = {} # this is not a set, it's an empty dictionary.
# my_set = {0, 1, 2, None, 3, True, False, "abc", "aaa"}  # pentru a econimisi memorie 1 si True este acelasi lucru , False si 0.
# print(my_set, type(my_set))
# print(hash(1))
# print(hash(True))       # hash-ul este identic

# #Exemplu
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)
# #Putem sa adaugam si sa scoatem elemente unice ( fara duplicate)

#Exemplu pop - (la lista soate ultimul element)
# my_set = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0}
# my_set.pop()
# my_set.pop()
# my_set.pop()
# print(my_set)
# print(len(my_set))

# my_set_1 = {1, 2, 3}
# my_set_2 = {2, 3, 4}
# print(my_set_1.union(my_set_2)) #uniunea distre seturi
# print(my_set_1.intersection(my_set_2))

# Exercitiu propriu
# list1 = [1, 2, 3, 4]
# list2 = [i**2 for i in list1]
# print(list2)