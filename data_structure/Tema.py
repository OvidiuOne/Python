numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("Lista mea:", (numbers))

print("Lista ordonata ascendent:", sorted(numbers))

print("Lista ordonata descendent:", sorted(numbers, reverse=True))

even_numbers = sorted(numbers)[1::2]
print("Numerele pare:", even_numbers)

odd_numbers = sorted(numbers)[::2]
print("Numerele impare:", odd_numbers)

#multiplu ai nr 3 - lista aranjata
multiples_of_3 = sorted(numbers)[2::3]
print("Multiplu de 3:", multiples_of_3)

#multiplu ai nr 3 - lista nearanjata
multiples_3 = [x for x in numbers if x % 3 == 0]
print("Multiplu de 3 nearanjat", multiples_3)