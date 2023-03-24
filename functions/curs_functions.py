# Functii
# print - scrie in terminal.
# def my_functio(parametrii):  numele nostru si caracterul :

# def my_first_function():   #definim o functie
#     print("Hello from my first function")
#
# # apelam o functie
# my_first_function()
#
# def my_first_function():
#     print("Hello from my first function")
#     print("sum of 5 + 7", 5 + 7)
#     print("End of my function! Good bye")
# print('--Before Function Call')
# print('--After Function Call')


# show_sum_of_numbers()

# Varianta 1
# def show_sum_of_numbers():
#     while True:
#         try:
#             a = int(input("a = "))
#             break
#         except ValueError:
#             print("Value")
#
#     while True:
#         try:
#             b = int(input("a = "))
#             break
#         except ValueError:
#             print("Value")
#
#
#     print(f"Sum of {a} and {b} is {a + b}")
#
#
# show_sum_of_numbers()
# show_sum_of_numbers()
# show_sum_of_numbers()  # folosesc codul de 3 ori.

#Metoda care sa retuneze un rezultat
#ne folosim de return ---
#return - imi va retuna o valoare care o pot pune in varianbila a , b

# def get_number():
#     number = int(input('number:'))
#     print('number', number)
#     return number
#
# a = get_number()
# print('a = ', a)
# a = get_number()
# print('b = ', b)
# print("Sum = ", a + b)
#


#
#  def get_number():
# #     number = int(input('number:'))
# #     print('number', number)
# def show_of_numbers():
# a = get_number()
# a = get_number()
# print('First number is: ', a)
# print('First number is: ', b)
# print("Sum = ", a + b)

# Varianta 2
#
# def get_numbers():
#     number = input("number:")
#     return int(number)
#
# def get_validated_number():
#     while True:
#         try:
#             number = get_numbers()
#             break
#         except ValueError:
#             print("Value is not a number")
#
# # def show_sum_of_numbers():
# #     a = get_validated_number()
# #     b = get_validated_number()
# def show_sum_of_numbers(a, b):
#
#
#     #Ce e mai jos e cod duplicat
#     # while True:
#     #     try:
#     #         # a = int(input("a = "))
#     #         a = get_numbers()
#     #         break
#     #     except ValueError:
#     #         print("Value is not a number")
#     #
#     # while True:
#     #     try:
#     #         # b = int(input("a = "))
#     #         b = get_numbers()
#     #         break
#     #     except ValueError:
#     #         print("Value")
#
#     print(f"Sum of {a} and {b} is {a + b}")
# n1 = get_validated_number()
# n2 = get_validated_number()
#
# show_sum_of_numbers(n1, n2)
#
#
# # verificati pentru try except unde tratam exceptiile de la un nivel la celalalt.
#
#
# # def show_sum_of_numbers(a,b):
# #     print(f"Sum of {a} and {b} is {a + b}")
# # show_sum_of_numbers( 2, 3)


#########pauza#####################


# def my_function(my_list):
#     my_list.append(4)
#
# l1 = [1, 2, 3]
# print("1.", l1)
# my_function(l1)
# print("2.", l1)
# # my_function(l1)
# # print("3.", l1)
# parametrii sunt trimisi prin referinta

#Ex 1
# def my_function(my_list):
#      my_list.append(4)
#      return my_list
#
# l1 = [1, 2, 3]
# l2 = my_function(l1)
#
# print("1.", l1)
# print("2.", l2)
# print("3.", l1 == l2)
# print("4.", l1 is l2) # sunt unu si acelasi obiect.

#Ex.2
# def my_function(my_list):
#     my_list = my_list.copy() # list(my_list) , my_list[:] 3 metode de copiere, facem o copie cu acelasi nume , se creeaza o alta locatie de memorie
#     my_list.append(4)
#     return my_list
#
# l1 = [1, 2, 3]     # 1 2 3
# l2 = my_function(l1)  # 1 2 3 4
#
# # ne folosim de assert pentru a testa o eroare.
#
# assert l1 is not l2
# assert l1 != l2
#
# # ATENTIE - append pe o lista inseamna modificare


#Ex.3

# def sort(my_list):
#     pass
#
# numbers = [1 , 6 , 2 ,8 , 3]
# print("Lista sortata", sorted(numbers))
#
# def my_function(a, b):  # a si b sunt parametrii pozitionali.
#     print(a + b)
#
# my_function(2, 3)

# def my_function(a, b):
#     for i in range(b):   #range intre o si valoarea , cu 0 primul element
#         print(a)
#
# my_function(2, 10)         # a si b sunt parametrii pozitionali si required
# my_function(10, 2)

# def my_function(a, b):
#     print(str(a) * b)
#
# my_function(10, 2)

########################################################### Ziua 2

# def f(param_1="abc"): #parametrii optional - sunt de tip cheie valoare
#     print(param_1)
#
# f()   #se va afisa stringul abc default
# f("def") #se va afisa def , va fi prelut string.


# def f(param_1, param_2, param_3="abc"): #parametrii pozitionali sunt inaintea celor optional de tip cheie valoare
#     print(param_1, param_2, param_3)
#
# f("a", "b")

# def do_math(a, b, operation='+'):
#     if operation == "+":
#         return a * b
#
#     if operation == "/":
#         return a / b
#
#     if operation == "-":
#         retunr a-b
#     return a + b
#
# print(do_math(2, 7))
#
# # return - se iese din functie.

# Exercitiu
# def f(a,b):
#     print(a)
#     print(b)
#
# f(10, -5)
#
# #variable lenght arguments

# def f(*args):
#     print(args)
# f()
# f(10, -5, 7, 2)
# # rezultatul este un tuplu

#Ex3
# def f(a, b , c, *args, param1="abc"):  #*args este un tuplu , se trece la final si contine toti parametri operationali
#     print(a, b, c, args, param1)
#
# # f()
# f(10, -5, 7, 2, 5, 10, param1= "ggg")    # rezultatul 10 -5 7 (2, 5, 10) ggg

# #Ex4
# def f(*args, **kwargs):  #kwargs - parametrii cheie valoare. kw- keyword
#     print(args, kwargs)
#
# f()
# f(1 ,2 ,3)
# f(1, 2, 3, 4, 5)
# f(1, 2, 3, 4, pl=2, p2="abc", p3=[12, 3])
#
# # rezultat (1, 2, 3, 4) {'pl': 2, 'p2': 'abc', 'p3': [12, 3]}

# #Exexple
#
# def f1():
#     pass
# def f1(a):
#     pass
# def f2(a, k1=None):
#     pass
#
# def f4(*args):
#     pass
#
# def f(a, b, *args, k1=None, k2=None, k3=None, **kwargs):
#     pass

# Proprietati ale functiilor

# def f(a,b):
#     return a + b
# ##1
# # a = f
# # print(a(2, 7))
#
# ##2
# def g(my_function):
#     return my_function(2, 7)
# print(g(f))

##new
#
# def g():
#     def f(a, b):
#         return a + b
#     return f
# a = g()
# print(a(2, 7))

##Exemplu
# my_variable = 10
# def f():
#     def g():
#         print("my variable", my_variable)
#
#     my_variable = 20
#     g()
#     print("my variable", my_variable)
#
# my_variable = 10
#
# f()
# print("my variable", my_variable)
#
# # in Pyton exista mai multe namespace-uri - 4 ( 1- built-in, 2. global, 3. enclosing, 4. local)  - python cauta invers
# # tot ce este in interiorul functiei este in namespace local.
# # daca avem g in interiorul f , g face parte din namespace local al lui f.



# def g():
#     def f(a, b):
#         return a + b
#     return f

# def f():
#     def int(x):                             #int este o functie in built in namespace, atentie la nume.
#         return "ha, ha"
#
#     a = int("10")    # local namespace
#     print(a)
#
# a = int("12")       # global
# print(a)
#
# f()

##print(dir(__builtins__))

#Cazuri recursivitate print all numbers from 0 to n

# def f(n):
#     print(n)
#
#     if n == 0:
#         return #returneaza
#
#     f(n - 1) #aici nu returneaza
#
# f(5) # 0,1,2,3,4,5

# def f(n):
#     # if n > 0:
#     #     previous_list = f(n - 1)
#     #     print("previous_list", previous_list)
#     # return[n]
#     if n == 0:
#         return[0]
#     previous_list = f(n - 1)
#     previous_list.append(n)
#     # print("previous_list", previous_list)
#     return previous_list
#
# l = f(5)  # programul revine de unde a ramas.
# print("function result", l)


#Exercitii

# TYPE HINTS / TYPE ANNOTATION

# def f(a:int, b:int):
#     print(a + b)\
#
# f(2, 5)
# f("abc", "def")
# f([1, 2, 4], [3, 4])


# def f(n:int):
#     return list(range(n))
#
# my_list = f(5)
# print('my_list', my_list)


#Cursul 3
#
# def my_function():
#     pass

# numbers = [6, 8, 5, 2, 4, 2, 3 ]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)

# def get_student_grade(student: dict) -> int:  #renuntam la definirea unei functii
#     return student["grade"]

# ##get_student_grade = lambda student: student["grade"] #functii anonime
#
# students = [
#     {"name": "A", "grade": 6},
#     {"name": "B", "grade": 8},
#     {"name": "C", "grade": 5},
#     {"name": "D", "grade": 2},
#     {"name": "E", "grade": 4},
#     {"name": "F", "grade": 2},
#     {"name": "G", "grade": 3},
# ]
# sorted_students = sorted(students, key=lambda student: student["grade"]) # va exista in memorie cand e intalnita. # student este o variabila = x
# # putem avea mai multe valori *args, **kwargs
# # doar returneaza
# print('sorted_students', sorted_students)
#
# ## Returnez valoarea: sorted_students [{'name': 'D', 'grade': 2}, {'name': 'F', 'grade': 2}, {'name': 'G', 'grade': 3}, {'name': 'E', 'grade': 4}, {'name': 'C', 'grade': 5}, {'name': 'A', 'grade': 6}, {'name': 'B', 'grade': 8}]
#

¿
### unde putem folosi lambda sau nu - in fct de context ###

########
##### Pauza #######
### 2 algoritmi care calculeaza cate numere pare sunt in segvente



# my_sequence = range()

###########  Module si pachete





