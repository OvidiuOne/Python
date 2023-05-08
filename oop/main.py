# def Person():
#     return
#
# class Person:
#     pass
class Person:
    def __init__(self, first_name, last_name):    #magic metods - rol predefinit   # self - instanta pentru care a fost apelata
        self.first_name = first_name
        self.last_name = last_name
    def intro_to_all(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}!")



if __name__ == '__main__':
    popescu_ion = Person("Popescu", "Ion")

    print(popescu_ion.first_name, popescu_ion.last_name)
    george_dinel = Person("George", "Dinel")

    print(george_dinel.first_name, george_dinel.last_name)


    # print(type(popescu_ion))
    # print(type(Person))




# popescu_ion = Person() # se apeleaza by default o functie
