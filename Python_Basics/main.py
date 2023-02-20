#1. exemplu 1
#varsta_copil_mic = 10
#varsta_copil_mare = 12
#print(varsta_copil_mic, varsta_copil_mare)
#print("copil mic = ", varsta_copil_mic)
#print("copil mare = ", varsta_copil_mare)

#2. exemplu 2
#nr_1 = 5
#nr_2 = 2
#nr_3 = 7 * 8
#nr_3 = nr_1 + 2
#nr_3 = nr_1 + nr_2
#nr_3 = nr_1 % nr_2
#nr_3 = (nr_1 % nr_2) == 1
#print('nr1 =',nr_1 , '; nr2 =',nr_2 , '; nr3 =', nr_3)

#a = 10
#print('a', a)
#print('id(a)', id(a))

#3. exemplu 3
#a = 3
#print('a = ', a)
#a = a + 5
#print('a = ', a)
#b = 4

#4. exemplu 4
# a = 4
# print(a, type(a))
# a = True
# print(a, type(a))

#5. exemplu 5
# wewdkdw = None #null --> from other languages.
# indiferent ca foolosim "" sau '' - doar sa folosim la fel in program.

#6. exemplu 6
# a = ""
# print("_", a , "_")
# print(type(a))

#7. exemplu 7
# message = 'Mihai, alias \'M\', a zis "Buna ziua!"'
# print(message, type(message)) # Mihai a zis "Buna ziua!"
# \ Caracterul care il urmeaza nu mai are acelasi rol fata de cel normal.
# message = 'Mihai, alias \'M\', a zis "Buna ziua!" \\ \'Salut!\' Ii raspunde Ionut'
# #Daca avem nevoie sa afisa un \ , il dublam sa il afisez.
# print(message, type(message)) # Mihai a zis "Buna ziua!"

#8. exemplu 8
#print("linia 1\n\nlinia 2")  # \b - backspake \n rand nou, \t aliniat
#print("linia 1\n\n\tlinia 2") # do the sameusing RAW string r - anuleaza

#9. exemplu 9
# my_name = "Mihai"
# my_age = 30
# my_city = "Craiova"
# #message = ("My name is Mihai, i am 30 years old and I am living in Craiova")
# message = ("My name is " + my_name + ", i am " + str(my_age) + " years old and I am living in " + my_city )
# print(message)
# avem 6 striguri

#Var 1 - sa formatam stringuri %
# my_name = "Mihai"
# my_age = 30
# my_city = "Craiova"
# message = ("My name is %s, i am %d years old and I am living in %s.") % (my_name, my_age, my_city)
# print(message)

#Var 2 - sa formatam stringuri .format - putem sa alegem ordinea
# my_name = "Mihai"
# my_age = 30
# my_city = "Craiova"
# #message = "My name is {1}, i am {2} years old and I am living in {0}.".format(my_name, my_age, my_city)
# putem sa dam ordinea, 0 , 1 , 2 , 3 , 4                                          0       1           2
# message = "My name is {name_1}, i am {my_second_guess} years old and I am living in {bla_bla}.".format(name_1=my_name, bla_bla=my_city, my_second_guess=my_age)
# message = "My name is {name}, i am {age} years old and I am living in {city}.".format(name=my_name, city=my_city, age=my_age)
# print(message)
# depasirea limitei de 120 caractere - recomandare

# #Var 3 - f-string sa interpolam valorile variabilelor direct in string. Cea mai folosita.
# my_name = "Mihai"
# my_age = 30
# my_city = "Craiova"
# message = f"My name is {my_name}, i am {my_age} years old and I am living in {my_city}."
# print(message)

# un caracter este tot un sir de caractere.

#functii
# print("print something in console")
# print(type(12))
# print(id(12)) aflam locatia de memorie

# a=3   - numar intreg
# b=3.0   - numar float
# print(a == b, a is b) # == verifica valoare , is verifica daca e acelasi obiect.

# a = 7
# print(a is 7) #SyntaxWarning: "is" with a literal. Did you mean "=="?